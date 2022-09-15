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
        self.simbolos_sin_e  = simbolos_afn
        self.afn = afn
        # añadimos el ε como parte de los símbolos/alfabeto
        self.simbolos_afn.append('ε')
        # lista de estado inicial de AFD
        self.e_closure = []
        
        #variables
        self.afd= None
        self.steps=[]
        self.state_index=0 #contiene qué estado tendrá una transición generada a continuación
        self.alphabet_index = 0 #alphabet_index contiene qué símbolo se utilizará para generar la siguiente transición
        self.unreachableStates = None #los estados que no se alcanzan
        self.redundantStates = None #redundantStates es la matriz de estados que se pueden combinar en un solo estado

    def NextStep():
        if (self.dfa == None): return 'initialize'
        if (self.state_index < self.dfa.states.length): return 'add_transition'

        if (!self.unreachableStates) { self.unreachableStates = self.getUnreachableStates() }
        if (self.unreachableStates.length > 0): return 'delete_state'

        if (!self.redundantStates) { self.redundantStates = self.getRedundantStates() }
        if (self.redundantStates.length > 0): return 'merge_states'
    
    """ def getUnreachableStates (tempDFA = undefined, list = []) {
        if (!tempDFA) {
            tempDFA = this.dfa.clone()
        }

        const nodesWithIncomingEdges = []

        // Iterate through all transitions and add the end nodes to the nodesWithIncomingEdges array
        for (const state of tempDFA.states) {
            for (const symbol of tempDFA.alphabet) {
                const node = tempDFA.transitions[state][symbol].join(',')

                // Don't consider nodes that have a transition back to themselves
                if (node !== state) nodesWithIncomingEdges.push(node)
            }
        }

        // The list of unreachable states are those that don't exist in the nodesWithIncomingEdges array
        // Make sure the start state is always in the final DFA by filtering it out of the resulting array
        const nodesWithoutIncomingEdges = tempDFA.states.filter(s => !nodesWithIncomingEdges.includes(s) && s !== tempDFA.startState)

        // If there were unreachable nodes, delete them and then recursively search for more
        if (nodesWithoutIncomingEdges.length > 0) {
            // Remove the nodes from the temporary DFA
            nodesWithoutIncomingEdges.forEach(n => tempDFA.removeState(n))

            // Recursively search for more unreachable nodes after deletion
            // Concat the unreachable nodes to the running list
            list = this.getUnreachableStates(tempDFA, list.concat(nodesWithoutIncomingEdges))
        }

        // Remove duplicates from the list by spreading it as a Set
        return [...new Set(list)]
    }
         """
        
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
        
