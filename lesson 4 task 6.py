from itertools import cycle
my_list = [i for i in range (0, 10)]
a = cycle (my_list)
print ([next(a) for i in range (0,10)])
from itertools import count

b = count()
print ([next(b) for i in range (0,10)])
