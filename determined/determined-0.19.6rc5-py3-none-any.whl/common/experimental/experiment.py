import enum
import sys
import time
from typing import Any, Dict, List, Optional

from determined.common import api
from determined.common.api import bindings
from determined.common.experimental import checkpoint, trial


# Wrap the autogenerated bindings in something a little more ergonomic.
class ExperimentState(enum.Enum):
    UNSPECIFIED = bindings.determinedexperimentv1State.STATE_UNSPECIFIED.value
    ACTIVE = bindings.determinedexperimentv1State.STATE_ACTIVE.value
    PAUSED = bindings.determinedexperimentv1State.STATE_PAUSED.value
    STOPPING_COMPLETED = bindings.determinedexperimentv1State.STATE_STOPPING_COMPLETED.value
    STOPPING_CANCELED = bindings.determinedexperimentv1State.STATE_STOPPING_CANCELED.value
    STOPPING_ERROR = bindings.determinedexperimentv1State.STATE_STOPPING_ERROR.value
    COMPLETED = bindings.determinedexperimentv1State.STATE_COMPLETED.value
    CANCELED = bindings.determinedexperimentv1State.STATE_CANCELED.value
    ERROR = bindings.determinedexperimentv1State.STATE_ERROR.value
    DELETED = bindings.determinedexperimentv1State.STATE_DELETED.value
    DELETING = bindings.determinedexperimentv1State.STATE_DELETING.value
    DELETE_FAILED = bindings.determinedexperimentv1State.STATE_DELETE_FAILED.value
    STOPPING_KILLED = bindings.determinedexperimentv1State.STATE_STOPPING_KILLED.value
    QUEUED = bindings.determinedexperimentv1State.STATE_QUEUED.value
    PULLING = bindings.determinedexperimentv1State.STATE_PULLING.value
    STARTING = bindings.determinedexperimentv1State.STATE_STARTING.value
    RUNNING = bindings.determinedexperimentv1State.STATE_RUNNING.value

    def _to_bindings(self) -> bindings.determinedexperimentv1State:
        return bindings.determinedexperimentv1State(self.value)


