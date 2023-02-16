import algorithm as algo
import hashTable as hash
import package as p
import csv


hashTable = hash.ChainingHashTable(40)

def main():
    #algo.tsp(dataSet) #to run algo
    loadPackageData("WGUPS Package File.csv")

    return

def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData) # skip header
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
 
            # insert it into the hash table
            hashTable.insert(id, p)


if (__name__ == "__main__"):
    main()