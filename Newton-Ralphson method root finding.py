'''
This Script Calculates the root of a function using Newton-Raphson method and provides a graphical representation
of what was happening during the calculation

Users Inputs:
you are to only alter these values
-> guess = your initial guess of the root (can be anything)
-> itterations = no of calculation you want (more = more accurate = more computation time, and wiseVersa)
-> expression = your function(function to be written with x not substituting value of x with integer type

additional modifiactions:
>>for i in range(-100,100) change these for changing the time. but you will have to adjust all for loops for correct dimentions
>>axis.set_xlim(something),axis.set_ylim(something). for changing the axes of the graph
>>plt.style.use(something) to change the style of plot
>>uncomment the 2nd line of animate(i) to see the derivative of the function

Created by Nodan Gichki
'''


from sympy import *
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
guess = 3
new_guess = 0
itterations = 5
previous_value = []
function_of_functions = []
derivative_of_derivatives = []
tanlines_of_tanline = []
time_of_times = []
x = Symbol('x')
expression = x**2#x ** 3 - 0.165 * x ** 2 + 0.000399

for loops in range(0,itterations):

    ##values of ploting the chart
    t = []                                                        #range same as len of expression with substitution
    for i in range(-100,100):
        t.append(i)
    function = [expression.subs(x,t[i]) for i in range(0,200)]     #substituting range of values
    derr = diff(expression,x)                                      #derivative of expression
    subs = [derr.subs(x,t[i]) for i in numpy.arange(0,200)]       #substituting range of values in derivative
## calculating next value of tanline
    tempval1 = expression.subs(x, guess)
    tempval2 = derr.subs(x, guess)
    tempval3 = guess - (tempval1 / tempval2)
    new_guess = tempval3
    tanx1 = guess
    tany1 = expression.subs(x,guess)
    tanm = derr.subs(x,guess)
    y = tanm*x-tanm*tanx1+tany1

    tanline = [y.subs(x,t[i]) for i in numpy.arange(0,200)]
    guess = new_guess
    previous_value.append(guess)

    function_of_functions.append(function)
    derivative_of_derivatives.append(subs)
    time_of_times.append(t)
    tanlines_of_tanline.append(tanline)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(15, 5))
axes.set_ylim(-500, 500)
axes.set_xlim(-50,50)
plt.style.use("ggplot")


def animate(i):
    plot1 = axes.plot(time_of_times[i], function_of_functions[i], color="blue")
    #axes.plot(time_of_times[i], derivative_of_derivatives[i], color="red")
    plot2 = axes.plot(time_of_times[i], tanlines_of_tanline[i], color="green")

    print(i)

anim = FuncAnimation(fig,animate,interval=200)
plt.show()

print(previous_value)