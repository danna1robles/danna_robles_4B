# Practica 2: Atributos publicos y privados

class Persona:
    def __init__(self, nombre, edad): # Constructor de una clase, para agregar atributos a un objeto
        self.nombre = nombre
        self.edad = edad #Atributo publico
        self.__cuenta = None #Atributo privado

    def presentarse(self):
            print(f"Hola mi nombre es {self.nombre}, y tengo {self.edad}")

    def cumplir_anios(self):
            self.edad += 1
            print(f"Esta persona cumplio {self.edad} anios")
    
    def asignar_cuenta(self, cuenta):
          self.__cuenta = cuenta
          print(f"{self.nombre} ahora tiene una cuenta bancaria")

    def consultar_saldo(self):
          if self.__cuenta:
                print(f"El saldo de {self.nombre} es ${self.__cuenta.mostrar_saldo}")
          else:
                print(f"{self.nombre} aun no tiene cuenta bancaria")

class cuenta_bancaria:
      def __init__(self, num_cuenta, saldo):
            self.num_cuenta = num_cuenta
            self.__saldo = saldo #Atributo privado

      def mostrar_saldo(self):
       return self.__saldo

      def depositar(self, cantidad):
            if cantidad > 0:
                  self.__saldo += cantidad
                  print(f"Se deposito la cantidad de ${cantidad} a la cuenta, nuevo si")
            else:
                  print("Ingresa una calntidad valida")

# Actividad 1.
      def retirar(self, cantidad):
            
            if cantidad > 0:
                if cantidad <= self._saldo:
                    self.__saldo -= cantidad
                    print(f"Se retiraron $ {cantidad}. Nuevo saldo: $ {self.__saldo}")
                else:
                 print ("Fondos insuficientes.")
            else:
                print ("Ingresa una cantidad válida.")


# Crear un objeto o instancia de la clase
persona1 = Persona("Miguel", 20)
cuenta1 = cuenta_bancaria("001", 500)

persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo

cuenta1.depositar(200)

# Acceder a los valores de los atributos publicos
print(persona1.nombre)
print(persona1.edad)
