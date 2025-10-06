
#practica 1 clases, objetos y atributos 

# una clase es una plantilla o un molde que define como sera un objeto 
class persona:
    def __init__(self, nombre, edad): #contructor de una clase 
        self.nombre = nombre
        self.edad = edad
        

    def presentarse (self):
        print(f"hola mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_años (self):
        self.edad += 1
        print(f"esta persona cumplio: {self.nombre} ahora tienes {self.edad} años")
##aigna metos a esos objetos 
#un objeto es una instancia creada a partir de una clase
#crear objetos que pertenece a una clase
estudiante1 = persona ("robles", 19)
estudiante2 = persona ("lucia", 18)

estudiante1.presentarse ()
estudiante1.cumplir_años ()

#paso 1 agrega un metodo cumplir años que aumente en 1 la edad

#INSTANCIA:
#cada objeto creado de una clese es una instancia podemos tener varias inastancias que coexistan con sus propios datos
#el objeto = instancia de la clase 
#cada vez que se crea un objeto con clases() se obtiene una instancia dependiente.
#cada instancia tiene sus propios datos aunque venga de la misma clase.


#abstraccion
#representar solo lo importante del mundo real, ocultando detalles importantess

class automovil:
    def __init__(self, marca):
        self.marca = marca 

    def arrancar(self):
        print(f"{self.marca} arranco ")
    
#crear un objeto auto y asignar una marca
auto = automovil("ford")
auto.arrancar()
#abstraccion: nos centramos solo en lo que importa (accion) que es arrancar el automovil, ocultando detalles internos como motor, transmision 
#tipo_conbustible
#enfoque solo en la accion del objeto.
#objetivo es hacer el codigo mas limpio y faciol d usar.

#1. crear una clase masota 
#2. agregar minimo 4 atributos
#3. definir al enos 4 metodos
#4. crear 2 instancia de la clase 
#5. llamr los metods y aplicar abtraccion. (agregar un atributo innecesario)

class mascota:

    def __init__(self, nombre, edad, tipo, raza, color):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.raza = raza
        self.color = color #atributo innecesario

    def ladrar(self):
        print(f"hola mi nombre es  {self.nombre} esta ladrando,tengo {self.edad},soy un {self.tipo}, mi raza es {self.raza}, mi color es {self.color} ")

perrito = mascota("rocry",3, "perro", "pastor aleman", "marron")

perrito.ladrar()
