lista = [3.14, "Hola Doc!", [911, "Los chicos malos"], 14, True]
tiene_sublista = False

for i in lista:
    if type(i) == list:
        print("La lista contiene una sublistas")
        tiene_sublista = True

if not tiene_sublista:
    print("La lista no contiene sublistas")
    