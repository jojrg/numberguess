class Foo:

    def __init__(self):
        self.name = 'Max'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val


myFoo = Foo()
print(myFoo.name)
myFoo.name = 'jochen'
print(myFoo.name)
