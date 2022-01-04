class MyClass:
    def __init__(self):
        self.property = []

    def newvalue(self, value):
        self.property.append(value)
    
    def findvalue(self, value):
        return self.property.index(value)
