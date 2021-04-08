# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
A = np.zeros([22,2])
A[:,0] = np.arange(0, 43, 2)
A[0:11,1] = [2, 6, 9, 12, 14, 16, 17.5, 18.5, 20, 20.5, 21.5]
A[11:22,1] = [22, 22.5, 22.7, 23.5, 23.5, 23.7, 24, 24, 24.2, 24.2, 24.5]
print(A[:])
plt.plot(A[:,0], A[:,1], 'o', label = "Messwerte")
plt.xlabel('Zeit [s]')
plt.ylabel('Spannung [V]')
# plt.show()
# interpolieren mit polynom 2. ordnung
p2 = interpolate.lagrange(A[[0,10,21],0], A[[0,10,21],1])
xnew = np.arange(-2, 50, 2)
ynew = p2(xnew)
error = (( p2(A[:,0]) - A[:,1])**2).sum()
print('P2 => Quadratische Fehler: %.4e; gemittelt %.4e.' % (error, error/22))
plt.plot(xnew, ynew, label="Polynome Ordnung 2", linestyle='-', c='k')

# polynom 5. ordnung
p5 = interpolate.lagrange(A[::4,0], A[::4,1])
xnew = np.arange(-2, 50, 2)
ynew = p5(xnew)
error = (( p5(A[:,0]) - A[:,1])**2).sum()
print('P5 => Quadratische Fehler: %.4e; gemittelt %.4e.' % (error, error/22))
plt.plot(xnew, ynew, label="Polynome Ordnung 5", linestyle='--', c='r')
# legende braucht label aus den plots
plt.legend(loc="lower right")
plt.show()