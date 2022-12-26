import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as cfit

def func(x,m,c):
    return (m*x+c)

data_set = pd.read_csv('data.csv')

x = data_set['x']
y = data_set['y']

opt_param,cov = cfit.curve_fit(func,x,y, p0 = [1.5,0.5])
m,c = opt_param

x_smple = np.linspace(min(x),max(y),100)
y_smple = func(x_smple,m,c)

print("parameter 1: ",m)
print("parameter 2: ",c)

plt.scatter(x,y,color="red")
plt.plot(x_smple,y_smple)
plt.show() 