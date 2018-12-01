
class Persona(object):
    
    def __init__(self, name):
        self.nombre = name
        self.edad = 0

    def setNombre(self, n):
        self.nombre = n

    def getNombre(self):
        return self.nombre

    def setEdad(self, n):
        self.edad = int(n)

    def getEdad(self):
        return self.edad

    def __str__(self):
        return "%s - %d" % (self.nombre, self.edad)
