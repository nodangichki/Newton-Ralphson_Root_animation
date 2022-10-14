import matplotlib.pyplot as plt
import numpy
from matplotlib.animation import FuncAnimation
from sympy import *

x = Symbol('x')
expression = x**3-7*x**2+14*x -6   # x**3+4*x**2-10
#variables
function = []
time = []
start = 1
stop = 3.2
calculated_xl = []
calculated_xu = []
xms_calculated = []
errors = [0]
itterations = 13
global nearest_root
for t in numpy.arange(-5,5,0.1):
    function.append(expression.subs(x,t))
    time.append(t)

for loops in range(0, itterations):
    xm = (start + stop) / 2
    fxl = expression.subs(x,start)
    fxu = expression.subs(x,stop)
    fxm = expression.subs(x,xm)
    if (fxm * fxl) < 0:
        stop = xm
    elif (fxm * fxl) > 0:
        start = xm

    calculated_xu.append(stop)
    calculated_xl.append(start)
    nearest_root = xm
    xms_calculated.append(nearest_root)
    if loops > 0:
        err = abs(((xm - xms_calculated[loops-1])/xm))*100
        errors.append(err)



plt.plot(time,function,color = "green")
for i in range(itterations):
    print(f'root {i+1} == {xms_calculated[i]} xl = {calculated_xl[i]} xu = {calculated_xu[i]} error= {round(errors[i],2)}%')
    plt.plot(calculated_xl[i],0,'bo')
    plt.plot(calculated_xu[i],0,'r+')
    plt.pause(0.1)

plt.show()
fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15, 5))
axes.set_ylim(0, 15)
axes.set_xlim(-1,1)
plt.style.use("ggplot")
