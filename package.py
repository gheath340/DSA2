
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, specialNote):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self. deadline = deadline
        self.mass = mass
        self.specialNote = specialNote
        self.status = "at hub"

    def getID(self):
        return self.id

    def setID(self, value):
        self.id = value

    def getAddress(self):
        return self.address

    def setAddress(self, value):
        self.address = value
        
    def getCity(self):
        return self.city

    def setCity(self, value):
        self.city = value
    
    def getState(self):
        return self.state

    def setState(self, value):
        self.state = value

    def getZip(self):
        return self.zip

    def setZip(self, value):
        self.zip = value

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, value):
        self.deadline = value

    def getMass(self):
        return self.mass

    def setMass(self, value):
        self.mass = value

    def getSpecialNote(self):
        return self.specialNote

    def setSpecialNote(self, value):
        self.specialNote = value

    def getStatus(self):
        return self.status

    def setStatus(self, value):
        self.status = value