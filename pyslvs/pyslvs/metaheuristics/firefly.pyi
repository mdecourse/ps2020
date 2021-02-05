# -*- coding: utf-8 -*-

from typing import Dict, Callable, Optional, Any
from .utility import Algorithm, ObjFunc, FVal

class Firefly(Algorithm):

    def __init__(
        self,
        func: ObjFunc[FVal],
        settings: Dict[str, Any],
        progress_fun: Optional[Callable[[int, str], None]] = None,
        interrupt_fun: Optional[Callable[[], bool]] = None
    ):
        """The format of argument `settings`:

        + `n`: Population
            + type: int
            + default: 80
        + `alpha`: Alpha factor
            + type: float (0.~1.)
            + default: 0.01
        + `beta_min`: Minimal attraction
            + type: float (0.~1.)
            + default: 0.2
        + `beta0`: Attraction rate
            + type: float (0.~1.)
            + default: 1.
        + `gamma`: Gamma rate
            + type: float (0.~1.)
            + default: 1.
        + `max_gen` or `min_fit` or `max_time`: Limitation of termination
            + type: int / float / float
            + default: Raise `ValueError`
        + `report`: Report per generation
            + type: int
            + default: 10

        Others arguments are same as [`Differential.__init__()`](#differential9595init__).
        """
        super(Firefly, self).__init__(...)
        ...
