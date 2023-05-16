class student:
    def __init__(self, name):
        self.name = name
        self.__private_another = name + ' this private'
        print("class created " + self.name)
    
    def sampleFunction(self):
        print(self.__private_another)
        
    def sampleParams(self, name):
        print(self.name + name)

        


x = student("ervin")

x.sampleFunction()
x.sampleParams("wew")

print(x)