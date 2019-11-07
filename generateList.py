import csv

class generateList:
    
    def __init__(self):
        self.dataSet = []
    
    def readArchive(self, archName):
        with open(archName, newline='') as file:
            spamReader = csv.reader(file, delimiter = ',')
            for line in spamReader:
                self.dataSet.append(line)
    
    def readLine(self, lineNumber):
        return self.dataSet[lineNumber]
            
