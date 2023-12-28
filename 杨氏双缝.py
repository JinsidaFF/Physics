import numpy as np
import matplotlib.pyplot as plt

def interSlit(dSlit, point=(1,1,1), dWave=1.06e-6):
    pVar = sum(np.array(point)**2) + 0.25*dSlit**2
    delt = 2*np.pi/dWave*(
        np.sqrt(pVar+point[0]*dSlit)-
        np.sqrt(pVar-point[0]*dSlit))
    return delt

def interYang(dSlit, dScreen, dWave):
    xAxis = np.arange(-200,201)*1e-5
    I = [waveAdd(1,1,interSlit(
            dSlit,(x,0,dScreen),dWave)) 
            for x in xAxis]
    plt.imshow(np.array([I]*100), cmap='gray', aspect='auto', extent=[xAxis.min(), xAxis.max(), 0, 1])
    plt.show()
waveAdd = lambda I1,I2,theta : I1+I2+2*np.sqrt(I1*I2)*np.cos(theta)

dSlit = eval(input("小孔间距(毫米)：")) * 1e-3
dScreen = eval(input("屏距(米)："))
dWave = eval(input("光的波长(nm)：")) * 1e-9

interYang(dSlit, dScreen, dWave)
