class Person(object):
    def __init__(self,name):
        self.name = name
        print(self.name)

    def say_somthing(self):
        print('hello')
        self.run(10)

    def run(self,num):
        print('run' * num)

person = Person('Mike')
person.say_somthing()

