class Animal:#method 1 class

    def run(self):
        print('animal is running')
    def eating(self):
        print('animal is eating')
dog = Animal()
dog.eating()
dog.run()
dog.breed='puddle'# adding breed
dog.age=5
print(dog.age)

#method 2
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n')


class Pet:
    def __init__(self,breed,colour,age): #by using a constructor
        self.breed=breed
        self.colour=colour
        self.age=age
    def run(self):
        print('dog is running')
    def eats(self):
        print('animal is eating....')
    def types(self):
        print('the breed is good')

dogs= Pet('puddle','golden',5)

print(dogs.breed)
print(dogs.age)
print(dogs.colour)
print(dogs.eats())


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n')

#create a class that will display a draw line
#when you create a line you have to specify its lemngth and draw lines

class Line:
    def __init__(self,length,x,y):
        self.length=length
        self.x=x
        self.y=y
    def draw(self):
        print('drawing...')

    def display(self):
        print('display....')

line1= Line(5,1,2)
print(line1.length)
print(line1.draw())


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n')

#inheritance

class Human:
    def speak(self):
        print('speaking')

class German(Human): #inherit the method from human class
    pass
class French(Human):
    pass
adi= French()
adi.speak()


