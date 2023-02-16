import algorithm as algo
import hashTable as hash
import package as p
import csv


hashTable = hash.ChainingHashTable(40)
distancesList = []
addressesList = []

def main():
    #algo.tsp(dataSet) #to run algo
    loadPackageData("packageFile.csv")
    loadDistanceData("distanceFile.csv")
    #loadAddressData("addressFile.csv")
    for p in addressesList:
        print(str(p) + "\n")


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
            a = distance[0]
            distance.pop(0)
            d = [distance]

            addressesList.append(a)
            distancesList.append(d)


def loadAddressData(fileName):
    with open(fileName) as addresses:
        addressData = csv.reader(addresses, delimiter=',')
        next(addressData)
        for address in addressData:
            addressesList.append(address)


if (__name__ == "__main__"):
    main()