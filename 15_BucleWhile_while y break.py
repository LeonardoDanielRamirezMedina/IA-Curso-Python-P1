#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#Se mostrará el uso del bucle while

x=0     #Se inicializa la variable x en 0

while x <= 20:                                  #se establece la condición para que entre el ciclo while
    x +=1                                       #el incremento por ciclo es de 1
    if x==15:                                   #si se cumple esta condicion se romperá el bucle
        print("El ciclo se rompe en x=15")      #mensaje al momento de romper el bucle
        break                                   #con break se detiene el ciclo en el valor establecido por if
    if x==4 or x==6 or x== 10:                  #se establece la condicion para aplicar el continue, saltando este valor en el ciclo
        print("Se salta el valor de x= ",x)     #se imprime el valor saltado
        continue                                #salta el valor establecido en el if
    print("El valor de x en el ciclo es: ",x)   #se imprime la posicion en el bucle
    
        
    
