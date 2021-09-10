from tdaPila import Pila
from tdaCola import Cola


def eliminarNotificacionesFacebook(objCola):
    eliminado = 0;
    largo = objCola.tamanio()

    for i in range(0, largo):

        if objCola.en_frente()[1] == 'Facebook':
            objCola.atencion()
            largo = largo - 1
        else:
            objCola.mover_final()

def mostrarMensajesTwitterContenganPython(objCola):
    estPython = False

    for i in range(0,objCola.tamanio()):
        vector = objCola.en_frente()

        if (vector[2].find('Python') != -1) and (vector[1] == 'Twitter'):
            print(objCola.en_frente())
        
        objCola.mover_final()

def mostrarNotificacionesInstagram(objCola):
    objPila = Pila()

    for i in range(0,objCola.tamanio()):

        if (objCola.en_frente()[1] == 'Instagram'):
            objPila.apilar(objCola.en_frente())

        objCola.mover_final()
        
    while(not objPila.pila_vacia()):
        print(objPila.desapilar())



def ejercicio2():
    objCola = Cola()

    listaNotificaciones = [
                            ['', 'Facebook', ''],
                            ['', 'Twitter', ''],
                            ['', 'Twitter', 'Notificación! esto Python contiene'],
                            ['', 'Facebook', ''],
                            ['', 'Instagram', 'Notificación! esto Python contiene'],
                            ['', 'Facebook', ''],
                            ['', 'Twitter', 'Notificación! esto Python contiene'],
                            ['', 'Instagram', ''],
                            ]

    for lista in listaNotificaciones:
        objCola.arribo(lista)
        
    eliminarNotificacionesFacebook(objCola)

    mostrarMensajesTwitterContenganPython(objCola)
    print('')
    mostrarNotificacionesInstagram(objCola)

ejercicio2()

