import graph

#keep track of the path
#make sure each vertex isnt visited
#set curr variable
#for each vertex
    #if not visited
        #make visited
        #set a very high low distance
        #set current vertex
        #for each vertex
            #as long as vertex isnt current
                #get the edge weight of those 2 vertecies
                #if that distance is new low
                    #set that distance as low and append to path

#pass in graph and node object
def nearestN(graph, starting):
    path = []
    for vertex in graph.vertexList:
        graph.vertexList[vertex].Visited = False
    current = starting
    for vertex in graph.vertexList:
        if graph.vertexList[vertex].Visited == False:
            graph.vertexList[current].Visited = True
            low = 99999
            current = vertex
            for vertex in graph.vertexList:
                if vertex != current:
                    distance = graph.edgeWeights[{current, vertex}]
                    if distance < low:
                        low = distance
                path.append(low)
