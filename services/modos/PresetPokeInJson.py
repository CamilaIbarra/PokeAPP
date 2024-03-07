import services.funciones.funciones_prueba as funciones_prueba

#rango de los pokemones de la primera generacion
inicio_pokemon = 0
fin_pokemon = 150

# Lista para el json de cada pokemon
#lista_pokemones = funciones_prueba.damePokemones(inicio_pokemon,fin_pokemon)["results"]

def preset1v1(p1):
    return funciones_prueba.usarArchivoCreado(p1)

def preset3v3(p1, p2, p3):
     listaPoke = [funciones_prueba.usarArchivoCreado(p1),funciones_prueba.usarArchivoCreado(p2), funciones_prueba.usarArchivoCreado(p3)]
     return listaPoke
 
def preset4v4(p1, p2, p3, p4):
     listaPoke = [funciones_prueba.usarArchivoCreado(p1),funciones_prueba.usarArchivoCreado(p2), funciones_prueba.usarArchivoCreado(p3), funciones_prueba.usarArchivoCreado(p4)]
     return listaPoke
 
def preset6v6(p1, p2, p3, p4, p5, p6):
    

     listaPoke = [funciones_prueba.usarArchivoCreado(p1),funciones_prueba.usarArchivoCreado(p2), funciones_prueba.usarArchivoCreado(p3), funciones_prueba.usarArchivoCreado(p4), 
                  funciones_prueba.usarArchivoCreado(p5), funciones_prueba.usarArchivoCreado(p6)]
     return listaPoke
