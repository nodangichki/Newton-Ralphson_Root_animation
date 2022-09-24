'''
This Script Calculates the root of a function using Newton-Raphson method and provides a graphical representation
of what was happening during the calculation

Users Inputs:
you are to only alter these values
-> guess = your initial guess of the root (can be anything)
-> itterations = no of calculation you want (more = more accurate = more computation time, and wiseVersa)
-> expression = your function(function to be written with x not substituting value of x with integer type
->xmin = where to start function from in x axis
->xmax = where to start function from y axis
->fine = smoothness of the function
->ymin,ymax = limit of y axis on the graph
->speed_of_animation = how fast new plot appears in seconds

additional modifiactions:

>>plt.style.use(something) to change the style of plot
>>uncomment the 2nd line of animate(i) to see the derivative of the function

Created by Nodan Gichki
'''


from sympy import *
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
x = Symbol('x')
#user defined variables
guess = 0.5
itterations = 5
expression = x ** 3 - 0.165 * x ** 2 + 0.000399#sin(x) #x**2
xmin = -10
xmax = 10
ymin = -2
ymax = 2
fine = 0.01
speed_of_animation = 5
#script variables
new_guess = 0
previous_value = []
function_of_functions = []
derivative_of_derivatives = []
tanlines_of_tanline = []
time_of_times = []
length = int((xmax-xmin)/fine)

for loops in range(0,itterations):

    ##values of ploting the chart
    t = []                                                        #range same as len of expression with substitution
    for i in numpy.arange(xmin,xmax,fine):
        t.append(i)
    function = [expression.subs(x,t[i]) for i in range(0,length)]     #substituting range of values
    derr = diff(expression,x)                                      #derivative of expression
    subs = [derr.subs(x,t[i]) for i in numpy.arange(0,length)]       #substituting range of values in derivative
## calculating next value of tanline
    tempval1 = expression.subs(x, guess)
    tempval2 = derr.subs(x, guess)
    tempval3 = guess - (tempval1 / tempval2)
    new_guess = tempval3
    tanx1 = guess
    tany1 = expression.subs(x,guess)
    tanm = derr.subs(x,guess)
    y = tanm*x-tanm*tanx1+tany1

    tanline = [y.subs(x,t[i]) for i in numpy.arange(0,length)]
    guess = new_guess
    previous_value.append(guess)

    function_of_functions.append(function)
    derivative_of_derivatives.append(subs)
    time_of_times.append(t)
    tanlines_of_tanline.append(tanline)
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
axes.set_ylim(ymin, ymax)
axes.set_xlim(xmin=xmin, xmax=xmax)
axes.autoscale(enable=None,tight=True,axis=y)

#plt.style.use("ggplot")

for i in range(itterations):
    print(f'Itteration NO.{i+1} and root guessed is {previous_value[i]}')
    axes.plot(time_of_times[i],tanlines_of_tanline[i],color="white")
    #axes.plot(time_of_times[i], derivative_of_derivatives[i], color="red")
    axes.plot(t, function, color="blue")
    axes.plot(time_of_times[i], tanlines_of_tanline[i], color="green")
    plt.pause(5)



plt.show()


