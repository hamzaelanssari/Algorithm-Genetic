from Individual import *
Length_Of_Genes=20
individuals=[]
individual1=Individual(Length_Of_Genes)
individual1.GenerateIndividual()
individual2=Individual(Length_Of_Genes)
individual2.GenerateIndividual()
individual3=Individual(Length_Of_Genes)
individual3.GenerateIndividual()
individual4=Individual(Length_Of_Genes)
individual4.GenerateIndividual()
individual5=Individual(Length_Of_Genes)
individual5.GenerateIndividual()
individuals.append(individual1)
individuals.append(individual2)
individuals.append(individual3)
individuals.append(individual4)
individuals.append(individual5)
print(individual1.GetGenes())
j=0
for i in individuals:
    print("individual ",j)
    print(i.GetGenes())
    j=j+1