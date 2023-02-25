#GARRETT HEATH 010229298
#OVERALL BIGO = O(N^2) + O(N^2) + O(N^2) + O(N^3) + O(N^4) + 3O(2N) + 3O(N) + 2O(N) = O(N^4)
import algorithm as algo
import hashTable as hash
import package as p
import graph
import csv
import os
import truck
import datetime
import re
from pathlib import Path

PACKAGES = hash.HashTable(40)
DISTANCEDICT = {}
ADDRESSLIST = []

#package ids for each truck
truck1 = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2 = [3, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 23, 24, 25, 36, 38]
truck3 = [9, 26, 27, 28, 32, 33, 35, 39]
#create graph for each truck
t1Graph = graph.Graph()
t2Graph = graph.Graph()
t3Graph = graph.Graph()
#truck speed mph
truckSpeed = 18
#time for each truck
t1Time = datetime.datetime(100,1,1,8,0,0)
t2Time = datetime.datetime(100,1,1,9,5,0)
t3Time = datetime.datetime(100,1,1,9,42,00)

def main():
    #load all data
    absolute_path = os.path.dirname(__file__)
    relative_path = "packageFile.csv"
    full_path = os.path.join(absolute_path, relative_path)
    loadPackageData(full_path)

    absolute_path = os.path.dirname(__file__)
    relative_path = "goodDistanceTable.csv"
    full_path = os.path.join(absolute_path, relative_path)
    loadDistanceData(full_path)
    #create graph data
    generateVertecies()
    startVertexEdgesCreate()
    generateEdges()
    #truck objects
    truck1Obj = truck.Truck(truck1, t1Graph, t1Time)
    truck2Obj = truck.Truck(truck2, t2Graph, t2Time)
    truck3Obj = truck.Truck(truck3, t3Graph, t3Time)
    #get the path of each truck
    t1Path, t1Distances = getPath(t1Graph, t1Graph.vertexList[0])
    t2Path, t2Distances = getPath(t2Graph, t2Graph.vertexList[0])
    t3Path, t3Distances = getPath(t3Graph, t3Graph.vertexList[0])

    checkTime = input("What time? (military time HH:MM:SS): ")
    #make sure input is formatted correctly
    if re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$', checkTime):
        #see if truck has left by entered time
        truck1Left = checkTruckLeavingTime(checkTime, truck1Obj)
        truck2Left = checkTruckLeavingTime(checkTime, truck2Obj)
        truck3Left = checkTruckLeavingTime(checkTime, truck3Obj)
        #if truck has left deliver packages until input time
        if truck1Left:
            truck1Obj.distance = deliverPackages(t1Path, t1Distances, truck1Obj, t1Graph, checkTime)
        if truck2Left:
            truck2Obj.distance = deliverPackages(t2Path, t2Distances, truck2Obj, t2Graph, checkTime)
        if truck3Left:
            truck3Obj.distance = deliverPackages(t3Path, t3Distances, truck3Obj, t3Graph, checkTime)
        totalDistance = truck1Obj.distance + truck2Obj.distance + truck3Obj.distance
        if checkTime > "10:20:00":
            PACKAGES.search(9).setAddress("410 S State St")
        #ui code
        print("1. Print All Package Status and Total Mileage")
        print("2. Get a Single Package Status with a Time")
        print("3. Get All Package Status with a Time")
        print("4. Get single package info")
        print("5. Exit Program")
        option = input("Enter number of option youd like to select: ")
        if option == "1":
            printAllPackageStatus(truck1Obj, truck2Obj, truck3Obj)
            print("\nDistance: " + str(totalDistance))
        elif option == "2":
            singleID = input("Package ID: ")
            printPackageStatus(singleID)
            print("\nTime: " + str(checkTime))
        elif option == "3":
            printAllPackageStatus(truck1Obj, truck2Obj, truck3Obj)
            print("\nTime: " + str(checkTime))
        elif option == "4":
            id = input("Package ID: ")
            printPackageInfo(id)
        elif option == "5":
            quit()
        else:
            print("Please select a valid option:")
            option = input("Enter number of option youd like to select: ")
    else:
        print("Please match the format given.")
        input("What time? (Military time HH:MM:SS): ")

#print all info of given package
#bigO = O(1)
def printPackageInfo(id):
    package = PACKAGES.search(int(id))
    print("ID: " + str(package.getID()))
    print("Address: " + package.getAddress())
    print("Deadline: " + str(package.getDeadline()))
    print("City: " + package.getCity())
    print("Zip: " + str(package.getZip()))
    print("Weight: " + str(package.getMass()))
    print("Status: " + package.getStatus())

#bigO = O(N)
#print status for every package
def printAllPackageStatus(truck1, truck2, truck3):
    for package in truck1.packages:
        print("ID: " + str(package) + "\nStatus: " + PACKAGES.search(package).getStatus())
    for package in truck2.packages:
        print("ID: " + str(package) + "\nStatus: " + PACKAGES.search(package).getStatus())
    for package in truck3.packages:
        print("ID: " + str(package) + "\nStatus: " + PACKAGES.search(package).getStatus())

#print status of given package
#bigO = O(1)
def printPackageStatus(id):
    package = PACKAGES.search(int(id))
    print(package.getStatus())

#bigO = O(1)
#deliver given package/update status
def deliverPackage(truck, id, distance, cuttoffTime):
    package = PACKAGES.search(id.label)
    deliveryTime = (distance / truckSpeed) * 3600
    tempTime = truck.time + datetime.timedelta(seconds=deliveryTime)
    if str(tempTime.time()) < cuttoffTime:
        truck.time +=  datetime.timedelta(seconds=deliveryTime)
        package.setStatus("Delivered at " + str(truck.time))
    else:
        package.setStatus("In route")

#bigO = O(N)
#deliver/update status of all packages
def deliverPackages(truckPath, truckDistances, truck, graph, checkTime):
    totalDistance = 0.0
    for id in range(len(truckPath)):
        if truckPath[id].label != 0:
            distance = truckDistances[id-1]
            deliverPackage(truck, truckPath[id], float(distance), checkTime)
            totalDistance += float(distance)
    return totalDistance

#get trucks path
#bigO = O(2N)
def getPath(graph, start):
    path = []
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

#see if truck has left at a given time
#bigO = O(1)
def checkTruckLeavingTime(cuttoffTime, truck):
    truckTime = str(truck.time.time())
    if truckTime < cuttoffTime:
        return True
    return False

#get shortest distance from given vertex in a graph
#bigO = O(N^2)
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

#bigO = O(N^2)
#generate all vertecies
def generateVertecies():
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

#bigO = O(N^3)
#generate edges from hub
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

#generate all non starting edges
#bigO = O(N^4)
def generateEdges():
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

#load package data from csv
#bigO = O(N^2)
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

#bigO = O(N^2)
#load distance data from csv
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