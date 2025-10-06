#PRACTICA 4  HERENCIA
#Danna MIChell RObles  HOY ES  22 DE SEPTIEMBRE 

#CREAR UNA CLASE "TICKET"  debe de incluir ; 
#ID
#TIPO (POR EJEMPLO SOFTWARE,PRUEBA)
#PRIORIDAD(ALTA, MEDIA , BAJA)
#ESTADO(POR DEFECTO , PENDIENTE
#CREAR DOS TICKETS DE EJEMPLO  Y MOSTRAR POR PANTALLA)


class Ticket:
    def __init__(self, id_ticket, tipo, prioridad, estado="Pendiente"):
        self.id_ticket = id_ticket
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = estado

    def mostrar_info(self):
        print(f"--- Ticket {self.id_ticket} ---")
        print(f"Tipo: {self.tipo}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")
        print("----------------------")


ticket1 = Ticket(1, "Software", "Alta")
ticket2 = Ticket(2, "Prueba", "robles")


ticket1.mostrar_info()
ticket2.mostrar_info()


# AHORA CREAMOS UNA CLASSE  "EMPLEADO ""
#A) crear una clase empleado  con atributo nombre 
#B) crear  metoo  trabajar_en_ticket(self,ticket)que imprima "EL EMPLEADO  <NOMBRE>  REVISA EL TICKET <ID>"


class empleado:
    def __init__(self,nombre):

        self.nombre =nombre
    def trabajar_en_ticket(self, ticket):
        print(f" EL EMPLEADFO  {self.nombre} revisa el ticket {ticket.id_ticket}")

    
empleado1 = empleado("robles")
empleado1.trabajar_en_ticket(ticket1)
empleado1.trabajar_en_ticket(ticket2)




#crea una clase desarrollador  que  herede  de EMPLEADO  y sobreescriba el metodo trabajar en ticket 


class Desarrollador(empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "software":
            ticket.estado = "Resuelto"
            print(f"El desarrollador {self.nombre} resolvió el ticket {ticket.id_ticket} de tipo {ticket.tipo}.")
        else:
            print(f"El desarrollador {self.nombre} no puede resolver el ticket {ticket.id_ticket} (tipo {ticket.tipo}).")


class Tester(empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "prueba":
            ticket.estado = "Resuelto"
            print(f"El tester {self.nombre} resolvió el ticket {ticket.id_ticket} de tipo {ticket.tipo}.")
        else:
            print(f"El tester {self.nombre} no puede resolver el ticket {ticket.id_ticket} (tipo {ticket.tipo}).")



ticket1 = Ticket(1, "Software", "Alta")
ticket2 = Ticket(2, "Prueba", "robles")


dev = Desarrollador("islem")
tester = Tester("angie")


dev.trabajar_en_ticket(ticket1)   
dev.trabajar_en_ticket(ticket2)  

tester.trabajar_en_ticket(ticket1) 
tester.trabajar_en_ticket(ticket2) 

# TESTER ; es la persona  encargada de probar  un sistema, programa o aplicacion  para verificar
# que funcione correctamente  y que no tenga errores antes que llegue al usuario final 




#crer clase    "projectManager" que asigne ticket

class  ProjectManger(empleado):
    def asignar_ticket(self , ticket, empleado):
        print(f"\n el Project Manager {self.nombre} asigna el ticket { ticket.id_ticket} a { empleado.nombre}")
   

# crear ticket  y empleados  / instancias de objetos 

ticket1= Ticket (1, " software" , "alta")
ticket2 = Ticket (2, "prueba" , "robles")
                
dev = Desarrollador("angie")
tester = Tester ("islem")
pm=ProjectManger("robles")

pm.asignar_ticket(ticket1 , dev)
pm.asignar_ticket(ticket2, tester)


pm.asignar_ticket(ticket1 , tester )
pm.asignar_ticket(ticket2 , dev)




#PARTE ADICIONAL
#Agregar un menu  while  y con  if que permita;
#1 crerar un ticket 
#2 Ver ticket
#3 asignar  tickets 
#4 salir  del programa 


#variabl
tickets = []  
empleados = [] 


dev = Desarrollador("islem")
tester = Tester("angie")
pm = ProjectManger("robles")
empleados.extend([dev, tester, pm])

# esta pare es para imprimir en la panatalla 
while True:
    print("\n- MENÚ PRINCIPAL WHILE Y CON IF  ")
    print("1 Crear un ticket")
    print(" Ver tickets")
    print(" Asignar tickets")
    print("Salir del prgrama")

    
# est apartye la tengo como la selleccion de una opcion que es del 12 al 4
#1 crerar un ticket 
#2 Ver ticket
#3 asignar  tickets 
#4 salir  del programa 

    opcion = input("Selecciona una opción Porfavor: ")

    if opcion == "1":
        id_ticket = len(tickets) + 1
        tipo = input("Ingrese el tipo de ticket (Software/Prueba): ")
        prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ")
        nuevo_ticket = Ticket(id_ticket, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print(f" Ticket {id_ticket} creado con éxito.")

    elif opcion == "2":
        if not tickets:
            print(" No hay tickets registrados.")
        else:
            for t in tickets:
                t.mostrar_info()

    elif opcion == "3":
        if not tickets:
            print("No hay tickets para asignar.")
        else:
            for i, t in enumerate(tickets, start=1):
                print(f"{i}. Ticket {t.id_ticket} - {t.tipo} ({t.estado})")
            num = int(input("Seleccione el número de ticket a asignar: ")) - 1

            print("\nEmpleados disponibles:")
            for i, e in enumerate(empleados, start=1):
                print(f"{i}. {e.nombre} ({e._class.name_})")
            num_emp = int(input("Seleccione el número de empleado: ")) - 1

            if 0 <= num < len(tickets) and 0 <= num_emp < len(empleados):
                pm.asignar_ticket(tickets[num], empleados[num_emp])
                empleados[num_emp].trabajar_en_ticket(tickets[num])
            else:
                print("Selecciónast e inválida.")

    elif opcion == "4":
        print("fue un gusto , hasta aqui el programa , lindo dia")
        break