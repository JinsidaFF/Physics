import matplotlib.pyplot as plt
import numpy as np

A1 = eval(input("输入第一个波的振幅："))
W1 = eval(input("输入第一个波的角频率："))
P1 = eval(input("输入第一个波的初相："))
A2 = eval(input("输入第二个波的振幅："))
W2 = eval(input("输入第二个波的角频率："))
P2 = eval(input("输入第二个波的初相："))

X = max(A1,A2)
fig=plt.figure(figsize=(5,5))
axs=fig.add_subplot(111)
axs.set(xlim=[-X,X],ylim=[-X,X],title='DuanXinJie-LiSaRu')  #title后面是图名记得更改
theta=np.linspace(0,2*np.pi,1000)
x=np.sin(theta)
y=np.sin(theta)
x = A1 * np.sin(W1*theta + P1 * np.pi)
y = A2 * np.sin(W2*theta + P2 * np.pi)
axs.plot(x,y)
plt.show()