# Crear la lista original
lista_original = [1, 2, 3]
print("lista_original =", lista_original, "id =", id(lista_original))

# Crear una copia de la lista
lista_referencia = lista_original.copy()
print("lista_referencia =", lista_referencia, "id =", id(lista_referencia))

# Modificar la copia
lista_referencia.append(4)

# Imprimir ambas listas
print("\nDespués de modificar lista_referencia:")
print("lista_original =", lista_original, "id =", id(lista_original))
print("lista_referencia =", lista_referencia, "id =", id(lista_referencia))
