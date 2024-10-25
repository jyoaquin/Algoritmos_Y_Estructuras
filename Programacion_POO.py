
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


class Persona():
    caminando = False
    nombre = ""
    apellido = ""

    def caminar(self):
        self.caminando = True
        print(f"Soy {self.nombre} {self.apellido} y estoy caminando!")
    
    def detener(self):
        self.caminando = False
        print(f"Soy {self.nombre} {self.apellido} y estoy detenido")


juan = Persona()
juan.nombre = input("Ingrese el nombre: ")[::-1]
juan.apellido = input("Ingrese el apellido: ")[::-1]
juan.caminar()
juan.detener()

