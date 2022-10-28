from fa_purity.cmd import (
    Cmd,
)
from fa_purity.frozen import (
    FrozenList,
)
from fa_purity.pure_iter.factory import (
    from_flist,
    from_range,
)
from fa_purity.stream.core import (
    Stream,
)
from fa_purity.stream.factory import (
    from_piter,
)
from fa_purity.stream.transform import (
    chain,
    consume,
    filter_opt,
    squash,
    until_none,
)
import pytest
from tests.stream._utils import (
    assert_different_iter,
    rand_int,
)
from typing import (
    Optional,
)


def _equal(a: int, b: int) -> None:
    assert a == b


def _mock_stream_opt(
    size: int, none_at: Optional[int]
) -> Stream[Optional[int]]:
    items = from_range(range(size)).map(
        lambda i: rand_int().map(lambda r: r if none_at != i else None)
    )
    return from_piter(items)


def test_chain_1() -> None:
    base = from_flist((1, 2, 3))
    items = base.map(lambda i: Cmd.from_cmd(lambda: i))
    stm = from_piter(items)
    unchained = stm.map(lambda _: base)
    chained = chain(unchained)
    assert_different_iter(chained)

    def _verify(elements: FrozenList[int]) -> None:
        assert elements == (1, 2, 3) * 3

    with pytest.raises(SystemExit):
        chained.to_list().map(_verify).compute()


def test_chain_2() -> None:
    base = from_flist((1, 2, 3))
    items = base.map(lambda i: Cmd.from_cmd(lambda: i))
    stm = from_piter(items)
    unchained = base.map(lambda _: stm)
    chained = chain(unchained)
    assert_different_iter(chained)

    def _verify(elements: FrozenList[int]) -> None:
        assert elements == (1, 2, 3) * 3

    with pytest.raises(SystemExit):
        chained.to_list().map(_verify).compute()


def test_consume() -> None:
    mutable = [0]

    def _mutate(i: int) -> Cmd[None]:
        def _action() -> None:
            mutable[0] = i

        return Cmd.from_cmd(_action)

    items = from_range(range(10)).map(lambda i: Cmd.from_cmd(lambda: i))
    stm = from_piter(items).map(lambda i: _mutate(i))
    result = consume(stm)

    def _verify() -> None:
        assert mutable[0] == 9

    assert mutable[0] == 0
    with pytest.raises(SystemExit):
        result.map(lambda _: _verify()).compute()


def test_squash() -> None:
    items = from_range(range(10)).map(lambda _: rand_int())
    stm = from_piter(items).map(lambda _: rand_int())
    result = squash(stm)
    assert_different_iter(result)


def test_filter_opt() -> None:
    stm = _mock_stream_opt(10, 5)
    stm_len = filter_opt(stm).to_list().map(len)
    with pytest.raises(SystemExit):
        stm_len.map(lambda n: _equal(n, 9)).compute()


def test_until_none() -> None:
    stm = _mock_stream_opt(10, 5)
    stm_len = until_none(stm).to_list().map(len)
    with pytest.raises(SystemExit):
        stm_len.map(lambda n: _equal(n, 5)).compute()
