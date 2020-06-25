#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". 
#Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y 
# si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".

name = input("Ingresar Nombre y Apellido: ")
nota = int(input("Ingresar Nota de Matemática: "))
nota = nota + int(input('Ingresar Nota de Literatura: '))
nota = nota + int(input('Ingresar Nota de Física: '))
promedio = nota/3

if promedio>6:
    tipo = "Aprobado."
    if promedio >9:
        tipo = tipo + " Alumno destacado."
elif promedio<4:
    tipo = "Insuficiente."
elif promedio>=4 and promedio<6:
    tipo = "A recuperatorio"


print("Nombre y Apellido: " + name)
print("Promedio: "+ str(promedio))
print(tipo)

