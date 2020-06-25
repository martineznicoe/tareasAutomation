#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#Nombre y apellido del comprador.
#Marca
#Puertas
#Color

#Marcas posibles y sus precios:
#Ford $100000
#Chevrolet: $120000  
#Fiat: $80000
#Por la cantidad de puertas se añade un precio: 
#2: $50000
#4: $65000
#5: $78000
#Dependiendo del color, se deben sumar:
#Blanco: $10000
#Azul: $20000
#Negro: $30000
#Deben imprimirse los datos de cada compra y el precio total.

for i in range(5):
    name = input("Ingresar Nombre y Apellido: ")
    marca = input("Elija la marca de auto (Ford) (Chevrolet) (Fiat) : ")
    puertas = input("Elija la cantidad de puertas (2), (4) o (5): ")
    color = input("Elija el color (Blanco) (Azul) (Negro): ")
    precio = 0


    if marca == 'Ford':
        precio = 100000
    elif marca == 'Chevrolet':
        precio = 120000
    elif marca == 'Fiat':
        precio = 80000

    if puertas == '2':
        precio += 50000
    elif puertas == '4':
        precio += 65000
    elif puertas == '5':
        precio += 78000

    if color == 'Blanco':
        precio += 10000
    elif color == 'Azul':
        precio += 20000
    elif color == 'Negro':
        precio += 30000

    print("Nombre y Apellido: " + name)
    print("SU COMPRA ES:")
    print("Marca = " + marca)
    print("Cantidad de puertas = " + puertas)
    print("Color = " + color)
    print("PRECIO TOTAL: $" + precio)
