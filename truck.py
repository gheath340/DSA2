

class Truck:
    def __init__(self, packageList, graph, time):
        self.packages = packageList
        self.distance = 0
        self.speed = 18
        self.graph = graph
        self.time = time

    def getPackages(self):
        return self.packages
    
    def setPackages(self, value):
        self.packages = value

    def getDistance(self):
        return self.distance
    
    def setDistance(self, value):
        self.distance = value

    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, value):
        self.speed = value

    def getGraph(self):
        return self.graph
    
    def setGraph(self, value):
        self.graph = value

    def getTime(self):
        return self.time
    
    def setTime(self, value):
        self.Time = value

    
