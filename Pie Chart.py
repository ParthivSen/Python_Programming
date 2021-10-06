import matplotlib.pyplot as pl
p=[95,93,95,95,85]
expl=[0.2,0.2,0.2,0.2,0.2]
l=['Physics','Chemistry','Math','CS','English']
pl.axis('equal')
pl.pie(p,labels=l,autopct="%1.2f%%",explode=expl)
pl.show()
