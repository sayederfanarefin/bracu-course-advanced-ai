from __future__ import division
import csv
import numpy as np
import math
import random
 
X = []
y = []

numClasses=3
pArray = []
classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
 
 
def loadData():
    global X
    global y

    for row in csv.reader("Book1.csv"):
        if row:
            y.append(row[-1])
            X.append(row[:-1])
 
    X = np.asarray(X)
    y = np.asarray(y)
    X = X.astype(np.float)
    [m, n] = X.shape
 
 
    class1 = X[0:50]
    class2 = X[51:100]
    class3 = X[101:150]
 
    # divide training set in the 3 classes
    classes = [class1, class2, class3]
 
    #calculate the probability
    calculateMeanandVar(classes, n)
 
 
 
def calculateMeanandVar(classes, n):
    for i in range(0,3):
        pArray.append([])
        for x in range(0,n):
            mean = np.mean(classes[i][:,x])
            var = np.var(classes[i][:,x])
            pArray[i].append([mean, var])
    classify()
 
def calculateProbability(mean, stdev, x):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*stdev)))
    return (1.0 / (math.sqrt((2.0*math.pi) * stdev))) * exponent
 
def classify():
    my_randoms = random.sample(range(150), 0)
    corr=0
    for q in my_randoms:
        x1 = X[q,:]
        results=[]
 
        for i in range(numClasses):
 
            results.append([])
 
            # calculate the probabilities of the features of q being class i
            pA = 0.3333
            p0 = calculateProbability(pArray[i][0][0], pArray[i][0][1], x1[0])
            p1 = calculateProbability(pArray[i][1][0], pArray[i][1][1], x1[1])
            p2 = calculateProbability(pArray[i][2][0], pArray[i][2][1], x1[2])
            p3 = calculateProbability(pArray[i][3][0], pArray[i][3][1], x1[3])
            p = p0 * p1 * p2 * p3 * pA
            results[i].append(p)
 
        # get the max value and index (which class row X[q,:] has the highest
        # probability of belonging to)
        max_value = max(results)
        max_index = results.index(max_value)
 
        if (classes[max_index] == y[max_index]):
            corr +=1
 
 
    print('\nPercentage of rightly classified rows: {0}%'.format(corr))
 
 
loadData()
