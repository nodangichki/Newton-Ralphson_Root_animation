"""
This Script Calculates the root of a function using Newton-Raphson method and provides a graphical representation
of what was happening during the calculation

Users Inputs:
you are to only alter these values
-> guess = your initial guess of the root (can be anything)
-> iterations = no of calculation you want (more = more accurate = more computation time, and wiseVersa)
-> expression = your function(function to be written with x not substituting value of x with integer type
->xmin = where to start function from in x-axis
->xmax = where to start function from y-axis
->fine = smoothness of the function
->ymin,ymax = limit of y-axis on the graph
->speed_of_animation = how fast new plot appears in seconds

additional modifications:

>>plt.style.use(something) to change the style of plot
>>uncomment the 2nd line of animate(i) to see the derivative of the function

Created by Nodan Gichki
"""


from sympy import *
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

x = Symbol('x')
# user defined variables
guess = 0.5
iterations = 10
expression = x ** 3 - 0.165 * x ** 2 + 0.000399  # sin(x) #x**2
xmin = -10
xmax = 10
ymin = -2
ymax = 2
fine = 0.01
speed_of_animation = 2
# script variables
new_guess = 0
previous_value = []
error_list = []
tanlines_of_tanline = []
time_of_times = []
length = int((xmax-xmin)/fine)

colors=sns.color_palette("rocket", iterations)
t = []                                                           # range same as len of expression with substitution
for i in numpy.arange(xmin,xmax,fine):
    t.append(i)
function = [expression.subs(x,t[i]) for i in range(0,length)]    # substituting range of values
derr = diff(expression,x)                                        # derivative of expression
subs = [derr.subs(x,t[i]) for i in numpy.arange(0,length)]       # substituting range of values in derivative
for loops in range(0, iterations):                               # this for loop is for the iterations
    # calculating next value of tan line
    tempval1 = expression.subs(x, guess)
    tempval2 = derr.subs(x, guess)
    tempval3 = guess - (tempval1 / tempval2)
    new_guess = tempval3
    tanx1 = guess
    tany1 = expression.subs(x,guess)
    tanm = derr.subs(x,guess)
    y = tanm*x-tanm*tanx1+tany1

    tanline = [y.subs(x,t[i]) for i in numpy.arange(0,length)]
    error = abs( ((new_guess - guess)/(new_guess))*100)
    error_list.append(error)
    guess = new_guess
    previous_value.append(guess)

    #function_of_functions.append(function)
    time_of_times.append(t)
    tanlines_of_tanline.append(tanline)
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
axes.set_ylim(ymin, ymax)
axes.set_xlim(xmin=xmin, xmax=xmax)
axes.autoscale(enable=None,tight=True,axis=y)

#plt.style.use("ggplot")

for i in range(iterations):
    print(f'Itteration NO.{i + 1} and root guessed is {previous_value[i]} error is {error_list[i]}%')
    plt.minorticks_on()
    plt.tick_params(direction='in', right=True, top=True)
    plt.tick_params(labelsize=14)
    plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)
    yticks = numpy.arange(ymin, ymax + 1, 1)
    plt.tick_params(direction='in', which='minor', length=5, bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='major', length=10, bottom=True, top=True, left=True, right=True)
    plt.yticks(yticks)

    axes.plot(time_of_times[i],tanlines_of_tanline[i],label=f'Root: {round(previous_value[i],4)} Err= {round(error_list[i],1)}%',  color=colors[i])
    plt.legend()
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Y-Values', fontsize=14)
    #axes.plot(time_of_times[i], derivative_of_derivatives[i], color="red")
    axes.plot(t, function, color="blue")
    plt.pause(speed_of_animation)

plt.show()


