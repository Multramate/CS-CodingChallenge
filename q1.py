import numpy as np
import itertools as it

def question01(portfolios):
  max_value = 0
  for (portfolio_1, portfolio_2) in it.combinations(portfolios, r = 2):
    new_value = portfolio_1 ^ portfolio_2
    if new_value > max_value:
      max_value = new_value
  return max_value