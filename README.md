# POO python

En Python, puedes crear una clase utilizando la palabra clave class. Una clase es una estructura que define un nuevo tipo de objeto, con sus propiedades (atributos) y comportamientos (métodos). Aquí tienes un ejemplo básico de cómo crear una clase en Python:

<class MiClase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2>

    def metodo1(self):
        # código del método 1
        pass

    def metodo2(self, parametro):
        # código del método 2 que recibe un parámetro
        pass


En este ejemplo, hemos creado una clase llamada MiClase. La función especial __init__ es el constructor de la clase, que se llama automáticamente cuando se crea un nuevo objeto de la clase. En el constructor, se definen los atributos de la clase (self.atributo1 y self.atributo2) y se inicializan con los valores pasados como parámetros (parametro1 y parametro2).

La clase también tiene dos métodos, metodo1 y metodo2. Ambos métodos toman self como primer parámetro, que es una referencia al objeto de la clase actual. Puedes definir más parámetros después de self si es necesario.

Dentro de los métodos, puedes escribir el código que define el comportamiento de la clase. En el ejemplo, se utilizan los comentarios # código del método para indicar dónde iría el código real.

Una vez que has definido tu clase, puedes crear objetos (instancias) de esa clase utilizando la siguiente sintaxis:

<objeto = MiClase(parametro1, parametro2)

Donde objeto es el nombre de la variable que representa el objeto creado y parametro1 y parametro2 son los valores que se pasan al constructor de la clase.

Puedes acceder a los atributos y llamar a los métodos de un objeto utilizando la notación de punto, por ejemplo:

<print(objeto.atributo1)
<objeto.metodo1()




