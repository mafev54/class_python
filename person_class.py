class Human:
    def __init__(self, gender, weight, height):
        self.__gender = gender
        self.__weight = weight
        self.__height = height
        self.__eat = False
        self.__sleep = False
        self.__read = False

    def eat(self):
        self.__eat = True
        print("I'm eating.")

    def sleep(self):
        self.__sleep = False
        print("I'm sleeping. DO NOT DISTURB.")

    def read(self):
        self.__read = True
        print("I'm reading right now.")

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height


class Person(Human):
    def __init__(self, name, age, profession, gender, weight, height):
        super().__init__(gender, weight, height)
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__greet = False

    def start_to_greet(self):
        self.__greet = True
        print("Hi there!")

    def stop_greeting(self):
        self.__greet = False
        print("Goodbye!")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_profession(self):
        return self.__profession

    def set_profession(self, profession):
        self.__profession = profession


person1 = Person("Mafe", "17", "developer", "Female", "x", "x")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
person1.start_to_greet()

print(f"Hi, I'm {person1.get_name()}, I'm {person1.get_age()} years old.\n "
      f"I am not yet a professional, but I want to be a {person1.get_profession()} someday.\n "
      f"My gender is {person1.get_gender()}, my weight is {person1.get_weight()}, and my height is {person1.get_height()}.")

person1.stop_greeting()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

person1.set_weight("45 kg")
person1.set_age("18")
person1.start_to_greet()

print(f"Hi, I'm {person1.get_name()}, I'm {person1.get_age()} years old.\n "
      f"I am not yet a professional, but I want to be a {person1.get_profession()} someday.\n "
      f"My gender is {person1.get_gender()}, my weight is {person1.get_weight()}, and my height is {person1.get_height()}.")

person1.read()
person1.stop_greeting()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

person1.start_to_greet()

person1.set_name("juan david")
person1.set_weight("x")
person1.set_profession("industrial mechanics")
person1.set_gender("Male")
person1.set_age("x")

print(f"Hi, I'm {person1.get_name()}, I'm {person1.get_age()} years old.\n "
      f"I am not yet a professional, but I want to be a {person1.get_profession()} someday.\n"
      f"My gender is {person1.get_gender()}, my weight is {person1.get_weight()}, and my height is {person1.get_height()}. And we are in 2023")

person1.eat()
person1.stop_greeting()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

person1.sleep()
