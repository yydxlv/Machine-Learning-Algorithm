# coding=utf_8
__author__ = 'xilin'
from math import log
import operator
import treePlotter
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    # change to discrete values
    return dataSet, labels
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt=0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    # print(labelCounts)
    return shannonEnt
# ���ո��������������ݼ�
def splitDataSet(dataSet, axis, value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
# ѡ����õ����ݼ����ַ�ʽ
def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntry=calcShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntry=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            print(subDataSet)
            prob=len(subDataSet)/float(len(dataSet))
            newEntry+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntry-newEntry
        if(infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature
# ���س��ִ������ķ�������
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
        sortedClassCount=sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]
#   �������ĺ���
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]  # stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1:  # stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       # copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree)[0]
    print(firstStr)
    secondDict = inputTree[firstStr]
    print(secondDict)
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
if __name__ == "__main__":
    myDat, labels = createDataSet()
    # print(myDat)
    # print(calcShannonEnt(myDat))
    # print(chooseBestFeatureToSplit(myDat))
    # print(createTree(myDat, labels))
    myTree=treePlotter.retrieveTree(0)
    # print(myTree)
    # print(classify(myTree,labels,[1,0]))
    # print(classify(myTree,labels,[1,1]))
    print(classify(myTree,labels,[1,0]))

    # fr=open('lenses.txt')
    # lenses=[inst.strip().split('\t')for inst in fr.readlines()]
    # lenseslabels=["ages","prescript","astigmatic","tearRate"]
    # lensesTree=createTree(lenses,lenseslabels)
    # print(lensesTree)
    # treePlotter.createPlot(lensesTree)