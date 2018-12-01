
import codecs

class MiArchivo:

    def __init__(self):

        self.archivo = codecs.open("data/demo.csv", "r")

    def getInformacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:

    def __init__(self):

        self.archivo = codecs.open("data/demo2.csv", "a")

    def setInformacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()
