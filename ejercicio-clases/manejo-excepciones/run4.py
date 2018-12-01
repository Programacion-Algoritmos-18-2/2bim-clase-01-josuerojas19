try:

    objeto = Persona("René")
    objeto.setEdad(10)
    print(objeto)
    
except TypeError as e:
    print("Error tipo %s %s" % (e.__class__, e))

except ValueError as e:
    print("Error tipo %s %s" % (e.__class__, e))

except NameError as e:
    print("Error %s" % e)

except AttributeError as e:
    print("Error %s" % e)

except Exception as e:
    print("Error %s" % e)

