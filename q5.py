import numpy as np
import collections as col

def question05(allowedAllocations, totalValue):
  allocs = 0
  blocks = col.deque(sorted(allowedAllocations))
  while totalValue > 0:
    totalValue = totalValue - blocks.pop()
    allocs = allocs + 1
  return allocs