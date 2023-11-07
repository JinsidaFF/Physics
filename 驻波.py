import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
fig=plt.figure()

A = eval(input("振幅："))

axs=fig.add_subplot(111)
axs.set(xlim=[0,10],ylim=[-A,A],title='DXJ-ZB') #title后面是图名记得更改
theta=np.linspace(0,10,1000)
x=theta
y=np.sin(theta)
Liss,=axs.plot(x,y)

def updata(n):
    x=theta
    y=n*np.sin(theta)
    Liss.set_data(x,y)
    return Liss

ani=animation.FuncAnimation(fig,updata,frames=np.linspace(-A,A,20),interval=1)
ani.save('ZB.gif')
plt.show()
