import codecs
class Estudiante():
	def __init__(self, name, n1, n2, n3):
		self.name = name
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		
	def gettNombre(self):
		return self.name

	def promedio(self):
		self.promedio = (self.n1 + self.n2 + self.n3) / 3
		return self.promedio

class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("informacion.csv", "r")

    def getInformacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("promedios.csv", "a")


    def setInformacion(self, p):
        self.archivo.write("%s tiene un promedio de: %.2f\n" % (p.obtener_nombre(), p.obtener_promedio()))

    def cerrar_archivo(self):
        self.archivo.close()




