# -*- coding: utf-8 -*-
import numpy as np

class kp5_regress():
    
    
    def _create_arr(self, x, y):
        # create array with data
        A = np.ones( (x.shape[0],x.shape[1]+1) )
        A[:,1:x.shape[1]+1] = x
        maxValue = np.max(A,axis=0)
        # normalilze to make easier comparison
        A = A/maxValue
        return A    
        
    def predict(self, xtest, ytest):
        A = self._create_arr(xtest, ytest)
        r = A@self._u - ytest        
        print("predict")
        self._quali(r)
            

    def fit(self, xtrain, ytrain):        
        A = self._create_arr(xtrain, ytrain)
        (u, _, Arank, _) = np.linalg.lstsq(A, ytrain, rcond=None)
        r = A@u - ytrain
        print("fit")
        self._quali(r)
        self._u = u   
        
    
    def _quali(self, r):
        r2 = np.linalg.norm(r)/r.shape[0]
        mean_res = np.mean(np.abs(r))
        max_res = np.max(np.abs(r))        
        print("r %f, meanError %f, maxError %f" % (r2, mean_res, max_res))
        
    def coeff(self):
        return self._u
        

if __name__ == '__main__':
    
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
    
    model = kp5_regress()
    
    model.fit(XTrain, YTrain)
    model.predict(XTest, YTest)
    
    print("mod coeff", model.coeff())