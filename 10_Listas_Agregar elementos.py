#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este codigo se explicará como agregar datos almacenados en listas

#------Método append()----

almacen=["Martillo","Pinzas","Multimetro"]  #Creamos la lista almacen con 3 wlwmwntos
almacen.append("Clavos")    #utilizando append() podemos agragar mas elementos unicamente al final de la lista (posicion 3)
almacen.append("Desarmador")    #Se agrega el elemento "Desarmador" al final de la lista (posicion 4)
print("Elementos en almacén: ",almacen)  #se muestra el contenido de la lista y los elementos agragados

#-----Método insert()-----

almacen.insert(0,"Lija")    #Usando insert() se agragan elementos en una posicion especifica, en este caso la posicion 0
almacen.insert(3,"Cinta")   #Se agraga el elemento "Cinta" en la posición 3 de la lista
print("Elementos en almacén: ",almacen)      #Se imprime contenido de la lista