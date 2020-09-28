import random


class Individual:
    def __init__(self, size_genes):
        self.size_genes = size_genes
        self.fitness = 0
        self.genes = []
        for i in range(self.size_genes):
            self.genes.append(random.randint(0, 1))

    def GetFitness(self):
        if (self.fitness != 0):
            for i in range(self.size_genes):
                if (self.genes[i] == 1):
                    self.fitness = self.fitness + 1
        return self.fitness

    def GetGenes(self, index):
        return self.genes[index]

    def GetGenes(self):
        return self.genes

    def SetGenes(self, index, value):
        self.genes[index] = value
        self.fitness = 0

    def GenerateIndividual(self):
        for i in range(self.size_genes):
            self.genes.append(random.randint(0, 1))
