class Person:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 100
        self.__name = "Arjun"

    def driving(self):
        print("Driving")
        print(self.__maxspeed)

    def setspeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed)


obj = Person()
obj.driving()
obj.setspeed(200)
