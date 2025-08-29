palabra = input("\nDigite una palabra: ")
lista_consonantes = []

for i in (palabra):
    if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        lista_consonantes.append(i)
    
print (lista_consonantes)
