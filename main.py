import algorithm as algo
import hashTable as hash
import package as p
import graph
import csv


PACKAGES = hash.ChainingHashTable(40)
DISTANCELIST = []
ADDRESSLIST = []

def main():
    loadPackageData("packageFile.csv")
    loadDistanceData("goodDistanceTable.csv")
    truck1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 2, 4, 5]
    truck2 = [3, 6, 18, 25, 36, 38, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24]
    truck3 = [9, 28, 32, 26, 27, 33, 35, 39]
    #MAPPING ALL DISTANCES OF ADDRESSES TO EACHOTHER
    #create graph for each truck
    t1Graph = graph.Graph()
    t2Graph = graph.Graph()
    t3Graph = graph.Graph()
    #generate vertecies for each truck
    for i in range(len(truck1)):
        vertex = graph.Vertex(str(truck1[i]))
        t1Graph.add_vertex(vertex)
    for i in range(len(truck2)):
        vertex = graph.Vertex(str(truck2[i]))
        t2Graph.add_vertex(vertex)
    for i in range(len(truck3)):
        vertex = graph.Vertex(str(truck3[i]))
        t3Graph.add_vertex(vertex)
    #generate edges for each truck(from each vertex to every other vertex) length^2
    for i in range(len(truck1)):
        for j in range(len(truck1)):
            t1Graph.add_undirected_edge(truck1[i], truck1[j], )


def loadPackageData(fileName):
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
 
            PACKAGES.insert(id, p)


def loadDistanceData(fileName):
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        for distance in distanceData:
            a = distance[0]
            distance.pop(0)
            d = [distance]

            ADDRESSLIST.append(a)
            DISTANCELIST.append(d)


if (__name__ == "__main__"):
    main()