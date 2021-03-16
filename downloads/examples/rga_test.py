# rga_test.py
from numpy import array
from matplotlib.pyplot import plot, show
from pyslvs.metaheuristics import AlgorithmType, ALGORITHM
# from pyslvs.metaheuristics.test import TestObj
from test import TestObj

t = AlgorithmType.RGA
settings = {'max_gen': 1000, 'report': 10, 'parallel': True}
a = ALGORITHM[t](TestObj(), settings)
# Show answer
ans = a.run()
# Plot convergance graph
h = array(a.history())
print(ans)
plot(h[:, 0], h[:, 1], 'ro-')
show()