

ventas = 0
ventas_total = 0
Resupuesta = ""
sucursales = ["NOA", "NEA", "pampeana", "Cuyo", "Patagonia" , "GBA"]
ventas_noas = 0
ventas_neas = 0
ventas_pampeanas = 0
ventas_cuyos = 0
ventas_patagonias = 0
ventas_gba = 0

print("--sistema de gestion de ventas--")

while Resupuesta != "no":

    ventas = int(input("Ingrese la Cantidad de Ventas: "))

    while ventas <= 0 :
        print("No valido, Ingrese otra vez")
        ventas = int(input("Ingrese la Cantidad de Ventas: "))

    print("--1. NOA")
    print("--2. NEA")
    print("--3. pampeana")
    print("--4. Cuyo")
    print("--5. Patagonia")
    print("--6. GBA")
    sucursal_ventas = int(input("Ingrese la sucursal (1-6): "))
    while sucursal_ventas < 1 or sucursal_ventas > 6:
        print("No valido, Ingrese otra vez")
        sucursal_ventas = int(input("Ingrese la sucursal (1-6): "))

    if sucursal_ventas == 1:
      ventas_noas += ventas
    elif sucursal_ventas == 2:
     ventas_neas += ventas
    elif sucursal_ventas == 3:
       ventas_pampeanas += ventas
    elif sucursal_ventas == 4:
       ventas_cuyos += ventas
    elif sucursal_ventas == 5:
       ventas_patagonias += ventas
    elif sucursal_ventas == 6:
       ventas_gba += ventas
    
    Resupuesta = input("¿Queres Seguir ingresando ventas?(si/no): ")
    while Resupuesta != "si" and Resupuesta != "no":
        print("No valido, Ingrese otra vez")
        Resupuesta = input("¿Queres Seguir ingresando ventas?(si/no): ")
    if Resupuesta == "no":
        print("Gracias por usar el sistema de gestion de ventas")
        ventas_total += ventas
        break
    else: 
       ventas_total += ventas  
        


print(f"Ventas total fueron de {ventas_total}")
print(f"La Cantidad de Ventas en la Sucursal NOA fueron {ventas_noas}")
print(f"La Cantidad de Ventas en la Sucursal NEA fueron {ventas_neas}")
print(f"La Cantidad de Ventas en la Sucursal Pampeana fueron {ventas_pampeanas}")
print(f"La Cantidad de Ventas en la Sucursal Patagonica fueron {ventas_patagonias}")
print(f"La Cantidad de Ventas en la Sucursal CUYO fueron {ventas_cuyos}")
print(f"La Cantidad de Ventas en la Sucursal GBA fueron {ventas_gba}")

if ventas_neas > 0:
    print ("Promedio total de ventas de NEA Fueron",(int((ventas_neas)/(ventas_total)*100)),"%")

if ventas_noas > 0:
    print ("Promedio total de ventas de NOA",(int((ventas_noas)/(ventas_total)*100)),"%")

if ventas_pampeanas > 0:
    print ("Promedio total de ventas de PAMPEANA",(int((ventas_pampeanas)/(ventas_total)*100)),"%")

if ventas_patagonias > 0:
    print ("Promedio total de ventas de PATAGONICA",(int((ventas_patagonias)/(ventas_total)*100)),"%")

if ventas_cuyos > 0:
    print ("Promedio total de ventas de CUYO",(int((ventas_cuyos)/(ventas_total)*100)),"%")

if ventas_gba > 0:
    print ("Promedio total de ventas de GBA",(int((ventas_gba)/(ventas_total)*100)),"%")
