# -*- coding: utf-8 -*-
import numpy as np

fstring = open("iris.data", "r")
ffloat = open("iris.csv", "w")
# recode string to int
for line in fstring:
    line = line.replace("Iris-setosa", "1")
    line = line.replace("Iris-versicolor", "2")
    line = line.replace("Iris-virginica", "3")
    ffloat.write(line)
    
fstring.close()
ffloat.close()

## wenn ein header in der tabelle existiert
#fFloat = open("iris.csv","r")
#header = fFloat.readline().rstrip('\n') # skip the header when loading
#ColumnNames = header.split(',')
dataset = np.loadtxt("iris.csv", delimiter=",")
