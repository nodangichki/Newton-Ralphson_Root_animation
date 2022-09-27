'''
This Script Calculates the root of a function using Secant method and provides a graphical representation
of what was happening during the calculation

Users Inputs:
you are to only alter these values
-> guess = your initial guess of the root (can be anything)
-> guess_xi_min1 = your initial guess 2 for secant line
-> iterations = no of calculation you want (more = more accurate = more computation time, and wiseVersa)
-> expression = your function(function to be written with x not substituting value of x with integer type
->xmin = where to start function from in x-axis
->xmax = where to start function from y-axis
->fine = smoothness of the function
->ymin,ymax = limit of y-axis on the graph
->speed_of_animation = how fast new plot appears in seconds

additional modifiactions:

>>plt.style.use(something) to change the style of plot

Created by Nodan Gichki
'''

from sympy import *
import numpy
import matplotlib.pyplot as plt

x = Symbol('x')
# user defined variables
guess = 0.05
guess_xi_min1 = 0.02
iterations = 2
expression = x ** 3 - 0.165 * x ** 2 + 0.000399  # x**2# #sin(x)
xmin = -10
xmax = 10
ymin = -2
ymax = 2
fine = 0.01
speed_of_animation = 5
# script variables
new_guess = 0
previous_value = []
x_values_per_itter = []
y_values_per_itter = []
length = int((xmax - xmin) / fine)

for loops in range(0, iterations):

    # values of ploting the chart
    t = []  # range same as len of expression with substitution
    for i in numpy.arange(xmin, xmax, fine):
        t.append(i)
    function = [expression.subs(x, t[i]) for i in range(0, length)]  # substituting range of values
    #    derr = diff(expression,x)                                      #derivative of expression
    #   subs = [derr.subs(x,t[i]) for i in numpy.arange(0,length)]       #substituting range of values in derivative
    ## calculating next value of tanline
    f_of_x = expression.subs(x, guess)
    f_of_xmin1 = expression.subs(x, guess_xi_min1)
    tempval3 = guess - ((f_of_x * (guess - guess_xi_min1)) / (f_of_x - f_of_xmin1))
    new_guess = round(tempval3, 5)

    x1 = guess
    y1 = expression.subs(x, guess)
    x2 = guess_xi_min1
    y2 = expression.subs(x, guess_xi_min1)

    x_of_1 = [x1, x2]
    y_of_1 = [y1, y2]

    x_values_per_itter.append(x_of_1)
    y_values_per_itter.append(y_of_1)

    guess_xi_min1 = guess
    guess = new_guess
    previous_value.append(guess)

    #    derivative_of_derivatives.append(subs)
    # tanlines_of_tanline.append(tanline)
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
axes.set_ylim(ymin, ymax)
axes.set_xlim(xmin=xmin, xmax=xmax)

for i in range(iterations):
    print(f'Itteration NO.{i + 1} and root guessed is {previous_value[i]}')
    axes.plot(t, function, color="blue")
    axes.plot(x_values_per_itter[i], y_values_per_itter[i], marker='o', color='red')
    plt.pause(5)

plt.show()
