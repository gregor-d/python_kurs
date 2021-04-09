import numpy as np

np.random.seed(45)

dataset = np.loadtxt("diagnosis.csv", delimiter=",")

X = dataset[:,1:6]
Y = dataset[:,6]
allData     = np.arange(0,X.shape[0])
iTesting    = np.random.choice(X.shape[0],int(X.shape[0]*0.2),replace=False)
iTraining   = np.delete(allData,iTesting) 
dataRecords = len(iTraining)
XTrain = X[iTraining,:]
YTrain = Y[iTraining]

PXI = np.zeros( (2,XTrain.shape[1],2) )
PI  = np.zeros(2)
for k in range(X.shape[1]):
    PXI[1,k,1] = np.sum(np.logical_and(XTrain[:,k],YTrain))
    PXI[1,k,0] = np.sum(np.logical_and(np.logical_not(XTrain[:,k]),YTrain))  
    PXI[0,k,1] = np.sum(np.logical_and(XTrain[:,k],np.logical_not(YTrain)))
    PXI[0,k,0] = np.sum(np.logical_not(np.logical_or(XTrain[:,k],YTrain)))
PI[1] = np.sum(YTrain)
PI[0] = dataRecords - PI[1]

PXI = (PXI + 1/2) / (dataRecords+1)
PI  = PI  / dataRecords
  
def predictNaiveBayesNominal(x):
    P = np.zeros_like(PI)
    allofthem = np.arange(XTrain.shape[1])
    for i in range(len(PI)):
        P[i] = np.prod(PXI[i,allofthem,x])*PI[i]
    denominator = np.sum(P)
    P = P/denominator
    choosenClass = np.argmax(P)
    return choosenClass

XTest = X[iTesting,:]
YTest = Y[iTesting]
correct   = np.zeros(2)
incorrect = np.zeros(2)

for i in range(XTest.shape[0]):
    klasse = predictNaiveBayesNominal(XTest[i,:].astype(int))
    if klasse == YTest[i]:
        correct[klasse] = correct[klasse] +1
    else:
        incorrect[klasse] = incorrect[klasse] +1
        
print("Von %d Testfaellen wurden %d richtig und %d falsch klassifiziert" % (XTest.shape[0],np.sum(correct),np.sum(incorrect) ))
