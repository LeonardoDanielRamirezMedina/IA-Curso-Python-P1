#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#------MANEJO DE EXCEPCIONES------

ban=True        #indicador para el ciclo while
monedero=0         #se declara el valor inicial del monedero en 0
x=0             #variable para guardar cantidad ingresada

while ban:      #el ciclo sigue mientras ban sea True
    try:                                                                            #prueba las siguientes lineas de codigo en busca de error
        print("Vienvenido al cajero Leo :D\nTu saldo es de:",monedero,"pesos")
        x=int(input("Introduce la cantidad de dinero que quieres guardar en tu cuenta: "))  #si se ingresa int sigue, sino entra except
    except ValueError:
        print("No es un numero. Introduce un numero por favor")
    else:
        monedero +=x                #suma cantidad ingresada
    finally:
        final=input("¿Quieres depositar mas dinero?  Si= S / No= N\t")      #confirmacion para seguir en el bucle while, si la respuesta es no ben toma el valor False
        if final == "N":
            print("Hasta luego")
            ban=False           #Con este cambio termina el bucle while
        else:
            print("Continuemos...")     #inicia de nuevo el ciclo