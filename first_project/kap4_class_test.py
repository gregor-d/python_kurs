import kap4_class
import numpy as np



data = np.loadtxt("diagnosis.csv", delimiter=",")


X = data[:, 1:6]
## nan einfügen
test = np.random.rand(X.shape[0],X.shape[1])
X[test<0.1] = np.nan
X

Y = data[:, 6]

bayes = kap4_class.bayes(X,Y)
bayes.fit()

xtest = X[bayes.test,:]
ytest = Y[bayes.test]
correct = np.zeros(2)
incorrect = np.zeros(2)

for i in range(xtest.shape[0]):
    klasse = bayes.predict(xtest[i,:])
    if klasse == ytest[i]:
        correct[klasse]+=1
    else:
        incorrect[klasse]+=1
        
print("von %d testfällen wurden %d richtig und %d falsch klassifiziert" % (xtest.shape[0], np.sum(correct), np.sum(incorrect) ))
