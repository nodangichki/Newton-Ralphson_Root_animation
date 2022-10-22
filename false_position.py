'''
script help
 user defined variables:
   xu / xl => initial values for upper and lower bounds
   iterations => maximum no of iterations to run
   expression => function to find root of
   error_break => set to true if you want to break the iterations if a certain error threshold is met
   error_threshold => if error_break is true iterations will stop when this error percentage is met
 !NOT TO CHANGE/SCRIPT VARIABLES!
   previous_value, errors[100], X [DO NOT CHANGE THESE VALUES!]
'''
from sympy import *

x = Symbol('x')  # from symbolic library define x as a symbol for substitution
xu = -15
xl = -10
iterations = 15000
expression = x**3+3*x**2-1
error_break = True   # should the program stop when error threshold is reached?
error_threshold = 0  # error threshold (program will stop when error is <= this value
previous_value = []
errors = [100]

for loops in range(0, iterations):

    f_of_xl = expression.subs(x, xl)  # calculating f(xl)
    f_of_xu = expression.subs(x, xu)  # calculating f(xu)
    xr = round(((xu * f_of_xl) - (xl * f_of_xu)) / (f_of_xl - f_of_xu), 5)  # calculating xr using false position
    f_of_xr = expression.subs(x, xr)  # calculating f(xr)
    if f_of_xr * f_of_xl < 0:  # checking condition f(xr).f(xl) < 0
        xu = xr
    elif f_of_xr * f_of_xl > 0:  # checking condition f(xr).f(xl) > 0
        xl = xr
    previous_value.append(xr)  # keeping previous values of xr for error calculations
    if loops > 0:              # checking condition when iterations are greater than 1, so we can calculate errors
        error = abs(((xr - previous_value[loops - 1]) / xr)) * 100
        errors.append(error)
    print(f' itter = {loops+1} root = {xr} error is: {errors[loops]}%')  # formatted string to print data in terminal
    if error_break == True and errors[loops] <= error_threshold:
        break       # break for loop when error threshold is reached

