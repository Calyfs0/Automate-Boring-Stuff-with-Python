class Robot_Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print('Woof Woof!')


# Main

robotDog = Robot_Dog('Rosie', 'Street Dog')
print(robotDog.name)
print(robotDog.breed)
robotDog.bark()
