# -*- coding: utf-8 -*-

from typing import Dict, Callable, Optional, Any
from .utility import Algorithm, ObjFunc, FVal

class Genetic(Algorithm):

    def __init__(
        self,
        func: ObjFunc[FVal],
        settings: Dict[str, Any],
        progress_fun: Optional[Callable[[int, str], None]] = None,
        interrupt_fun: Optional[Callable[[], bool]] = None
    ):
        """The format of argument `settings`:

        + `nPop`: Population
            + type: int
            + default: 500
        + `pCross`: Crossover rate
            + type: float (0.~1.)
            + default: 0.95
        + `pMute`: Mutation rate
            + type: float (0.~1.)
            + default: 0.05
        + `pWin`: Win rate
            + type: float (0.~1.)
            + default: 0.95
        + `bDelta`: Delta value
            + type: float
            + default: 5.
        + `max_gen` or `min_fit` or `max_time`: Limitation of termination
            + type: int / float / float
            + default: Raise `ValueError`
        + `report`: Report per generation
            + type: int
            + default: 10

        Others arguments are same as [`Differential.__init__()`](#differential9595init__).
        """
        super(Genetic, self).__init__(...)
        ...
