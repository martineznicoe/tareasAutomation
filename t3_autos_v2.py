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

#####

#1-Ya no sabemos cuantos clientes tendremos, 
#2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3-Lo mismo con la cantidad de puertas y los colores.
#4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5-Si la cantidad de clientes fue:
#--5.1: 0 a 5 personas no hay descuento
#--5.2: 6 a 10 personas: hay un descuento del 10%
#--5.3: 11 a 50 personas: hay un descuento del 15%
#--5.4: Más de 50 personas: El descuento es del 18%
#6-Solo se va a mostrar que se vendió al final del programa
a="s"
numero_pedido=0
autos = {'a':'Ford', 'b':'Chevrolet', 'c':'Fiat'}
puertas = {'2':'2', '4':'4', '5':'5'}
color = {'bl':'Blanco', 'az':'Azul', 'ne':'Negro'}
pedidos = {}

def calculo_precio():
    precio=0
    if pedidos[str(numero_pedido)+"a"] == 'Ford':
        precio = 100000
    elif pedidos[str(numero_pedido)+"a"] == 'Chevrolet':
        precio = 120000
    elif pedidos[str(numero_pedido)+"a"] == 'Fiat':
        precio = 80000

    if pedidos[str(numero_pedido)+"p"] == '2':
        precio += 50000
    elif pedidos[str(numero_pedido)+"p"] == '4':
        precio += 65000
    elif pedidos[str(numero_pedido)+"p"] == '5':
        precio += 78000

    if pedidos[str(numero_pedido)+"c"] == 'Blanco':
        precio += 10000
    elif pedidos[str(numero_pedido)+"c"] == 'Azul':
        precio += 20000
    elif pedidos[str(numero_pedido)+"c"] == 'Negro':
        precio += 30000

    pedidos[str(numero_pedido)+"costo"]=precio

def calculo_precio_final():
    precio_final=0
    for i in range(numero_pedido):
        i+=1
        precio_final+=int(pedidos[str(i)+"costo"])
    if numero_pedido > 50:
        precio_final-=precio_final *18/100
        return precio_final
    elif numero_pedido >10 and numero_pedido<=50:
        precio_final-=precio_final *15/100
        return precio_final
    elif numero_pedido >5 and numero_pedido<=10:
        precio_final-=precio_final *10/100
        return precio_final
    return precio_final
    
#Input de ingreso de pedidos
while a == "s":
    numero_pedido+=1
    verif = "nook"
    pedidos[str(numero_pedido)+"n"]=input("Ingresar Nombre y Apellido: ")
    
    while verif == "nook":
        ans=input("Elija la marca de auto (a) Ford (b) Chevrolet (c) Fiat : ")
        if ans in autos.keys():
            pedidos[str(numero_pedido)+"a"]=autos[str(ans)]
            verif = "ok"

    verif="nook"
    while verif == "nook":
        ans=input("Elija la cantidad de puertas (2), (4) o (5): ")
        if ans in puertas.keys():
            pedidos[str(numero_pedido)+"p"]=puertas[str(ans)]
            verif = "ok"

    verif="nook"
    while verif == "nook":
        ans=input("Elija el color (bl) Blanco (az) Azul (ne) Negro: ")
        if ans in color.keys():
            pedidos[str(numero_pedido)+"c"]=color[str(ans)]
            verif = "ok"

    verif="nook"
    while verif == "nook":
        ans = input("¿Quiere cargar un nuevo pedido? (s) Si (n) No: ")
        if ans == "s":
            a=ans
            verif = "ok"
        elif ans == "n":
            a=ans
            verif = "ok"
        else:
            verif="nook"
    calculo_precio()


#Imprime los datos de los pedidos ingresados
#Calcula al final el precio total de los pedidos con el descuento incluido en el caso que cumpla las condiciones.
for i in range(numero_pedido):
    i+=1
    print("PEDIDO N°"+str(i))
    print("Nombre y Apellido: "+pedidos[str(i)+"n"])
    print("Marca: "+pedidos[str(i)+"a"])
    print("Cantidad de puertas: "+pedidos[str(i)+"p"])
    print("Color: "+pedidos[str(i)+"c"])
    print("Precio: $"+str(pedidos[str(i)+"costo"]))
    print("<------>")
print("PRECIO TOTAL: $"+str(calculo_precio_final()))
print("<<--FIN DE PEDIDOS-->>")

    
