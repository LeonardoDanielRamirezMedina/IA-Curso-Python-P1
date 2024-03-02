#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este codigo se explicará como utilizar listas

materias =["Cálculo","Control", "IA", "PLC", "Economía","Inglés", "Microcontroladores", "Visión Artificial","Vibraciones mecánicas"]    #Se crea la lista escribiendo cada elemento de esta entre corchetes
print("Lista materias:",materias)     #Se muestra en consola el contenido de la lista "materias" tal como está en el código
print(materias[2])  #Se imprime el contenido de la posicion 2 de la lista (cuenta desde la posicion 0)
print(materias[0])   #Se imprime el contenido de la posicion 0 de la lista

datos= ["Leonardo", 20, "CETI", 56.8]       #Podemos almacentar diferentes tipos de datos en las listas
print("Lista de datos: ", datos)

#------POSICIONES NEGATIVAS EN LAS LISTAS------

print("Materia: ",materias[-1])     #Al utilizar posiciones negativas se manda llamar a los datos ordenados de fin a inicio, aqui se imprime el ultimo elemento
print("Materia: ",materias[-2])     #Se imprime el segundo elemento de la lista de fin a inicio
