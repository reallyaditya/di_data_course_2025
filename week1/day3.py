class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

    def wag_tail(self):
        print("Wagging tail")

    def sit(self):
        print(self.name + " is sitting")


# Create an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever", 3)

# Access the attributes of the object
print(my_dog.name)
my_dog.name = "Rick"
print(my_dog.breed)
print(my_dog.age)

# Call the bark method
my_dog.bark()
