#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este codigo se explicara como ordenar listas usando sort() y sorted() y contar elementos de listas usando len()

#-------metodo sort() y sorted()--------

menu=["Pizza", "Ensalada", "Tacos", "Atún"] #Se declara la lista "menu"
print(sorted(menu))     #Se ordena alfabeticamente la lñista de manera no permanente
print(menu[0])      #Se imprime el dato de la posicion 0 de la lista

menu.sort() #Se ordena la lista alfabeticamente de forma permanente
print(menu) #se muestra el contenido
print("Primer dato: ",menu[0])  #Se comprueba que se ordenó de forma permanente
menu.sort(reverse=True) #Se ordena alfabeticamente de manera inversa
print(menu) #Se muestra la lista
print("Primer dato: ",menu[0])  #Se comprueba que esta ordenada de forma inversa mostrando el dato 0

#------método len()--------

print("Numero de elementos en la lista: ",len(menu)) #Por medio del método len() se cuenta el numero de elemntos de la lista menu