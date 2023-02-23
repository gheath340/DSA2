#GARRETT HEATH 010229298
import algorithm as algo
import hashTable as hash
import package as p
import graph
import csv
import os.path
import truck

#formatting time   result = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))
PACKAGES = hash.ChainingHashTable(40)
DISTANCEDICT = {}
ADDRESSLIST = []

truck1 = truck.Truck()
#package ids for each truck
truck1L = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2L = [3, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 23, 24, 25, 36, 38]
truck3L = [9, 26, 27, 28, 32, 33, 35, 39]
#create graph for each truck
t1Graph = graph.Graph()
t2Graph = graph.Graph()
t3Graph = graph.Graph()
#truck speed mph
truckSpeed = 18
#time for each truck
t1Time = 8.0
t2Time = 9.08333333333
t3Time = 0.0

truck1 = truck.Truck(truck1L, t1Graph, t1Time)
truck2 = truck.Truck(truck2L, t2Graph, t2Time)
truck3 = truck.Truck(truck3L, t3Graph, t3Time)

#LEFT OFF ABOUT TO MAKE EVERYTHING WITH TRUCK OBJECTS
def main():
    #TO DO: KEEP TRACK OF TIME AND UPDATE DELIVERY STATUS
    #PACKAGE WITH WRONG ADDRESS
    loadPackageData("/Users/garrettheath/Desktop/projects/DSA2/packageFile.csv")
    loadDistanceData("/Users/garrettheath/Desktop/projects/DSA2/goodDistanceTable.csv")
    generateVertecies()
    startVertexEdgesCreate()
    generateEdges()
    totalDistance = 0
    t1Path, t1Distances = getPath(t1Graph, t1Graph.vertexList[0])
    t2Path, t2Distances = getPath(t2Graph, t2Graph.vertexList[0])
    t3Path, t3Distances = getPath(t3Graph, t3Graph.vertexList[0])
    for distance in t1Distances:
        totalDistance += float(distance)
    for distance in t2Distances:
        totalDistance += float(distance)
    for distance in t3Distances:
        totalDistance += float(distance)

    print(totalDistance)

def deliverPackage(truck, graph, id, truckTime, distance):
    package = PACKAGES.search(id)
    deliveryTime = distance / truckSpeed
    truckTime

def deliverPackages(truck, graph):
    distance = 0
    #get path and distances for truck
    #loop through both lists
    #for each item take the packageID(vertex label) adjust the delivery status to delivered(w/time)
        #calculate the time that drive took based on miles and 18 mph speed
        #add time to trucks time
        #add distance to trucks distance
    truckPath, truckDistance = getPath(graph, graph.vertexList[0])
    for stop in truckPath:
        time = 0.0
        package = PACKAGES.search(stop)
        package.setStatus("Delivered at " + time)
    return distance

#trucks graph and start vertex object
def getPath(graph, start):
    path = []
    #will need distances to add up total distance
    distances = []
    path.append(start)
    current = start
    start.Visited = True
    distance, vertex = shortestDistance(graph, current)
    distances.append(distance)
    while vertex != None:
        path.append(vertex)
        current = vertex
        current.Visited = True
        distance, vertex = shortestDistance(graph, current)
        if distance != 9999:
            distances.append(distance)

    return [path, distances]
        

#pass in vertex object
def shortestDistance(graph, vertex):
    lowDistance = 9999
    lowObject = None
    for v in graph.vertexList:
        if graph.vertexList[v].Visited == False:
            distance = graph.edge_weights[(vertex, graph.vertexList[v])]
            if float(distance) < float(lowDistance):
                lowDistance = distance
                lowObject = graph.vertexList[v]
    return [lowDistance, lowObject]

    
def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = str(start_vertex.label) + path
    return path

def generateVertecies():
    #generate vertecies for each truck
    v = graph.Vertex(0, True)
    for g in [t1Graph, t2Graph, t3Graph]:
        g.add_vertex(v)
    for truck in [truck1, truck2, truck3]:
        for i in range(len(truck)):
            vertex = graph.Vertex(truck[i])
            if truck == truck1:
                t1Graph.add_vertex(vertex)
            elif truck == truck2:
                t2Graph.add_vertex(vertex)
            else:
                t3Graph.add_vertex(vertex)


def startVertexEdgesCreate():
    for truck in [truck1, truck2, truck3]:
        for i in range(len(truck)):
            package = PACKAGES.search(truck[i])
            packageAddress = package.getAddress()
            dList = DISTANCEDICT["\ufeffHUB"]
            counter = 0
            while ADDRESSLIST[counter] != packageAddress:
                counter += 1
            distance = dList[0][counter]
            if truck == truck1:
                t1Graph.add_undirected_edge(t1Graph.vertexList[0], t1Graph.vertexList[truck[i]], distance)
            elif truck == truck2:
                t2Graph.add_undirected_edge(t2Graph.vertexList[0], t2Graph.vertexList[truck[i]], distance)
            else:
                t3Graph.add_undirected_edge(t3Graph.vertexList[0], t3Graph.vertexList[truck[i]], distance)

    return
#edges created by vertex objects not ids
def generateEdges():
    #generate edges for each truck
    for truck in [truck1, truck2, truck3]:
        for i in range(len(truck)):
            for j in range(1, len(truck)):
                package1 = PACKAGES.search(truck[i])
                package1Address = package1.getAddress()
                package2 = PACKAGES.search(truck[j])
                package2Address = package2.getAddress()
                dList = DISTANCEDICT[package1Address]

                counter = 0
                while ADDRESSLIST[counter] != package2Address:
                    counter += 1
                distance = dList[0][counter]
                if truck == truck1:
                    t1Graph.add_undirected_edge(t1Graph.vertexList[truck[i]], t1Graph.vertexList[truck[j]], distance)
                elif truck == truck2:
                    t2Graph.add_undirected_edge(t2Graph.vertexList[truck[i]], t2Graph.vertexList[truck[j]], distance)
                else:
                    t3Graph.add_undirected_edge(t3Graph.vertexList[truck[i]], t3Graph.vertexList[truck[j]], distance)


#load package data into items and hashTable
def loadPackageData(fileName):
    #if os.path.isfile(fileName):
        with open(fileName) as packages:
            packageData = csv.reader(packages, delimiter=',')
            next(packageData)
            for package in packageData:
                id = int(package[0])
                address = package[1]
                city = package[2]
                state = package[3]
                zip = package[4]
                deadline = package[5]
                mass = package[6]
                note = package[7]
           
                pack = p.Package(id, address, city, state, zip, deadline, mass, note)
 
                PACKAGES.insert(id, pack)

#load distance data into distance dictionary and addresslist
def loadDistanceData(fileName):
    if os.path.isfile(fileName):
        with open(fileName) as distances:
            distanceData = csv.reader(distances, delimiter=',')
            for distance in distanceData:
                a = distance[0]
                distance.pop(0)
                d = [distance]

                ADDRESSLIST.append(a)
                DISTANCEDICT[a] = d


if (__name__ == "__main__"):
    main()