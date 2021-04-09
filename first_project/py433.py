# -*- coding: utf-8 -*-
import numpy as np

dataset = np.loadtxt("diagnosis.csv", delimiter=",")

X = dataset[:,1:6]
Y = dataset[:,6]
allData     = np.arange(0,X.shape[0])
iTesting    = np.random.choice(X.shape[0],int(X.shape[0]*0.2),replace=False)
iTraining   = np.delete(allData,iTesting) 
dataRecords = len(iTraining)
XTrain = X[iTraining,:]
YTrain = Y[iTraining]


XTest = X[iTesting,:]
YTest = Y[iTesting]


T = dataset[:,0]
trueIndex = np.flatnonzero(YTrain==1)
falseIndex = np.flatnonzero(YTrain==0)
muApproxTrue = np.sum(T[trueIndex])/trueIndex.shape[0]
sgApproxTrue = np.sqrt(np.sum( (T[trueIndex]-muApproxTrue)**2 ) / (trueIndex.shape[0] -1))
muApproxFalse = np.sum(T[falseIndex])/falseIndex.shape[0]
sgApproxFalse = np.sqrt(np.sum( (T[falseIndex]-muApproxFalse)**2 ) / (falseIndex.shape[0] -1))

def Gausverteilung(x,mu,sigma):
    y = np.exp(-0.5*( (x-mu)/sigma)**2 )/(sigma*np.sqrt(2*np.pi))
    return(y)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(131)
ax.hist(T[:],15,density=1, facecolor='k', alpha=0.5)
ax.set_xlabel('Temperatur'); 
ax.set_ylabel('Wahrscheinlichkeit')
Tplot = np.arange(33,44,0.05)
ax.plot(Tplot,Gausverteilung(Tplot,muApproxTrue,sgApproxTrue),'k:')
ax.plot(Tplot,Gausverteilung(Tplot,muApproxFalse,sgApproxFalse),'k-.')
ax.set_ylim([0,0.8])
ax.set_title('Alle Trainingsdaten')

ax = fig.add_subplot(132)
ax.hist(T[falseIndex],15,density=1, facecolor='k', alpha=0.5)
ax.set_xlabel('Temperatur')
ax.plot(Tplot,Gausverteilung(Tplot,muApproxFalse,sgApproxFalse),'k-.')
ax.set_ylim([0,0.8])
ax.set_title('Negative Diagnose')
ax = fig.add_subplot(133)
ax.hist(T[trueIndex],15,density=1, facecolor='k', alpha=0.5)
ax.set_xlabel('Temperatur')
ax.plot(Tplot,Gausverteilung(Tplot,muApproxTrue,sgApproxTrue),'k:')
ax.set_ylim([0,0.8])
ax.set_title('Positive Diagnose')
plt.tight_layout()
plt.show(block=False)
