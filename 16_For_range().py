#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#Ejemplo de uso del ciclo for

colores=("azul","rojo","verde","amarillo","blanco","negro")     #se crea la tupla colores
for x in colores:                   #se utiliza el ciclo for que recorerá todas las posiciones de la tupla colores
    if x == "amarillo":             #al igual que en el bucle while se puede utilizar continue por medio de un if
        continue                #se salta la posicion establecida
    print("El color es: "+x+".")                    #se imprime el contenido de la tup´la en la posicion x

else:
    print("termina el ciclo for")       #se indica cuendo el bucle termina

print("\n")

for x in range(7,700,100):          #ciclo for que inicia en 7, termina en 700 y avanza de 100 en 100 establecido en range()
    print(x)                        #se imprime el valor de x en cada punto del ciclo
else:
    print("termina el ciclo for")       #se indica el fin del ciclo for