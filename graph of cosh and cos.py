import numpy as np
import matplotlib.pyplot as pl
x=np.linspace(0,3.14)
a=np.sin(x)
b=np.cos(x)
c=np.tan(x)
d=np.log(x)
pl.plot(x,a,'b',label='sin x')
pl.plot(x,b,'r',label='cos x')
pl.plot(x,c,'g',label='tan x')
pl.plot(x,d,'y',label='log x')
pl.legend(loc='upper left')
pl.show()
