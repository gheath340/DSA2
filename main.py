import algorithm as algo
import hashTable as hash
import package as p
import csv


PACKAGES = hash.ChainingHashTable(40)
DISTANCELIST = []
ADDRESSLIST = []

def main():
    #algo.tsp(dataSet) #to run algo
    loadPackageData("packageFile.csv")
    loadDistanceData("goodDistanceTable.csv")
    truck1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 2, 4, 5]
    truck2 = [3, 6, 18, 25, 36, 38, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24]
    truck3 = [9, 28, 32, 26, 27, 33, 35, 39]



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

#create the graph w/ location as key and list of distances as value list


if (__name__ == "__main__"):
    main()