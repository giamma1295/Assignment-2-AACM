from random import seed
from random import random
from datetime import datetime
class Graph:
    #constructor
    #it will take the following arguments:
    #1) N -> number of node
    #2) p -> Edge creation probability 
    #3) Directed = False, set if a graph is directed
    def __init__(self,N, p, Directed = False):
        #input Validation
        if not isinstance(N, int):
            raise Exception('N should be an integer value. The passed value of N was: {}'.format(N))

        if not (isinstance(p, (int, float)) and 0<=p<=1):
            raise Exception('p should be an int or a float and must be 0<=p<=1. The passed value of p was: {}'.format(p))
        
        #set random seed generator, we will use the timestamp as seed
        seed(datetime.now())

        #Store if graph is directed or not
        self.__diGraph = Directed

        #store number of Vetrex
        self.__vertrexN = N

        #start Graph creation
        self.__edgesList = []
        

        #execute the right creation method 
        if Directed: 
            self.__mkDiGraph(N,p)
        else:
            self.__mkGraph(N,p)
            pass
        #print(self.__edgesList)
        pass
    #function for DirectedGraph Creation
    def __mkDiGraph(self,N,p):
        #print("Directed")
        for u in range(N):
            for v in range(N):
                if u == v:
                    continue
                if p >= random(): 
                    self.__edgesList.append((u,v))
                    pass
                pass
            pass
        pass
    #function for Simple Graph Creation
    def __mkGraph(self,N,p):
        #print("Not Directed")
        for u in range(N):
            for v in range(u + 1 , N):
                if p >= random(): 
                    self.__edgesList.append((u,v))
                    pass
            pass
        pass

    
    def info(self):
        #"""info.
        #method that print information about Graph
        #"""
        #print(self.__edgesList)
        print("Graph info")
        print("Directed : " + str(self.__diGraph))
        print("Number of vertrex : " + str(self.__vertrexN))
        print("Number of edges : " + str(self.edge_count()))

        pass

    def edge_count(self):
        return len(self.__edgesList)

    #"""
    # method that calculate the degree distribution
    # Returns:
    #   Dict: for simple graph -> Degree Distribution of the graph
    #"""
    def degDistribution(self, out=True):
        d = []
        if self.__diGraph :
            d = self.__degDistDirected(out)
        else:
            d = self.__degDistSimple()
        
        d = list(map(lambda x : float(x)/self.__vertrexN, d))
        #print(d)

        #test purpose
        #x = 0.0
        #for c in d:
        #    x = x + c
        #    pass
        #if abs(1 - x) >  0.1:
        #   raise Exception("Failed Test {}".format(x))

        return d

    def __degDistSimple(self):
        #will contain the degree of every vertreex in graph
        temp = [0]*self.__vertrexN 

        for edge in self.__edgesList:
            temp[edge[0]] = temp[edge[0]] + 1
            temp[edge[1]] = temp[edge[1]] + 1
            pass
        pass
        #print(temp)

        #let's create the list containing the distribution
        #it will be list[k] -> number of vertrex having k degree in the graph
        #so the index will be 0<=k<=N-1(we don't allow loops in our graph)
        dist = [0]*self.__vertrexN
        for t in temp:
            dist[t] = dist[t] + 1
            pass
        #print(dist)

        return dist

    #for directed Graph return:
    # out == True -> outDegree Distribution
    # out == False -> inDegree Distribution
    def __degDistDirected(self, out):
        #will contain the degree of every vertreex in graph
        temp = [0]*self.__vertrexN 
        
        for edge in self.__edgesList:
            if out:
                temp[edge[0]] = temp[edge[0]] + 1
            else:
                temp[edge[1]] = temp[edge[1]] + 1
            pass
        pass
        #print(temp)

        #let's create the list containing the distribution
        #it will be list[k] -> number of vertrex having k degree in the graph
        #so the index will be 0<=k<=N-1(we don't allow loops in our graph)
        dist = [0]*self.__vertrexN
        for t in temp:
            dist[t] = dist[t] + 1
            pass
        
        #print(dist)
        return dist

    pass