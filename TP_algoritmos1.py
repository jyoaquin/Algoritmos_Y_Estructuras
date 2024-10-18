
#1)

"""
print("El programa le pedira tres números y luego mostrara el mayor de ellos!")

num1 = int(input("Ingrese el primer número: "))

num2 = int(input("Ingrese el segundo número: "))

num3 = int(input("Ingrese el último número: "))

if num1 > num2:
    if num1 > num3:
        print(f"El primer número es el mayor: {num1}")
    else:
        print(f"El primer tercer es el mayor: {num3}")
elif num2 > num3:
    print(f"El primer segundo es el mayor: {num2}")
"""
#2)
"""
num = int(input("Ingrese un número: "))

divisores = [2 , 3 , 5 , 7]

div = True
i = 0

while div:
    if num % divisores[i] == 0:
        print(f"El número es divisible por {divisores[i]}")
        div = False
    else:
        if i == 3:
            print("El número no es divisible.")
            div = False
    
    i += 1
"""

#3)

nota = float(input("Ingrese la nota: "))

if nota > 5:
    if nota <= 6:
        print("La calificacion es Suficiente")
    elif nota <= 7:
        print("La calificacion esta Bien")
    elif nota <= 9:
        print("La calificacion es Notable")
    else:
        print("La calificacion es Sobresaliente")
else:
    if nota > 3:
        print("La calificacion es Insuficiente")
    else:
        print("La calificacion es Muy insufiente")
        