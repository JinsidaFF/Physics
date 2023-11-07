import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation
fig=plt.figure()

A = eval(input("振幅："))
W = eval(input("角频率："))
axs=fig.add_subplot(111)
axs.set(xlim=[0,10],ylim=[-A,A],title='DXJ-XB') #title后面是图名记得更改
theta=np.linspace(0,10,1000)
x=theta
y=A*np.sin(W*theta)
Liss,=axs.plot(x,y)


def updata(n):
    x=theta
    y=A*np.sin(W*theta+n*np.pi)
    Liss.set_data(x,y)
    return Liss

ani=animation.FuncAnimation(fig,updata,frames=np.linspace(0,3,200),interval=10)
ani.save('XB.gif')
plt.show()
