#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#----Se explicará el uso de las clases-----
class compras():            #se decclara la clase vacia compras() y se salta usando pass
    pass

class agencia:          #se declara la clase agencia
    def __init__(datos,marca, nombre, precio):          #con __init__ se establece que neustra clase debe tener valores iniciales
        datos.marca = marca                         #se guarda el atributo marca
        datos.nombre = nombre                         #se guarda el atributo nombre
        datos.precio = precio                         #se guarda el atributo precio

    def venta(car):             #se declara la función venta
        print("Se ha vendido el carro: "+car.marca,car.nombre,"a",car.precio,"pesos.")  #esta funcion imprime los atributos del objeto en este formato

carro1=agencia("Honda","Civic","450000")        #se introducen los valores iniciales para poder usar las funciones de la clase agencia
carro2=agencia("Ford","Mustang","800000")       #se introducen valores inicales del objeto carro2
carro1.venta()                  #el objeto carro1 llama a la funcion venta
carro2.venta()                  #el objeto carro2 llama a la funcion venta

carro1.nombre="Accord"          #de esta manera se modifica un atributo del objeto carro1
carro1.venta()              #se muestran los datos del objeto por medio de la funcion vemta()

del carro2.precio       #de esta manera se elimina el atributo precio de carro2
del carro2              #de esta manera se elimina por completo el objeto carro2