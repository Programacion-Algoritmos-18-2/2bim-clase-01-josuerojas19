
from manejo import *

m = MiArchivo()
m2 = MiArchivoEscribir() 


lista = m.getInformacion()

lista = lista[1:6]
listaNueva = []

for linea in lista:
	linea = linea.split("|")
	linea[3] = linea[3].replace('\n', '')
	listaNueva.append(linea)

for linea in listaNueva:
	objeto = Estudiante(linea[0], int(linea[1]), int(linea[2]), int(linea[3]))
	m2.setInformacion(objeto)

m.cerrar_archivo()
m2.cerrar_archivo()

print("Proceso finalizado")


