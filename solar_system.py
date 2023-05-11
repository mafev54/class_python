class Planet:
    def __init__(self, name, distance_sun, radius, gravity, mass, orbital_period):
        self.__name = name
        self.__distance_sun = distance_sun
        self.__radius = radius
        self.__gravity = gravity
        self.__mass = mass
        self.__orbital_period = orbital_period
        self.stop = False

    def get_name1(self):
        return self.__name

    def set_name1(self, name):
        self.__name = name

    def get_distance_sun1(self):
        return self.__distance_sun

    def set_distance_sun1(self, distance_sun):
        self.__distance_sun = distance_sun

    def get_radius1(self):
        return self.__radius

    def set_radius1(self, radius):
        self.__radius = radius

    def get_gravity1(self):
        return self.__gravity

    def set_gravity1(self, gravity):
        self.__gravity = gravity

    def get_mass1(self):
        return self.__mass

    def set_mass1(self, mass):
        self.__mass = mass

    def get_orbital_period1(self):
        return self.__orbital_period

    def set_orbital_period1(self, orbital_period):
        self.__orbital_period = orbital_period


class Moon(Planet):
    def __init__(self, name, distance_sun, radius, gravity, mass, orbital_period, moon_name, moon_orbital, moon_mass, moon_gravity, moon_radius):
        super().__init__(name, distance_sun, radius, gravity, mass, orbital_period)
        self.__moon_name = moon_name
        self.__moon_orbital = moon_orbital
        self.__moon_mass = moon_mass
        self.__moon_gravity = moon_gravity
        self.__moon_radius = moon_radius

    def get_moon_name1(self):
        return self.__moon_name

    def set_moon_name1(self, moon_name):
        self.__moon_name = moon_name

    def get_moon_orbital1(self):
        return self.__moon_orbital

    def set_moon_orbital1(self, moon_orbital):
        self.__moon_orbital = moon_orbital

    def get_moon_mass1(self):
        return self.__moon_mass

    def set_moon_mass1(self, moon_mass):
        self.__moon_mass = moon_mass

    def get_moon_gravity1(self):
        return self.__moon_gravity

    def set_moon_gravity1(self, moon_gravity):
        self.__moon_gravity = moon_gravity

    def get_moon_radius1(self):
        return self.__moon_radius

    def set_moon_radius1(self, moon_radius):
        self.__moon_radius = moon_radius


planet = Moon("Earth", "149.6 millions km", "6,371 km", "9.807 m/s²", "5.972E24 kg",
              "365", "planetary natural satellite", "27.32", "7,349E22 kg", "1.62 m/s²", "1.737.1 km")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
earth = print("Our home, planet Earth, is a rocky, terrestrial planet. It has a solid, active surface, with mountains, valleys, \n"
              "canyons, plains and much more.Earth is special because it is an ocean planet, with water covering 70 percent of its surface.\n")

print(f"This is the planet {planet.get_name1()}, its distance from the sun is {planet.get_distance_sun1()}, besides this it has a radius of {planet.get_radius1()},\n"
      f"its gravity is {planet.get_gravity1()}, its mass is {planet.get_mass1()}, it takes  {planet.get_orbital_period1()} days to go around the sun.\n"
      f"Now let's talk about the moon. It is called {planet.get_moon_name1()}, it takes { planet.get_moon_orbital1()} days to go around the earth, \n"
      f"it has a mass of{ planet.get_moon_mass1()}, we also know that it has a gravity of { planet.get_moon_gravity1()}, and its raidus is { planet.get_moon_radius1()}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
planet.set_name1("Mars")
planet.set_distance_sun1("227.9 millones km")
planet.set_radius1("3,389.5 km")
planet.set_gravity1("3.721 m/s²")
planet.set_mass1("6.39x10^23 kg")
planet.set_orbital_period1("687")
planet.set_moon_name1("fobos")
planet.set_moon_orbital1("8 hrs")
planet.set_moon_mass1("1,072-1016 kg")
planet.set_moon_gravity1(" 0.0057 m/s²")
planet.set_moon_radius1("11.267 km")

mars = print(f"Mars is a cold desert planet. It is half the size of Earth, and is also called the ""red planet"".\n"
             f"It is red because of the rusty iron in the soil. Like Earth, Mars has seasons, ice caps, volcanoes, canyons, and weather.\n")

print(f"This is the planet {planet.get_name1()}, its distance from the sun is {planet.get_distance_sun1()}, besides this it has a radius of {planet.get_radius1()},\n"
      f"its gravity is {planet.get_gravity1()}, its mass is {planet.get_mass1()}, it takes  {planet.get_orbital_period1()} days to go around the sun.\n"
      f"Now let's talk about the moon. It is called {planet.get_moon_name1()}, it takes { planet.get_moon_orbital1()} days to go around the earth, \n"
      f"it has a mass of{ planet.get_moon_mass1()}, we also know that it has a gravity of { planet.get_moon_gravity1()}, and its raidus is { planet.get_moon_radius1()}")
