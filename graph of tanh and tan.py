import numpy as np
import matplotlib.pyplot as pl
x=np.linspace(-3.14,3.14)
a=np.tan(x)
b=np.tanh(x)
c=np.arctan(x)
d=np.arctanh(x)
pl.plot(x,a,'b',label='tan x')
pl.plot(x,b,'r',label='tanh x')
pl.plot(x,c,'g',label='arctan x')
pl.plot(x,d,'y',label='arctanh x')
pl.legend(loc='upper right')
pl.show()
