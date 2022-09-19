import sys

class PLF:
    def __init__(self):

        args = sys.argv

        validActions = ["minimizar", "afd", "validar", "complemento",
                        "potencia", "kleene", "aceptarVacia", "noAceptarVacia",
                        "union", "concatenacion", "interseccion"]

        if (len(args) < 2) or (args[1] not in validActions):
            print ("Tienes que ingresar una accion valida.")
            sys.exit()

        action = args[1]

        if action == "minimizar":
            return self._minimizar(args)

    #Metodo que lanza el proceso de minimizacion de un AFD
    def _minimizar(self, args):
        # Verificamos que tenemos todos los parametros necesarios
        if (len(args) < 4):
            print ("El uso del programa debe ser: %s %s <archivo de datos> <archivo de resultado>" % (args[0], args[1]))
            sys.exit()

        dataFile = args[2]
        resultFile = args[3]

        # Instanciamos un AF
        af = AF()

        # Cargamos el AF desde el archivo
        self._loadFromFile(af, dataFile)

        # Ejecutamos la minimizacion
        af.minimize()

        # Escribimos el AD minimizado en un archivo
        self._writeOnFile(af, resultFile)

        print ("Minimizacion terminada correctamente, el AFD de resultado esta en: %s" % (resultFile))
