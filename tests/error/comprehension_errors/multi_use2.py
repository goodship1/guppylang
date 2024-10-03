import guppylang.prelude.quantum as quantum
from guppylang.decorator import guppy
from guppylang.module import GuppyModule
from guppylang.prelude.quantum import qubit
from guppylang.prelude.builtins import owned

module = GuppyModule("test")
module.load_all(quantum)


@guppy(module)
def foo(qs: list[qubit] @owned, xs: list[int]) -> list[qubit]:
    return [q for x in xs for q in qs]


module.compile()
