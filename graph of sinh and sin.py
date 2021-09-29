import numpy as np
import matplotlib.pyplot as pl
x=np.linspace(0,6.28)
a=np.sin(x)
b=np.sinh(x)
c=np.arcsin(x)
d=np.arcsinh(x)
pl.plot(x,a,'b',label='sin x')
pl.legend(loc='upper left')
pl.show()
