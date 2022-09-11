'''
CLASE DEDICADA A LA CONVERSION DE UN AFN A UN AFD
'''
import pandas as pd


class AFNtoAFD():
    def __init__(self, estados_afn, transiciones_afn, estado_inicial_afn, estado_final_afn, simbolos_afn):
        self.estados_afn = estados_afn
        self.transiciones_afn = transiciones_afn
        self.estado_inicial_afn = estado_inicial_afn
        self.estado_final_afn = estado_final_afn
        self.simbolos_afn = simbolos_afn

    def conversion(self):
        print("\nAcá va el metodo de conversion de afn a afd")
