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

# person = Person('Mike')
# person.say_somthing()

# del person
# print('#####')

class Car(object):
    def __init__(self,model=None):
        self.model = model
        print('run __init__')

    def run(self):
        print('run')

    def ride(self,person):
        person.drive()

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def __init__(self,model='Model S',enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self,is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print('super run')
    def auto_run(self):
        print('auto run')

# print('#####')
# tesla_car = TeslaCar('model S')
# tesla_car.enable_auto_run =True
# print(tesla_car.enable_auto_run)

class Person(object):
    def __init__(self,age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self,age =1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self,age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

# baby = Baby()
# adult = Adult()
#
# car = Car()
# car.ride(adult)

class Word(object):
    def __init__(self,text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self,word):
        return self.text.lower() + self.text.lower()

w = Word('test')
w2 = Word('test')

print(w.text)
print(w)

print(len(w.text))
print(len(w))