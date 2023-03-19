#implement page rank algorithm
import numpy as np
import scipy as sc
import pandas as pd
from fractions import Fraction

def float_format(vector, decimal ):
    return np.round((vector).astype(float),
                    decimals = decimal)

dp = Fraction(1,3)

M = np.matrix([[0,0,1],[Fraction(1,2),0,0], [Fraction(1,2),1,0]])

E = np.zeros((3,3))
E[:] = dp

beta = 0.8

A= beta* M + ((1- beta)*E)

r = np.matrix([dp,dp,dp])
r = np.transpose(r)

previous_r = r
for i in range(1,10):
    r = A*r
    print(float_format(r,3))
    if (float_format(previous_r,3)==float_format(r,3)).all():
        break
    previous_r=r

print("Final:\n", float_format(r,3))
print("sum", np.sum(r))
  