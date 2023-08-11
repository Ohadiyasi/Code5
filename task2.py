#
##
### created by yseeva
##  aug 6th
# second order equation solver

import math

def solve_second(A,B,C):
    delta= math.pow(B,2) -4*A*C
    if delta>0:
          x1=(-B+math.sqrt(delta))/2*A
          x2=(-B-math.sqrt(delta))/2*A
          print(f"TWO ANSWERS | ANSWERS ARE : \n  x1= {x1}  , x2={x2}")
    elif delta==0:
          x3=B/2*A 
          print(f"ONLY ONE ANSWER \n ANSWER IS : \n x={x3}")
    else:
          print(f" delta is {delta} ")


print("-- WELCOME --")
print(" here we find answers to the desired equation ")
print("please first standardize your very own equation like this =   ax^2 + bx + c = 0")

a=float(input("ENTER a  = > "))

b=float(input("ENTER b = > "))
c=float(input("ENTER c= > "))

solve_second(a,b,c)