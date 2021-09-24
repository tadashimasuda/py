class Person(object):
    def __init__(self,name):
        self.name = name
        print(self.name)

    def say_somthing(self):
        print('hello')
        self.run(10)

    def run(self,num):
        print('run' * num)

    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_somthing()

del person
print('#####')

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('#####')

toyota_car = ToyotaCar()
toyota_car.run()

print('#####')

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()