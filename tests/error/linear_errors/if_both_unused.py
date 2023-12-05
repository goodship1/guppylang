import guppy.prelude.quantum as quantum
from guppy.decorator import guppy
from guppy.module import GuppyModule
from guppy.hugr.tys import Qubit


module = GuppyModule("test")
module.load(quantum)


@guppy.declare(module)
def new_qubit() -> Qubit:
    ...


@guppy(module)
def foo(b: bool) -> int:
    if b:
        q = new_qubit()
    else:
        q = new_qubit()
    return 42


module.compile()
