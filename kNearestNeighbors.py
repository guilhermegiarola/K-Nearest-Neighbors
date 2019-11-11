from generateList import generateList
import matplotlib.pyplot as plt
import math
import itertools
import os 
import time

class kNearestNeighbors:
    handInput = []
    orderedList = {}
    comparedNeighbors = []
    kNeighbors = []
    accuracyList = []

    def __init__(self, fileName):
        auxList = generateList()
        auxList.readArchive(fileName)
        
        aux = 3
        while(aux < 75):
            self.kNeighbors.append(aux)
            aux = aux + 2

    def getDistance(self, firstHand, secondHand):
        summation = 0
        for i in range(0,len(firstHand)-1):
            value1 = float(firstHand[i])
            value2 = float(secondHand[i])
            summation = float(summation) + float(value1 - value2)**2
        return math.sqrt(summation)
    
    def executeKNN(self, entry, num):
        auxList = generateList()
        auxList.readArchive('iris.csv')
        auxValue = []
        auxDistance = 9999999
        distance = 0

        for i in range(1,len(auxList.dataSet)-1):
            distance = self.getDistance(entry, auxList.readLine(i))
            #Cria um dicionário o qual é indexado pelas distâncias.
            self.orderedList[distance] = auxList.readLine(i)
        
        auxIterator = 0

        for distance, value in sorted(self.orderedList.items()):
            if(auxIterator < int(num)):
                self.comparedNeighbors.append(value[4])
                auxIterator += 1

        auxIterator = 0
        value = self.mostFrequent(self.comparedNeighbors)
        self.comparedNeighbors = []
        self.orderedList = {}
        return value
    
    def mostFrequent(self, List):
        IS = 0
        IVe = 0
        IVi = 0

        for i in List:
            if(i == 'Iris-setosa'):
                IS = IS + 1
            elif(i == 'Iris-versicolor'):
                IVe = IVe + 1
            elif(i == 'Iris-virginica'):
                IVi = IVi + 1
        
        if(IS > IVi and IS > IVe):
            return 'Iris-setosa'
        elif(IVe > IS and IVe > IVi):
            return 'Iris-versicolor'
        else:
            return 'Iris-virginica'


    def confusionMatrix(self):
        confusionMatrix = []
        for element in range(0,3):
            confusionMatrix.append([])
        
        for i in range(0,3):
            for j in range(0,3):
                confusionMatrix[i].append(0)

        auxList = generateList()
        auxList.readArchive('test.csv')

        for j in self.kNeighbors:
            for i in range(0, 75):
                entry = auxList.readLine(i)
                result = self.executeKNN(auxList.readLine(i), j)

                if(entry[4] == 'Iris-setosa' and result == 'Iris-setosa'):
                    confusionMatrix[0][0] += 1
                elif(entry[4] == 'Iris-setosa' and result == 'Iris-versicolor'):
                    confusionMatrix[0][1] += 1
                elif(entry[4] == 'Iris-setosa' and result == 'Iris-virginica'):
                    confusionMatrix[0][2] += 1
                if(entry[4] == 'Iris-versicolor' and result == 'Iris-setosa'):
                    confusionMatrix[1][0] += 1
                elif(entry[4] == 'Iris-versicolor' and result == 'Iris-versicolor'):
                    confusionMatrix[1][1] += 1
                elif(entry[4] == 'Iris-versicolor' and result == 'Iris-virginica'):
                    confusionMatrix[1][2] += 1
                elif(entry[4] == 'Iris-virginica' and result == 'Iris-setosa'):
                    confusionMatrix[2][0] += 1
                elif(entry[4] == 'Iris-virginica' and result == 'Iris-versicolor'):
                    confusionMatrix[2][1] += 1
                elif(entry[4] == 'Iris-virginica' and result == 'Iris-virginica'):
                    confusionMatrix[2][2] += 1
        
                accuracy = 0
                for i in range(0, len(confusionMatrix[0])):
                    accuracy = accuracy + confusionMatrix[i][i]
                
            for i in range(0,3):
                for j in range(0,3):
                    confusionMatrix[i][j] = 0

            accuracy = accuracy*100/75
            self.accuracyList.append(accuracy)
            accuracy = 0
    
    def plotarGrafico(self):
        fig = plt.figure()

        ax1 = fig.add_subplot(111)
        ax1.set_title("Accuracy x Quantity of Neighbors(k)")
        ax1.set_ylabel('Accuracy')
        ax1.set_xlabel('Quantity of Neighbors')

        plt.plot(self.kNeighbors, self.accuracyList)
        plt.show()
#---------------------------------Main Code-----------------------------------------#        
classList = generateList()
classList.readArchive('iris.csv')

execution = kNearestNeighbors('iris.csv')

execution.confusionMatrix()
execution.plotarGrafico()