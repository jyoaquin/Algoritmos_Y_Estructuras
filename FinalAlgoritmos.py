# Crear un programa para gestionar estudiantes y sus calificaciones en una materia.Define una clase Estudiante que tenga los siguientes atributos:
# •	nombre (str)
# •	edad (int)
# •	notas (list de float)
# Define los siguientes métodos para la clase:
# •	agregar_nota(self, nota) - Agrega una nueva calificación al estudiante.
# •	promedio(self) - Calcula y retorna el promedio de las notas.
# •	informacion(self) - Imprime el nombre, edad y promedio del estudiante.
# Define una clase Materia que tenga los siguientes atributos:
# •	nombre (str)
# •	estudiantes (list de objetos Estudiante).
# Define los siguientes métodos para la clase Materia:
# •	agregar_estudiante(self, estudiante) - Agrega un nuevo estudiante a la lista.
# •	mostrar_estudiantes(self) - Muestra la información de todos los estudiantes.

# Agrega más métodos a las clases si es necesario, como borrar estudiantes o encontrar al estudiante con el mejor promedio.Modifica el programa para que lea los datos de entrada del usuario.Crea validaciones para asegurar que las notas estén entre 0 y 100.

class Estudiante:
    # Definición del contructor para la creacion de alumnos
    def __init__(self,nombre, edad, notas=None, promedio=None):
        self.nombre = nombre
        self.edad = edad
        self.notas = []
        self.promedio = 0
    
    # Metodos requeridos en la clase estudiantes:

    # Agrega la nota indicada al alumno, agregandolo a su list de notas
    def AgregarNota(self, nota):
        
        if nota < 100 and nota > 0:
            self.notas.append(nota)

            print("Calificación agregada correctamente!")
            print(f"cant notas : {len(self.notas)}")
        else:
            print("La calificaion indicada es inapropiada. Intente nuevamente y recuerde que las calificaciones son de 0 a 100!")

    # Calcula el promedio del estudiante y lo muestra en pantalla
    def Promedio(self):

        if len(self.notas) < 0:
            
            print("El estudiante aun no tiene calificaciones! Introduzca las calificaciones y vuelva a intentarlo ")

        else:

            self.promedio = sum(self.notas) / len(self.notas)

            print(f"El promedio de {self.nombre} es de {self.promedio}")

    # Muestra en pantalla la información del estudiante (nombre, edad y promedio)
    def Informacion(self):

        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio de notas: {self.Promedio()}")

# Declaración de la clase materia, con constructor indicando el nombre de la materia y creando la lista de estudiantes vacia
class Materia:
    def __init__(self, nombre, estudiantes=None):
        self.nombre = nombre
        self.estudiantes = []
    

    def AgregarEstudiante(self, nombre=input("Ingrese el nombre del estudiante: "), edad=input("Ingrese la edad del estudiante: ")):
        
        i = len(self.estudiantes) + 1
        self.nombreObjeto = f"estudiante{i}"
        self.estudiante1 = Estudiante(nombre, edad)
    
    def MostrarEstudiantes(self):
        for i in self.estudiantes:
            i.Informacion()


# nomMateria = input("Ingrese el nombre de la materia: ")
# materia1 = Materia("mate")

# materia1.AgregarEstudiante()

# materia1.MostrarEstudiantes()

# -------------

# nombre = input("Ingrese el nombre : ")
# edad = input("Ingrese la edad: ")
# estudiante1 = Estudiante(nombre, edad)

# estudiante1.AgregarNota(nota=float(input("Ingrese la nota del alumno: ")))

# estudiante1.AgregarNota(nota=float(input("Ingrese la nota del alumno: ")))

# estudiante1.AgregarNota(nota=float(input("Ingrese la nota del alumno: ")))

# print(estudiante1.notas)

# estudiante1.Informacion()

# estudiante1.Promedio()

# estudiante1.Informacion()
