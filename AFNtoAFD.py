'''
CLASE DEDICADA A LA CONVERSION DE UN AFN A UN AFD
'''
import pandas as pd


class AFNtoAFD():
    def __init__(self, estados_afn, transiciones_afn, estado_inicial_afn, estado_final_afn, simbolos_afn, afn):
        # variables necesarias para poder pasar de un afn a un afd
        self.estados_afn = estados_afn
        self.transiciones_afn = transiciones_afn
        self.estado_inicial_afn = estado_inicial_afn
        self.estado_final_afn = estado_final_afn
        self.simbolos_afn = simbolos_afn
        self.afn = afn
        # añadimos el ε como parte de los símbolos/alfabeto
        self.simbolos_afn.append('ε')

    def conversion(self):
        print("\nConvirtiendo de AFN a AFD...")
        #afn = self.afn
        numero_estados = len(self.estados_afn)
        numero_transiciones = len(self.transiciones_afn)

        #se asignan valores de nuevo al afn
        afn = {}                                 
        for estado in range(numero_estados):  
            afn[estado] = {} 
            reaching_state = []
            for j in range(len(self.simbolos_afn)):
                path = self.simbolos_afn[j]
                for j in range(numero_transiciones):               
                    reaching_state = [x[2] for x in self.transiciones_afn if x[0] == estado and x[1] == path]                 
                    afn[estado][path] = reaching_state   

        print(afn)
        afn_table = pd.DataFrame(afn)
        print(afn_table.transpose())
        # estado final
        afn_final_state = self.estado_final_afn
        