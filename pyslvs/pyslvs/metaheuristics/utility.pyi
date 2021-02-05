# -*- coding: utf-8 -*-

from abc import abstractmethod
from typing import TypeVar, Tuple, Sequence, Dict, Callable, Optional, Generic, Any
from numpy import ndarray, double

FVal = TypeVar('FVal')


class ObjFunc(Generic[FVal]):

    @abstractmethod
    def fitness(self, v: ndarray) -> double:
        """(`cdef` function) Return the fitness from the variable list `v`.
        This function will be directly called in the algorithms.
        """
        ...

    @abstractmethod
    def result(self, v: ndarray) -> FVal:
        ...


class Algorithm(Generic[FVal]):

    func: ObjFunc[FVal]

    def __class_getitem__(cls, item):
        # PEP 560
        raise NotImplemented

    @abstractmethod
    def __init__(
        self,
        func: ObjFunc[FVal],
        settings: Dict[str, Any],
        progress_fun: Optional[Callable[[int, str], None]] = None,
        interrupt_fun: Optional[Callable[[], bool]] = None
    ):
        """The argument `func` is an object inherit from [ObjFunc],
        and all abstract methods should be implemented.

        The format of argument `settings` can be customized.

        The argument `progress_fun` will be called when update progress,
        and the argument `interrupt_fun` will check the interrupt status from GUI or subprocess.
        """
        ...

    def history(self) -> Sequence[Tuple[int, float, float]]:
        ...

    def run(self) -> FVal:
        ...
