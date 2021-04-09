import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
fFloat = open("BostonFeature.csv","r")
X = np.loadtxt(fFloat, delimiter=","); fFloat.close()
fFloat = open("BostonTarget.csv","r")
y = np.loadtxt(fFloat, delimiter=","); fFloat.close()

TrainSet = np.random.choice(X.shape[0],int(X.shape[0]*0.80), replace=False)
XTrain = X[TrainSet,:]
YTrain = y[TrainSet]
TestSet = np.delete(np.arange(0, len(y) ), TrainSet)
XTest = X[TestSet,:]
YTest = y[TestSet]
A = np.ones( (XTrain.shape[0],14) )
A[:,1:14] = XTrain
maxValue = np.max(A,axis=0)
A = A/maxValue
(u, _, Arank, _) = np.linalg.lstsq(A, YTrain)
r = A@u - YTrain
print(np.linalg.norm(r)/r.shape[0], np.mean(np.abs(r)), np.max(np.abs(r)))


print(u)