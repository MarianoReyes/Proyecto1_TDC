'''
CLASE DEDICADA A LA CONVERSION DE UN AFN A UN AFD
'''
import pandas as pd

#variables
steps=[]
state_index=0 #contiene qué estado tendrá una transición generada a continuación
alphabet_index = 0 #alphabet_index contiene qué símbolo se utilizará para generar la siguiente transición
unreachableStates = undefined #los estados que no se alcanzan
redundantStates = undefined #redundantStates es la matriz de estados que se pueden combinar en un solo estado

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
        self.e_closure = []

    def verificar_path(self, estado):
        '''
        desde el 6 pasa al 4 llega al 0 o 2 y se detiene
        '''
        for i in range(len(self.transiciones_afn)):
            if self.transiciones_afn[i][0] == estado:
                #regresar todos los estados hasta donde llego
                if self.transiciones_afn[i][1] == "ε":
                    self.e_closure.append(self.transiciones_afn[i][0])
                    self.e_closure.append(self.transiciones_afn[i][2])

    def mover(self, closure, transicion):
        estado = self.transiciones_afn[closure][transicion]
        return estado


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
        #print(afn_table.transpose())
        # estado final
        afn_final_state = self.estado_final_afn
        e_closure = []
        #print("transiciones:", self.transiciones_afn)
        '''for x in range(len(self.transiciones_afn)):

            if self.transiciones_afn[x][1] == "ε":

                if self.transiciones_afn[x][0] not in e_closure and self.transiciones_afn[x][2] not in e_closure:
                    if self.transiciones_afn[x][1] != "ε":
                        pass
                    else:
                        e_closure.append(self.transiciones_afn[x][0])
                        e_closure.append(self.transiciones_afn[x][2])'''

        x = self.estado_inicial_afn 

        # recorre todos los estados el afn
        
        # si no es un conjunto vacio el epsilon pasa
        while x <= len(afn):
            if afn[x]["ε"] != "" :
                # lista temporal del array de llegada
                lista_temp = afn[x]["ε"]
                for x in lista_temp:
                    # por cada uno en el array de llegada se añade al e?closure
                    if x not in e_closure:
                        e_closure.append(x)
                        print("A: ",sorted(e_closure))


        

        lista_estados = [e_closure]
        
