#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#----se explicará como funciona la herencia de clases y de propiedades __init_ ademas de las clases y subclases

class hotel:                                              #se declara la clase principal hotel
    def __init__(datos,nombre_hotel,nombre_huesped):        #se establece que se necesitan datos iniciales
        datos.nombre_hotel = nombre_hotel                   #se guardan los atributos
        datos.nombre_huesped = nombre_huesped

    def registro(self):                             #se declara la función para mostrar los datos correspondientes a cada objeto
        print("Registro huesped:\nHotel:",self.nombre_hotel,"\nNombre huesped: ",self.nombre_huesped)

huesped1 = hotel("RIU","Leonardo Ramírez")          #se declara el objeto que pertenece a la clase hotel con sus atriobutos iniciales
huesped1.registro()                                 #el objketo huesped1 llama a la funcion registro() de la clase hotel
    
class hotelVip(hotel):                               #se declara la subclasede hotel llamada hotelVip
    def __init__(datos, nombre_hotel, nombre_huesped, tipovip):         #se establece que necesita valores iniciales
        hotel.__init__(datos,nombre_hotel, nombre_huesped)              #se heredan los valores iniciales de la clase principal hotel
        datos.tipovip= tipovip                                          #se guarda los atributos no heredados

    def registroVip(self):              #función unica de la subclase que usa dotos heredados de la clase principal
        print("\n\nRegistro huesped:\nHotel:",self.nombre_hotel,"\nNombre huesped: ",self.nombre_huesped,"\nTipo de servicio vip: ",self.tipovip)               #se muestran los datos heredados y no heredados

huesped2 = hotelVip("RIU","Eduardo Ramírez","Todo incluido")    #se crea el objeto huesped2 que pertenece a la subclase hotelVip
huesped2.registroVip()                                          #el objeto llama a la funcion registroVip()