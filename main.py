from Graph import Graph

#test parameter
#Node in Graph
N = 10

#probability
p = 0.31

#Number of Experiment
exp = 10

#Directed
D = False
desc = ""

if D:
    desc = "Directed"
else:
    desc = "Simple"

#for Directed Graphs, choose between inDegree Distribution and outDegree Distribution
out = True # True -> outDegree Distribution, False -> inDegree Distribution
descOut = "degree"

if out and D:
    descOut = "out Degree"
elif not out and D:
    descOut = "in Degree"

#Print Info about the esperiment
print("We will create {} {} graphs using the Erdos-Renyi Model".format(exp,desc))
print("Using the Following parameter : N -> {}, p -> {}".format(N,p))
print("and for each one we will calculate the {} distribution".format(descOut))

#here we will store a graph's list 
gList = []

#create 10 graphs
for i in range(10):
    gList.append(Graph(N, p, D))

#print info for every graph in list
for i in range(len(gList)):
    print("\n--------------------------")
    print("Graph {} infos ".format(i + 1))
    gList[i].info()
    print("--------------------------\n")
    pass

#get for every graph the degree distribution

degDistPerc = list(map(lambda x : x.degDistribution(out), gList))
#degDistPerc = list(map(lambda e : list(map(lambda x : x/N ,e)),degDist))

print("\n---------------------------------")
print("\n------Degree Distributions-------")
print("\n---------------------------------")
#print('\n\n'.join(map(str, degDist)))
print('\n\n'.join(map(str, degDistPerc)))  
print("---------------------------------\n")

#calculte the experiments Avg degree Distribution 
#sumDegDist = [sum(x) for x in zip(*degDist)]
#avgDegDist = list(map( lambda x : x/ (N*exp),sumDegDist))
sumdegDistPerc = [sum(x) for x in zip(*degDistPerc)]
avgDegDistPerc = list(map( lambda x : x/ exp,sumdegDistPerc))
#summ = float(map( lambda x : sum(x)  ,avgDegDist))
#print(avgDegDist)
#print(sum(avgDegDist))
#print("\n\n\n")
print("The average degree distribution for the experiment is :\n ")
print(avgDegDistPerc)
#print(sum(avgDegDistPerc))