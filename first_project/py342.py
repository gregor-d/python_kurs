# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
A = np.zeros([101,2])
A[:,0] = np.arange(0, 1.01, 0.01)
A[:,1] = np.sin(4*np.pi*A[:,0])**2
print(A[:])
plt.plot(A[:,0], A[:,1], '-', label = "sin")
# interpolieren mit polynom 10. ordnung

p10 = interpolate.lagrange(A[::10,0], A[::10,1])
print(p10)
xnew = np.arange(0, 1, 0.01)
ynew = p10(xnew)
error = (( p10(A[:,0]) - A[:,1])**2).sum()
print('P10 => Quadratische Fehler: %.4e; gemittelt %.4e.' % (error, error/22))
plt.plot(xnew, ynew, label="P10", linestyle='--', c='k')
plt.plot(np.arange(0,1.1,0.1), A[::10,1], 'o', c='k')

# legende braucht label aus den plots
plt.legend(loc="lower right")
plt.show()# -*- coding: utf-8 -*-

