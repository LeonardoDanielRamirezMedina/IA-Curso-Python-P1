#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#En este codigo se explicará el uso de funciones y sus argumentos

def catalogo(marca, consola, *args):        #se crea la función catalogo con 2 argumentos obligatorios y argumentos arbitrarios
    print("Marca: "+marca)                  
    print("Consola: "+consola)                     #Se imrpímen los argumentos ingresados
    print("Juegos disponibles:\n")
    for x in args:                       #por medio del ciclo for se imprimen los argumentos arbitrarios guardados en la lista juegos
        print("Juego:"+x)

juegos=["Mario Kart","Pokémon","Zelda","Super Smash Bros"]      #lista que será utilizada como argumentos arbitrarios

catalogo("Nintendo","Switch",*juegos)       #se llama a la función y se ingresan los valores de los argumentos