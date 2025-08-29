lista_original = [1, 2, 3]
print("lista_original =", lista_original, "id =", id(lista_original))


lista_referencia = lista_original.copy()
print("lista_referencia =", lista_referencia, "id =", id(lista_referencia))


lista_referencia.append(4)

print("\nDespués de modificar lista_referencia:")
print("lista_original =", lista_original, "id =", id(lista_original))
print("lista_referencia =", lista_referencia, "id =", id(lista_referencia))
