from sympy import *
import numpy
import matplotlib.pyplot as plt

wc = 100
wm = 10
xmin = -2
xmax = 2
fine = 0.001
carier = []
messege = []
modulated = []
time = []
demodulation = []

for t in numpy.arange(xmin,xmax,fine):
    carier.append(cos(wc*t))
    messege.append(cos(wm*t))
    modulated.append(cos(wc*t)*cos(wm*t))
    time.append(t)
    demodulation.append((0.5*cos(wm*t))+(0.5*cos(wm*t)*cos(2*wc*t)))

plt.subplot(4,1,1)
plt.plot(time,messege,color='green')
plt.subplot(4,1,2)
plt.plot(time,carier,color = 'orange')
plt.subplot(4,1,3)
plt.plot(time,modulated,color='red')
plt.subplot(4,1,4)
plt.plot(time,demodulation,color='blue')

plt.show()
