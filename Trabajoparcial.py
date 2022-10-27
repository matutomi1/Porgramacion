
def agregarElemento(lista, elemento):
  lista.append(elemento)

listaglobal = []

def imprimirCancion(elemento):
  print("Nombre: " + elemento["nombre"])
  print("Artista: " + elemento["artista"])
  print("Letra: " + elemento["letra"])

def imprimirLista(lista): 
  for i in range(len(lista)):
    imprimirCancion(lista[i])
    print("-------------------")

agregarElemento(listaglobal, {"nombre": "Bandoleros", "artista": "Don omar", "letra": "Yo Tego Calderon, Don Omar, los bandoleros Aunque digan que soy Un bandolero donde voy"})
agregarElemento(listaglobal, {"nombre": "Ella y yo", "artista": "Don omar", "letra": "Go And another one That's right Go Dominicans Boricuas Hands upIn their feet, everybody come on"})
agregarElemento(listaglobal, {"nombre": "Despacito", "artista": "Luis fonsi", "letra": "Ay Fonsi, DYOh, oh no, oh no (oh) Hey yeahDiridiri, dirididi DaddyGo!"})
agregarElemento(listaglobal, {"nombre": "Gasolina", "artista": "Daddy Yankee", "letra": "Oh Oh Oh Oh Oh Who's this? (Oh) Da-ddy Yan-kee (oh, oh)"})
agregarElemento(listaglobal, {"nombre": "Llamado de emergencia", "artista": "Daddy Yankee", "letra": "Atencion a todas las unidades Llamado de emergencia del sistema 911 Hombre moribundo con aparente ataque cardíaco"})


def buscarElemento(lista, elemento):
  return elemento in lista






def buscarCancion(devolverPos = False):
  cancion = ''
  pos = ''
  nombreCancion = input('Ingrese el nombre de la cancion: ')
  for i in range(len(listaglobal)): # i --> 0, 1, 2
    if listaglobal[i]["nombre"] == nombreCancion: 
      cancion = listaglobal[i]
      pos = i
  if cancion != '': 
    imprimirCancion(cancion)
  else:
    print("No se ha encontrado la cancion") 
  if (devolverPos == False): 
   return cancion
  else:
    return pos 

print(listaglobal[0]['nombre'])

def opcionesMenu(elecUser):
  if elecUser == '1': # agregar
    artista = input('Ingrese artista: ')
    cancion = input('Ingrese nombre de la cancion: ')
    letra = input('Ingrese letra: ')
    agregarElemento(listaglobal, {"nombre": cancion, "artista": artista, "letra": letra})
    pos = int(len(listaglobal)-1)
    imprimirCancion(listaglobal[pos])
    textoMenu()
  elif elecUser == '2': # buscar
    buscarCancion()

    textoMenu()
  elif elecUser == '3': # modificar
    pos = buscarCancion(True)
    if pos == '':
      textoMenu()
    nuevoNombre = input('Ingrese el nuevo nombre: ')
    listaglobal[pos]['nombre'] = nuevoNombre
    nuevoArtista = input('Ingrese el nuevo artista: ')
    listaglobal[pos]['artista'] = nuevoArtista
    nuevaLetra = input('Ingrese la nueva letra: ')
    listaglobal[pos]['letra'] = nuevaLetra
    imprimirCancion(listaglobal[pos])
    textoMenu()
  elif elecUser == '5':
    print('salir')
  elif elecUser == '4':  
    imprimirLista(listaglobal)
    textoMenu()
  else:
    print('opcion incorrecta')
    textoMenu()


def textoMenu():
  print('opcion 1 ingresar')
  print('opcion 2 buscar')
  print('opcion 3 modificar')
  print('opcion 4 imprimir lista')
  print('opcion 5 salir')
  eleccion = input()
  opcionesMenu(eleccion)


textoMenu()
 