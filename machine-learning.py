import numpy
import matplotlib.pyplot as plt
from scipy import stats

x = numpy.random.uniform(1.0,5.0,10)
y = numpy.random.uniform(1.0,5.0,10)

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myFunc(x):
    return slope * x + intercept

myModel = list(map(myFunc,x))


plt.scatter(x,y)
plt.plot(x,myModel)
plt.show()