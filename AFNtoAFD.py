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
        nfa = {}
        n = len(self.estados_afn)  # Enter total no. of states
        # Enter total no. of transitions/paths eg: a,b so input 2 for a,b,c input 3
        t = len(self.transiciones_afn)
