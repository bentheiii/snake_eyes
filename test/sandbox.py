from itertools import islice

from snake_eyes import *

d6 = die(6)

ex = explode(d6)

print(ex.approx_mean(sample_size=1_000_000))
