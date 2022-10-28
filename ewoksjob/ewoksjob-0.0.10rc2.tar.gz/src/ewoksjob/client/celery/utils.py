import logging
from typing import List
from celery import current_app
from celery.result import AsyncResult

__all__ = [
    "get_future",
    "cancel",
    "get_result",
    "get_not_finished",
    "get_not_finished_futures",
]


logger = logging.getLogger(__name__)


def get_future(task_id) -> AsyncResult:
    return AsyncResult(task_id)


def cancel(task_id):
    future = get_future(task_id)
    if future is not None:
        future.revoke(terminate=True)


def get_result(task_id, **kwargs):
    kwargs.setdefault("interval", 0.1)
    future = AsyncResult(task_id)
    if future is not None:
        return future.get(**kwargs)


def get_not_finished():
    inspect = current_app.control.inspect()
    task_ids = list()

    workers = inspect.active()  # running
    if workers is None:
        logger.warning("No Celery workers were detected")
        workers = dict()
    for tasks in workers.values():
        for task in tasks:
            task_ids.append(task["id"])

    workers = inspect.scheduled()  # pending
    if workers is None:
        workers = dict()
    for tasks in workers.values():
        for task in tasks:
            task_ids.append(task["id"])

    return task_ids


def get_not_finished_futures() -> List[AsyncResult]:
    lst = [get_future(task_id) for task_id in get_not_finished()]
    return [future for future in lst if future is not None]
