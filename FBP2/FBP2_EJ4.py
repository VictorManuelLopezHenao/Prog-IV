print("\tAuto Cinema\n")

valor_total_entrada = 0
cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros del vehiculo: "))

for i in range(cantidad_pasajeros):

    edad = int(input(f"Ingrese la edad del pasajero {i+1}" ))
        
    if (edad <= 3):
        valor_total_entrada += 0
    elif (edad >= 4 and edad <= 11):
       valor_total_entrada += 16.00
    elif (edad >= 50):
        valor_total_entrada += 40.00
    else:
        valor_total_entrada += 34.00

print(f"El valor total de las entradas es:  {valor_total_entrada:<10.2}")

 

    




