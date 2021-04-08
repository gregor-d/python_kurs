import numpy as np

np.random.seed(42)

# fin = open("diagnosis.data", "r")
# fout = open("diagnosis.csv", "w")

# for line in fin:
#     line = line.replace(",", ".")
#     line = line.replace("\t", ",")
#     line = line.replace("yes", "1")
#     line = line.replace("no", "0")
#     line = line.replace("\r\n", "\n")
#     fout.write(line)
# fin.close()
# fout.close()

data = np.loadtxt("diagnosis.csv", delimiter=",")

# aufteilen in trainingsmenge 0.8 und test 0.2
X = data[:, 1:6]
Y = data[:, 6]
alldata = np.arange(0, X.shape[0])
test = np.random.choice(X.shape[0], 
                        int(X.shape[0]*0.2),
                        replace=False)
train = np.delete(alldata, test)
records = len(train)
xtrain = X[train,:]
ytrain = Y[train]

# 3d matrix erstellen, anzahl variablen
pix = np.zeros((2, xtrain.shape[1], 2))
pi = np.zeros(2)

# anzahl variablen
for k in range(X.shape[1]):
    # summe an fällen für variable k, wenn k = ja und y = ja
    pix[0, k, 0] = np.sum(np.logical_and(xtrain[:,k], ytrain))
    # summe an fällen für variable k, wenn k = ja und y = nein
    pix[0, k, 1] = np.sum(np.logical_and(np.logical_not(xtrain[:,k]), ytrain))
    # summe an fällen für variable k, wenn k = nein und y ja
    pix[1, k, 0] = np.sum(np.logical_and(xtrain[:,k],np.logical_not(ytrain)))
    pix[1, k, 1] = np.sum(np.logical_not(np.logical_or(xtrain[:,k],ytrain)))
for k in range(X.shape[1]):
    nan_test = np.logical_not(np.isnan(xtrain[:,k]))
    xtrain2 = xtrain[nan_test,k]
    ytrain2 = ytrain[nan_test]
    # summe an fällen für variable k, wenn k = ja und y = ja
    pix[0, k, 0] = np.sum(np.logical_and(xtrain2, ytrain2))
    # summe an fällen für variable k, wenn k = ja und y = nein
    pix[0, k, 1] = np.sum(np.logical_and(np.logical_not(xtrain2), ytrain2))
    # summe an fällen für variable k, wenn k = nein und y ja
    pix[1, k, 0] = np.sum(np.logical_and(xtrain2,np.logical_not(ytrain2)))
    pix[1, k, 1] = np.sum(np.logical_not(np.logical_or(xtrain2,ytrain2)))
# anzahl y/krebs
pi[0] = np.sum(ytrain)
# anzahl kein krebs
pi[1] = records - pi[0]

pix = (pix + 1/2) / (records+1)
pi = pi / records

# ws das eine merkmalskombination zu einer klasse gehört
def pnbn(x):
    p = np.zeros_like(pi)
    # alle merkmale
    allofthem = np.arange(xtrain.shape[1])
    for i in range(len(pi)):
        p[i] = np.prod(pix[i, allofthem, x]) * pi[i]
    den = np.sum(p)
    p = p/den
    choosenclass = np.argmax(p)
    return choosenclass

xtest = X[test,:]
ytest = Y[test]
correct = np.zeros(2)
incorrect = np.zeros(2)

for i in range(xtest.shape[0]):
    klasse = pnbn(xtest[i,:].astype(int))
    if klasse == ytest[i]:
        correct[klasse]+=1
    else:
        incorrect[klasse]+=1
        
print("von %d testfällen wurden %d richtig und %d falsch klassifiziert" % (xtest.shape[0], np.sum(correct), np.sum(incorrect) ))
