class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
            return f"{self.name} бррррррр "
my_cat = Cat('alah')
print(my_cat.speak())
my_cat.name = 'обрыган'
print(my_cat.name)
