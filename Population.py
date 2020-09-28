from Individual import *
class Population:
    def __init__(self,popSize,individual_size):
        self.popSize=popSize
        self.individuals=[]
        self.fittestScore=0
        for i in range(popSize):
            self.individuals.append(Individual(individual_size))
    def SelectFittest(self):
        Maxfit=0
        indexMaxfit=0
        for i in range(self.popSize):
            if(Maxfit<self.individuals[i].GetFitness()):
                Maxfit=self.individuals[i].GetFitness()
                indexMaxfit=i
        self.fittestScore=self.individuals[indexMaxfit]
        return Maxfit
    def GetFittesScore(self):
        return self.fittestScore
    def SelectSecondFittest(self):


