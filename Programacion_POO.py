
# class Persona():
#     caminando = False
#     nombre = ""
#     apellido = ""

#     def caminar(self):
#         self.caminando = True
#         print(f"Soy {self.nombre} {self.apellido} y estoy caminando!")
    
#     def detener(self):
#         self.caminando = False
#         print(f"Soy {self.nombre} {self.apellido} y estoy detenido")


# juan = Persona()
# juan.nombre = "Juan"
# juan.apellido = "Perez"
# juan.caminar()
# juan.detener()


# class Persona():
#     caminando = False
#     nombre = ""
#     apellido = ""

#     def caminar(self):
#         self.caminando = True
#         print(f"Soy {self.nombre[::-1]} {self.apellido} y estoy caminando!")
    
#     def detener(self):
#         self.caminando = False
#         print(f"Soy {self.nombre} {self.apellido} y estoy detenido")


# juan = Persona()
# juan.nombre = input("Ingrese el nombre: ")
# juan.apellido = input("Ingrese el apellido: ")[::-1]
# juan.caminar()
# juan.detener()

#Metodo constructor

# class Alumno:
#     nro_alumnos = 0


#     def __init__(self,nombre, nota):
#         self.nombre = nombre
#         self.nota = nota
#         Alumno.nro_alumnos += 1

#     def __str__(self):
#         return f"Nombre: {self.nombre} (nota: {self.nota})"
    
#     def __del__(self):
#         Alumno.nro_alumnos -= 1
#         print("Alumno dado de baja.")
#         print(f"{Alumno.nro_alumnos} legajos restantes.")

#     def mostrar_estado(self):
#         print(f"El estado de {self.nombre} es ", end="")
#         if self.nota <=4:
#             print("regular")
#         elif self.nota <= 9:
#             print("bueno")
#         else:
#             print("excelente")

# alumno1 = Alumno("Aldo López" , 8)
# alumno2 = Alumno("Juana Martin", 3)
# print(alumno1)
# print(alumno2)
# alumno1.mostrar_estado()
# alumno2.mostrar_estado()
# input("Pulse enter para salir")


#Super clase, banco-cliente

class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self,monto):
        self.monto = self.monto + monto

    def extraer(self,monto):
        self.monto = self.monto - monto
    
    def retornar(self):
        return self.monto

    def imprimir(self):
        print("{} tiene depositada la suma de {}".format(self.nombre,round(self.monto,2)))
    
class Banco:
    def __init__(self):
            self.cliente1 = Cliente(input("Ingrese el nombre del cliente N° 1: "))
            self.cliente2 = Cliente(input("Ingrese el nombre del cliente N° 2: "))
            self.cliente3 = Cliente(input("Ingrese el nombre del cliente N° 3: "))
            

    def operar(self):
        self.cliente1.depositar(float(input(f"Ingrese el monto a depositar de {self.cliente1.nombre}: ")))
        self.cliente2.depositar(float(input(f"Ingrese el monto a depositar de {self.cliente2.nombre}: ")))
        self.cliente3.depositar(float(input(f"Ingrese el monto a depositar de {self.cliente3.nombre}: ")))
        self.cliente3.extraer(float(input(f"Ingrese el monto a extraer de {self.cliente3.nombre}: ")))

    def depositos_totales(self):
        total = round(self.cliente1.retornar()+self.cliente2.retornar()+self.cliente3.retornar(),2)
        print("El total de dinero en el banco es :{}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

banco = Banco()

banco.operar()

banco.depositos_totales()
