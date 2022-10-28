import pytest
from ..client import celery
from ..client import local
from .utils import wait_not_finished


def test_normal(ewoks_worker, tmpdir):
    assert_normal(celery, tmpdir)


def test_normal_local(local_ewoks_worker, tmpdir):
    assert_normal(local, tmpdir)


def test_normal_local_slurm(local_slurm_ewoks_worker, tmpdir):
    assert_normal(local, tmpdir)


def test_cancel(ewoks_worker, tmpdir):
    assert_cancel(celery, tmpdir)


def test_cancel_local(local_ewoks_worker, tmpdir):
    assert_cancel(local, tmpdir)


def test_cancel_local_slurm(local_slurm_ewoks_worker, tmpdir):
    assert_cancel(local, tmpdir)


def assert_normal(mod, tmpdir):
    seconds = 5
    timeout = 10
    filename = tmpdir / "finished.sem"
    future = mod.submit_test(seconds=seconds, filename=str(filename))
    wait_not_finished(mod, {future.task_id}, timeout=timeout)
    results = mod.get_result(future.task_id, timeout=timeout)
    assert results == {"return_value": True}
    assert filename.exists()
    wait_not_finished(mod, set(), timeout=timeout)


def assert_cancel(mod, tmpdir):
    seconds = 10
    timeout = seconds * 2
    filename = tmpdir / "finished.sem"
    future = mod.submit_test(seconds=seconds, filename=str(filename))

    if mod is local:
        # The current implementation does not allow cancelling running tasks
        mod.cancel(future.task_id)
        try:
            results = mod.get_result(future.task_id, timeout=timeout)
        except mod.CancelledError:
            assert not filename.exists()
        else:
            assert results == {"return_value": True}
            assert filename.exists()
            pytest.xfail(f"{mod.__name__} ran until completion")
    else:
        wait_not_finished(mod, {future.task_id}, timeout=timeout)
        mod.cancel(future.task_id)
        try:
            results = mod.get_result(future.task_id, timeout=timeout)
        except mod.CancelledError:
            assert not filename.exists()
        else:
            assert results == {"return_value": True}
            assert filename.exists()
            pytest.xfail(f"{mod.__name__} ran until completion")

    wait_not_finished(mod, set(), timeout=timeout)
