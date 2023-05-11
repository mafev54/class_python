frogs_toads = print("Amphibian Biography: Its name comes from the Greek and means ""both environments"", since its life takes place between the aquatic and terrestrial environments.\n"
                    "They are the amphibian ancestors of the first group of vertebrates that colonized the continent and adapted to a semi-terrestrial life.\n"
                    "They are found in virtually all regions of the world except those with the harshest climatic conditions such as the Arctic, Antarctica and the most extreme deserts.")


class Tadpole:
    def __init__(self, fin, gill):
        self.__fin = fin
        self.__gill = gill
        self.__aquatic_animal = False

    def aquatic(self):
        self.__aquatic_animal = True
        print("the next animal is a tadpole")

    def get_fin(self):
        return self.__fin

    def get_gill(self):
        return self.__gill


class Amphibious(Tadpole):
    def __init__(self, name, scientific_name, age, gender, weight, feeding, fin, gill):
        super().__init__(fin, gill)
        self.__name = name
        self.__scientific_name = scientific_name
        self.__age = age
        self.__gender = gender
        self.__weight = weight
        self.__feeding = feeding
        self.__rana = False
        self.__sapo = False

    def first_frog(self):
        self.__rana = True
        print("the next animal is a frog")

    def first_toad(self):
        self.__sapo = True
        print("the next animal is a toad")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_scientific_name(self):
        return self.__scientific_name

    def set_scientific_name(self, scientific_name):
        self.__scientific_name = scientific_name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_feeding(self):
        return self.__feeding


amphibious1 = Amphibious("glass frog", "Centrolenidae", "5 years", "Female",
                         "200 gr", "insects: fly larvae, young grasshoppers, etc.", "fin", "gill")

amphibious1.first_frog()

print(f"this is a  {amphibious1.get_name()}, its scientific name is {amphibious1.get_scientific_name()}, it is {amphibious1.get_age()},"
      f" its a {amphibious1.get_gender()}, it weighs {amphibious1.get_weight()}, its diet are {amphibious1.get_feeding()},"
      f" it doesn't have {amphibious1.get_fin()}, it doesn't have { amphibious1.get_gill()}")

print("................................................................................................................................")

amphibious1.first_toad()

amphibious1.set_name("American toad")
amphibious1.set_scientific_name("Anaxyrus americanus")
amphibious1.set_age("2")
amphibious1.set_gender("Male")
amphibious1.set_weight("95 gr")

print(f"this is a  {amphibious1.get_name()}, its scientific name is {amphibious1.get_scientific_name()}, it is {amphibious1.get_age()},"
      f" its a {amphibious1.get_gender()}, it weighs {amphibious1.get_weight()}, its diet are {amphibious1.get_feeding()},"
      f" it doesn't have {amphibious1.get_fin()}, it doesn't have { amphibious1.get_gill()}")

print("................................................................................................................................")

amphibious1.aquatic()

amphibious1.set_name("tadpole")
amphibious1.set_scientific_name("Pelophylax perezi")
amphibious1.set_age("1 month")
amphibious1.set_gender("Male")
amphibious1.set_weight("20 gr")

print(f"this is a  {amphibious1.get_name()}, its scientific name is {amphibious1.get_scientific_name()}, it is {amphibious1.get_age()},"
      f" its a {amphibious1.get_gender()}, it weighs {amphibious1.get_weight()}, its diet are {amphibious1.get_feeding()},"
      f" it doesn't have {amphibious1.get_fin()}, it doesn't have { amphibious1.get_gill()}")

print("................................................................................................................................")
