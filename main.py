import algorithm as algo
import hashTable as hash
import package as p
import csv


hashTable = hash.ChainingHashTable(40)
distancesList = []

def main():
    #algo.tsp(dataSet) #to run algo
    loadPackageData("WGUPS Package File.csv")
    loadDistanceData("WGUPS Distance Table.csv")

    return

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
 
            hashTable.insert(id, p)

def loadDistanceData(fileName):
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)
        for distance in distanceData:
            d = [distance]

            distancesList.append(d)


if (__name__ == "__main__"):
    main()