import matplotlib.pyplot as plt
import numpy as np

A1 = eval(input("输入第一个波的振幅："))
W1 = eval(input("输入第一个波的角频率："))
A2 = eval(input("输入第二个波的振幅："))
W2 = eval(input("输入第二个波的角频率："))

X = A1 + A2
fig=plt.figure(figsize=(5,5))
p1=fig.add_subplot(111)
p1.set(xlim=[0,10*X],ylim=[-1.5*X,1.5*X],title='DuanXinJie-p') #title后面是图名记得更改
theta=np.linspace(0,10*X,1000)
x1 = A1 * np.cos(W1*theta)
x2 = A2 * np.cos(W2*theta)
A = np.sqrt(A1 ** 2 + A2 ** 2 + 2*A1*A2)
x3 = A * np.cos(0.5*abs(W2-W1)*theta)
p1.plot(theta,x1 + x2)
p1.plot(theta,x3)
plt.show()
