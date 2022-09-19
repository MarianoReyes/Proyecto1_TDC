'''
CLASE DEDICADA A LA CONVERSION DE UN AFN A UN AFD
'''
from unittest import result
import pandas as pd



class AFNtoAFD():
    def __init__(self, estados_afn, transiciones_afn, estado_inicial_afn, estado_final_afn, simbolos_afn, afn):
        # variables necesarias para poder pasar de un afn a un afd
        self.estados_afn = estados_afn
        self.transiciones_afn = transiciones_afn
        self.estado_inicial_afn = estado_inicial_afn
        self.estado_final_afn = estado_final_afn
        self.simbolos_afn = simbolos_afn
        self.simbolos_sin_e  = simbolos_afn
        self.afn = afn
        # añadimos el ε como parte de los símbolos/alfabeto
        self.simbolos_afn.append('ε')
        # lista de estado inicial de AFD
        
        #variables
        self.afd= None
        self.steps=[]
        self.state_index=0 #contiene qué estado tendrá una transición generada a continuación
        self.alphabet_index = 0 #alphabet_index contiene qué símbolo se utilizará para generar la siguiente transición
        self.unreachableStates = None #los estados que no se alcanzan
        self.redundantStates = None #redundantStates es la matriz de estados que se pueden combinar en un solo estado
        self.reachablestates = None #losestados que son alcanzados
    
    def e_closure(self,afn):
        
        estados = self.estados_afn
        temporal=[estados] #contenedor temporal
        estados_e=[estados] #los estados que se muevan con e
        
        for x in range (len(temporal)):
            #introduce los estados que tienen el epsilon
            reachablestates = afn[x]["ε"]
            print(estados_e)
            print(temporal)
            
            for estados in reachablestates:
                if estados not in estados_e:
                    estados_e.append(estados)
                    temporal.append(estados)

            print(estados_e)
            print(temporal)
            
        print(estados_e) 
    
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
        e_closure(afn)
        
        
    
            
        
        
