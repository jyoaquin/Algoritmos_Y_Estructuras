
class Persona():
    caminando = False
    nombre = ""
    apellido = ""

    def caminar(self, nombre, apellido):
        self.caminando = True
        print(f"Soy {nombre} {apellido} y estoy caminando!")
    
    def detener(self, nombre, apellido):
        self.caminando = False
        print(f"Soy {nombre} {apellido} y estoy detenido")


juan = Persona()
juan.nombre = "Juan"
juan.apellido = "Perez"
juan.detener(juan.nombre, juan.apellido)
juan.caminar(juan.nombre, juan.apellido)  

