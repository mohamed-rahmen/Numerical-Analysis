
#Q6
import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-1*np.pi,2*np.pi,200)
y = np.sin(x)
plt.plot(x,y)
plt.show()

#Q7
x=np.arange(0,5)
f= np.absolute(x-3)**3
g= x*np.sin(x)
plt.plot(x,f,'r')
plt.plot(x,g,'g--')
plt.show()