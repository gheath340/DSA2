import algorithm as algo
import hashTable as hash
import package as p
import graph
import csv


PACKAGES = hash.ChainingHashTable(40)
DISTANCEDICT = {}
ADDRESSLIST = []


def main():
    loadPackageData("packageFile.csv")
    loadDistanceData("goodDistanceTable.csv")
    truck1 = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck2 = [3, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 23, 24, 25, 36, 38]
    truck3 = [9, 26, 27, 28, 32, 33, 35, 39]
    #FIGURING OUT HOW IM MAKING GRAPHS AND HOW IM CONNECTING ALL VERTEXES
    #create graph for each truck
    t1Graph = graph.Graph()
    t2Graph = graph.Graph()
    t3Graph = graph.Graph()
    # for distance in DISTANCEDICT:
    #     print(distance + str(DISTANCEDICT[distance]))
    #generate vertecies for each truck
    for i in range(len(truck1)):
        vertex = graph.Vertex(truck1[i])
        t1Graph.add_vertex(vertex)
    for i in range(len(truck2)):
        vertex = graph.Vertex(truck2[i])
        t2Graph.add_vertex(vertex)
    for i in range(len(truck3)):
        vertex = graph.Vertex(truck3[i])
        t3Graph.add_vertex(vertex)
    #generate edges for each truck(from each vertex to every other vertex) length^2
    for i in range(len(truck1)):
        for j in range(1, len(truck1)):
            package1 = PACKAGES.search(truck1[i])
            package1Address = package1.getAddress()
            package2 = PACKAGES.search(truck1[j])
            package2Address = package2.getAddress()
            dList = DISTANCEDICT[package1Address]

            counter = 0
            while ADDRESSLIST[counter] != package2Address:
                counter += 1
            distance = dList[0][counter]
            print(package1Address)
            print(package2Address)
            print(distance)
            t1Graph.add_undirected_edge(t1Graph.vertexList[truck1[i]], t1Graph.vertexList[truck1[j]], distance)


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
 
            PACKAGES.insert(id, pack)


def loadDistanceData(fileName):
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