# testobj.pyx
cimport cython
from numpy import array, float64 as f64
from pyslvs.metaheuristics.utility cimport ObjFunc

@cython.final
cdef class TestObj(ObjFunc):
    """
    f(x) = x1^2 + 8*x2
    """

    def __cinit__(self):
        self.ub = array([100, 100], dtype=f64)
        self.lb = array([0, 0], dtype=f64)

    cdef double fitness(self, double[:] v) nogil:
        return 1+1/(v[0] * v[1]*(80-v[0]*v[1])/(2.0*(v[0]+v[1]))*v[0] * v[1]*(80-v[0]*v[1])/(2.0*(v[0]+v[1])))

    cpdef object result(self, double[:] v):
        """x = (0, 0)"""
        return tuple(v)