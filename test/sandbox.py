from itertools import islice

from snake_eyes import *

g = UnshiftedGeometricDistribution(1)
print(g.support_space().minimum())
z = g.zip(g)

ss = z.support_space()
print(list(islice(ss, 20)))
