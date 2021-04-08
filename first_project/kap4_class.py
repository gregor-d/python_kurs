import numpy as np

class bayes():
    
    def __init__(self, predictors, target):
        
        # create training and test data
        alldata = np.arange(0, predictors.shape[0])
        self.test = np.random.choice(predictors.shape[0], 
                                int(predictors.shape[0]*0.2),
                                replace=False)
        train = np.delete(alldata, self.test)
        self.records = len(train)
        self.xtrain = predictors[train,:]
        self.ytrain = target[train]
        
    def fit(self):
            pix = np.zeros((2, self.xtrain.shape[1], 2))
            pi = np.zeros(2)

            # anzahl variablen
            for k in range(self.xtrain.shape[1]):
                xtrain = self.xtrain[:,k]
                ytrain = self.ytrain
                # summe an fällen für variable k, wenn k = ja und y = ja
                pix[0, k, 0] = np.sum(np.logical_and(xtrain, ytrain))
                # summe an fällen für variable k, wenn k = ja und y = nein
                pix[0, k, 1] = np.sum(np.logical_and(np.logical_not(xtrain), ytrain))
                # summe an fällen für variable k, wenn k = nein und y ja
                pix[1, k, 0] = np.sum(np.logical_and(xtrain,np.logical_not(ytrain)))
                pix[1, k, 1] = np.sum(np.logical_not(np.logical_or(xtrain,ytrain)))
            # anzahl y/krebs
            pi[0] = np.sum(ytrain)
            # anzahl kein krebs
            pi[1] = self.records - pi[0]

            self.pix = (pix + 1/2) / (self.records+1)
            self.pi = pi / self.records

    # ws das eine merkmalskombination zu einer klasse gehört
    def predict(self, predictors):
        p = np.zeros_like(self.pi)
        # alle merkmale
        allofthem = np.arange(self.xtrain.shape[1])
        for i in range(len(self.pi)):
            nan_test = np.logical_not(np.isnan(predictors))
            predictors = predictors[nan_test].astype(int)
            allofthem = allofthem[nan_test] 
            p[i] = np.prod(self.pix[i, allofthem, predictors]) * self.pi[i]
        den = np.sum(p)
        p = p/den
        choosenclass = np.argmax(p)
        return choosenclass

    def testindex(self):
        return self.test

# for k in range(self.xtrain.shape[1]):
#                 # wenn merkmal nicht existiert entfernen aus vektor
#                 nan_test = np.logical_not(np.isnan(self.xtrain[:,k]))
#                 xtrain = self.xtrain[nan_test,k]
#                 ytrain = self.ytrain[nan_test]                                
#                 # summe an fällen für variable k, wenn k = ja und y = ja
#                 pix[0, k, 0] = np.sum(np.logical_and(xtrain, ytrain))
#                 # summe an fällen für variable k, wenn k = ja und y = nein
#                 pix[0, k, 1] = np.sum(np.logical_and(np.logical_not(xtrain), ytrain))
#                 # summe an fällen für variable k, wenn k = nein und y ja
#                 pix[1, k, 0] = np.sum(np.logical_and(xtrain,np.logical_not(ytrain)))
#                 pix[1, k, 1] = np.sum(np.logical_not(np.logical_or(xtrain,ytrain)))