class ExperimentReference:
    """
    An ExperimentReference object is usually obtained from
    ``determined.experimental.client.create_experiment()``
    or ``determined.experimental.client.get_experiment()``.

    Helper class that supports querying the set of checkpoints associated with an
    experiment.
    """

    def __init__(
        self,
        experiment_id: int,
        session: api.Session,
    ):
        self._id = experiment_id
        self._session = session

    @property
    def id(self) -> int:
        return self._id

    def _get(self) -> bindings.v1Experiment:
        """
        _get fetches the main GET experiment endpoint and parses the response.
        """
        resp = bindings.get_GetExperiment(self._session, experimentId=self._id)
        return resp.experiment

    def activate(self) -> None:
        bindings.post_ActivateExperiment(self._session, id=self._id)

    def archive(self) -> None:
        bindings.post_ArchiveExperiment(self._session, id=self._id)

    def cancel(self) -> None:
        bindings.post_CancelExperiment(self._session, id=self._id)

    def delete(self) -> None:
        """
        Delete an experiment and all its artifacts from persistent storage.

        You must be authenticated as admin to delete an experiment.
        """
        bindings.delete_DeleteExperiment(self._session, experimentId=self._id)

    def get_config(self) -> Dict[str, Any]:
        return self._get().config

    def get_trials(
        self,
        sort_by: trial.TrialSortBy = trial.TrialSortBy.ID,
        order_by: trial.TrialOrderBy = trial.TrialOrderBy.ASCENDING,
    ) -> List[trial.TrialReference]:
        """
        Get the list of :class:`~determined.experimental.TrialReference` instances
        representing trials for an experiment.

        Arguments:
            sort_by: Which field to sort by. See :class:`~determined.experimental.TrialSortBy`.
            order_by: Whether to sort in ascending or descending order. See
                :class:`~determined.experimental.TrialOrderBy`.
        """

        def get_with_offset(offset: int) -> bindings.v1GetExperimentTrialsResponse:
            return bindings.get_GetExperimentTrials(
                self._session,
                experimentId=self._id,
                offset=offset,
                orderBy=bindings.v1OrderBy(order_by.value),
                sortBy=bindings.v1GetExperimentTrialsRequestSortBy(sort_by.value),
            )

        resps = api.read_paginated(get_with_offset)

        return [trial.TrialReference(t.id, self._session) for r in resps for t in r.trials]

    def kill(self) -> None:
        bindings.post_KillExperiment(self._session, id=self._id)

    def pause(self) -> None:
        bindings.post_PauseExperiment(self._session, id=self._id)

    def unarchive(self) -> None:
        bindings.post_UnarchiveExperiment(self._session, id=self._id)

    def wait(self, interval: float = 5.0) -> ExperimentState:
        """
        Wait for the experiment to reach a complete or terminal state.

        Arguments:
            interval (int, optional): An interval time in seconds before checking
                next experiement state.
        """
        elapsed_time = 0.0
        while True:
            exp = self._get()
            if exp.state in (
                bindings.determinedexperimentv1State.STATE_COMPLETED,
                bindings.determinedexperimentv1State.STATE_CANCELED,
                bindings.determinedexperimentv1State.STATE_DELETED,
                bindings.determinedexperimentv1State.STATE_ERROR,
            ):
                return ExperimentState(exp.state.value)
            elif exp.state == bindings.determinedexperimentv1State.STATE_PAUSED:
                raise ValueError(
                    f"Experiment {self.id} is in paused state. Make sure the experiment is active."
                )
            else:
                # ACTIVE, STOPPING_COMPLETED, etc.
                time.sleep(interval)
                elapsed_time += interval
                if elapsed_time % 60 == 0:
                    print(
                        f"Waiting for Experiment {self.id} to complete. "
                        f"Elapsed {elapsed_time / 60} minutes",
                        file=sys.stderr,
                    )

    def top_checkpoint(
        self,
        sort_by: Optional[str] = None,
        smaller_is_better: Optional[bool] = None,
    ) -> checkpoint.Checkpoint:
        """
        Return the :class:`~determined.experimental.Checkpoint` for this experiment that
        has the best validation metric, as defined by the ``sort_by`` and ``smaller_is_better``
        arguments.

        Arguments:
            sort_by (string, optional): The name of the validation metric to
                order checkpoints by. If this parameter is not specified, the metric
                defined in the experiment configuration ``searcher`` field will be used.

            smaller_is_better (bool, optional): Specifies whether to sort the
                metric above in ascending or descending order. If ``sort_by`` is unset,
                this parameter is ignored. By default, the value of ``smaller_is_better``
                from the experiment's configuration is used.
        """
        checkpoints = self.top_n_checkpoints(
            1, sort_by=sort_by, smaller_is_better=smaller_is_better
        )

        if not checkpoints:
            raise AssertionError("No checkpoints found for experiment {}".format(self.id))

        return checkpoints[0]

    def top_n_checkpoints(
        self,
        limit: int,
        sort_by: Optional[str] = None,
        smaller_is_better: Optional[bool] = None,
    ) -> List[checkpoint.Checkpoint]:
        """
        Return the N :class:`~determined.experimental.Checkpoint` instances with the best
        validation metrics, as defined by the ``sort_by`` and ``smaller_is_better``
        arguments. This method will return the best checkpoint from the
        top N best-performing distinct trials of the experiment. Only checkpoints in
        a ``COMPLETED`` state with a matching ``COMPLETED`` validation are considered.

        Arguments:
            limit (int): The maximum number of checkpoints to return.

            sort_by (string, optional): The name of the validation metric to use for
                sorting checkpoints. If this parameter is unset, the metric defined
                in the experiment configuration searcher field will be
                used.

            smaller_is_better (bool, optional): Specifies whether to sort the
                metric above in ascending or descending order. If ``sort_by`` is unset,
                this parameter is ignored. By default, the value of ``smaller_is_better``
                from the experiment's configuration is used.
        """

        def get_with_offset(offset: int) -> bindings.v1GetExperimentCheckpointsResponse:
            return bindings.get_GetExperimentCheckpoints(
                self._session,
                id=self._id,
                offset=offset,
                states=[bindings.determinedcheckpointv1State.STATE_COMPLETED],
            )

        resps = api.read_paginated(get_with_offset)

        checkpoints = [
            checkpoint.Checkpoint._from_bindings(c, self._session)
            for r in resps
            for c in r.checkpoints
        ]

        if not checkpoints:
            raise AssertionError("No checkpoint found for experiment {}".format(self.id))

        if not sort_by:
            training = checkpoints[0].training
            assert training
            config = training.experiment_config
            sb = config.get("searcher", {}).get("metric")
            if not isinstance(sb, str):
                raise ValueError(
                    "no searcher.metric found in experiment config; please provide a sort_by metric"
                )
            sort_by = sb
            smaller_is_better = config.get("searcher", {}).get("smaller_is_better", True)

        def key(ckpt: checkpoint.Checkpoint) -> Any:
            training = ckpt.training
            assert training
            return training.validation_metrics["avgMetrics"][sort_by]

        checkpoints.sort(reverse=not smaller_is_better, key=key)

        # Ensure returned checkpoints are from distinct trials.
        t_ids = set()
        checkpoint_refs = []
        for ckpt in checkpoints:
            training = ckpt.training
            assert training
            if training.trial_id not in t_ids:
                checkpoint_refs.append(ckpt)
                t_ids.add(training.trial_id)

        return checkpoint_refs[:limit]

    def __repr__(self) -> str:
        return "Experiment(id={})".format(self.id)
