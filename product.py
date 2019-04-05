#!/usr/bin/env python3

from functools import reduce

print(reduce(lambda x, y: x*y, list(range(1, 11))))

