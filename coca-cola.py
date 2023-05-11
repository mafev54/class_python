class Coca_cola:
    def __init__(self, quantity, sugar, coloring, flavorings, acidifier, caffeine):
        self.__quantity = quantity
        self.__sugar = sugar
        self.__coloring = coloring
        self.__flavorings = flavorings
        self.__acidifier = acidifier
        self.__caffeine = caffeine
        self.__to_open = False
        self.__to_drink = False

    def get_quantity1(self):
        return self.__quantity

    def set_quantity1(self, quantity):
        self.__quantity = quantity

    def get_sugar1(self):
        return self.__sugar

    def set_sugar1(self, sugar):
        self.__sugar = sugar

    def get_coloring1(self):
        return self.__coloring

    def set_coloring1(self, coloring):
        self.__coloring = coloring

    def get_flavorings1(self):
        return self.__flavorings

    def set_flavorings1(self, flavorings):
        self.__flavorings = flavorings

    def get_acidifier1(self):
        return self.__acidifier

    def set_acidifier1(self, acidifier):
        self.__acidifier = acidifier

    def get_caffeine1(self):
        return self.__caffeine

    def to_open(self):
        self.__to_open = True
        print("You opened it.")

    def to_drink(self):
        self.__to_drink = True
        print("Drink it.")


class Monster(Coca_cola):
    def __init__(self, quantity, sugar, coloring, flavorings, acidifier, caffeine, taurine, vitamin):
        super().__init__(quantity, sugar, coloring, flavorings, acidifier, caffeine)
        self.__taurine = taurine
        self.__vitamin = vitamin

    def get_taurine1(self):
        return self.__taurine

    def get_vitamin1(self):
        return self.__vitamin


coca = Coca_cola("coke", "sugar", "caramel", "lime, lemon, orange, neroli, cinnamon, nutmeg and vanilla.",
                 "Phosphoric acid", "caffeine")

print(f"{coca.get_quantity1()} is a product that has {coca.get_sugar1()}, {coca.get_coloring1()} {coca.get_flavorings1()} as a colorant and flavoring,\n "
      f"{coca.get_acidifier1()} and has {coca.get_caffeine1()}.")

drink = Monster("monster", "sugar", "caramel", "lime, lemon, orange, neroli, cinnamon, nutmeg and vanilla.",
                "Phosphoric acid", "caffeine", "taurine", "vitamin")

print("Monster")

print(f"{drink.get_quantity1()} is a product that has {drink.get_sugar1()}, {drink.get_coloring1()} {drink.get_flavorings1()} as a colorant, and flavoring,\n "
      f"{drink.get_acidifier1()}, has {drink.get_caffeine1()}, has {drink.get_taurine1()},and has {drink.get_vitamin1()}")

drink.to_open()
drink.to_drink()
