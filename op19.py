class Car:

    name = ""

    speed =0

 

    def __init__(self, name, speed) :

        self.name = name

        self.speed = speed

 

    def getname(self) :

        return self.name

 

    def getspeed(self) :

        return self.speed

 

car1, car2= None, None

 

 

car1 = Car("아우디",0)

car2 = Car("벤츠", 30)

 

 

print("%s의 현재 속도는 %d입니다." % (car1.getname(), car1.getspeed()))

print("%s의 현재 속도는 %d입니다." % (car2.getname(), car2.getspeed()))
