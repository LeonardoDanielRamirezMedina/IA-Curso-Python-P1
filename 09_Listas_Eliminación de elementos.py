#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este codigo se explicará como eliminar datos almacenados en listas

#----MÉTODO del-----

materias =["Cálculo","Control", "IA", "PLC", "Economía","Inglés", "Microcontroladores", "Visión Artificial","Vibraciones mecánicas"] #Se declara la lista "materias"
del materias[0] #Se utiliza el método del psrs eliminar el dato almacenado en la posicion0 de la lista materias
print(materias) #Se imprime la lista con el dato 0 eliminado

del materias[-1]    #Se elimina el ultimo elemento de la lista
print(materias)    #Se impirme el contenido de la lista sin los datos que eliminamos

#----MÉTODO remove()-----

lista=[1,2,3,"Eliminar1",4,5,"Eliminar2",6] #Se crea la lista con nuestros datos
print("Lista completa: ",lista)        #Se imprime la lista con todos sus datos

lista.remove("Eliminar1")       #Se utiliza el metodo remove para eliminar datos de nuestra lista sin utilizar la posicion de dicho dato
lista.remove("Eliminar2")       #Se elimina el datp "Eliminmar 2" utilizando su nombre por medio de remove()
print("Lista con datos eliminados: ",lista)                    #Se imprime la lista con los datos eliminados

#----MÉTODO pop()-----

tareas=["Tarea Mate ","Tarea Geografia ", "Tarea Artes ","Tarea Circuitos "]    #Se crea la lista "tareas"
print(tareas)       #Se muestra su contenido
papelera= tareas.pop(1)     #Se elimina y almacena en otra lista el dato de la posicion 1 usando el método pop
papelera+= tareas.pop(2)        #Se elimina y almacena en la lista papelera el dato de la posicion 2 de "tareas"
print("Tareas: ",tareas)        #Contenido de la lista tareas
print("Archivos en papelera: ",papelera)    #Se muestran los datos eliminados de la lista tareas, guardados en la lista "papelera"



