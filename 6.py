class Animal:
    def init(self, name):
        self.name = name


class Dog(Animal):
    def init(self, name):
        super().init(name)
        self.sound = "Woof"


dog1 = Dog("Rex")

print("Itning nomi:", dog1.name)
print("Itning tovushi:", dog1.sound)