import numpy as np
import scipy.special as ss
from numpy.random import rand
from itertools import product
import matplotlib.pyplot as plt

def hydrogen(n,l,m,r,th,phi):
    na = 0.53*n
    tmp = (2/na)**3
    tmp *= ss.factorial(n-l-1)
    tmp /= 2*n*ss.factorial(n+l)**3
    tmp2 = np.exp(-r/na) * (2*r/na)**l
    laguerre = ss.assoc_laguerre(2*r/na, n-l-1, 2*l+1)
    R_nl = np.sqrt(tmp)*tmp2*laguerre
    return R_nl*ss.sph_harm(m,l,th,phi)

def pts2xyz(pts):
    r, th, phi = zip(*pts)
    x = r*np.sin(phi)*np.cos(th)
    y = r*np.sin(phi)*np.sin(th)
    z = r*np.cos(phi)
    return x,y,z

def getPts(n, l, m, N, rMax, randMax):
    r = rand(N)*rMax
    th = rand(N)*np.pi*2
    phi = rand(N)*np.pi
    pts = []
    for axis in zip(r,th,phi):
        p = hydrogen(n, l, m,*axis)**2
        if p*axis[0]**2 > np.random.rand()*randMax:
            pts.append(axis)
    print(len(pts))
    return pts


n = eval(input("主量子数："))
l = eval(input("角量子数："))
m = eval(input("磁量子数："))

pts = getPts(n, l, m, 200000, 5, 1/200)
x,y,z = pts2xyz(pts)
ax = plt.subplot(projection='3d')
ax.scatter(x, y, z, marker='.')
plt.show()
