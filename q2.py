import numpy as np
import itertools as it

def question02(cashFlowIn, cashFlowOut):
  ins = map(sum, powerset(cashFlowIn))
  outs = map(sum, powerset(cashFlowOut))
  return min([abs(_in - _out) for _in, _out in it.product(ins, outs)][1:])

def powerset(set):
  ls = list(set)
  ln = len(ls)
  return it.chain.from_iterable(it.combinations(ls, r) for r in range(ln + 1))