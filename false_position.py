from sympy import *

x = Symbol('x')  # from symbolic library define x as a symbol for substitution
xu = 0.11
xl = 0
iterations = 6
expression = x ** 3 - 0.165 * x ** 2 + 0.000399
error_break = False   # should the program stop when error threshold is reached?
error_threshold = 3  # error threshold (program will stop when error is <= this value
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

