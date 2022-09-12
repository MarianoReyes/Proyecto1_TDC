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
        afn = self.afn
        numero_estados = len(self.estados_afn)
        numero_transiciones = len(self.transiciones_afn)

        # print(afn)
        afn_table = pd.DataFrame(afn)
        print(afn_table)
        # estado final
        afn_final_state = self.estado_final_afn
        ###################################################

        # todos los estados nuevos creados para el afd
        new_states_list = []  
        # afd generado
        afd = {}  
        # conatins all the states in afn plus the states created in afd are also appended further
        keys_list = (x[0] for x in afn)
        # list of all the paths eg: [a,b] or [0,1]
        path_list = (x[2] for x in afn)

        ###################################################

        # Computing first row of afd transition table

        afd[keys_list[0]] = {}  # creating a nested dictionary in afd
        for y in range(numero_transiciones):
            # creating a single string from all the elements of the list which is a new state
            var = "".join(afn[keys_list[0]][path_list[y]])
            # assigning the state in afd table
            afd[keys_list[0]][path_list[y]] = var
            if var not in keys_list:  # if the state is newly created
                # then append it to the new_states_list
                new_states_list.append(var)
                # as well as to the keys_list which contains all the states
                keys_list.append(var)

        ###################################################

        # Computing the other rows of afd transition table

        # consition is true only if the new_states_list is not empty
        while len(new_states_list) != 0:
            # taking the first element of the new_states_list and examining it
            afd[new_states_list[0]] = {}
            for _ in range(len(new_states_list[0])):
                for i in range(len(path_list)):
                    temp = []  # creating a temporay list
                    for j in range(len(new_states_list[0])):
                        # taking the union of the states
                        temp += afn[new_states_list[0][j]][path_list[i]]
                    s = ""
                    # creating a single string(new state) from all the elements of the list
                    s = s.join(temp)
                    if s not in keys_list:  # if the state is newly created
                        # then append it to the new_states_list
                        new_states_list.append(s)
                        # as well as to the keys_list which contains all the states
                        keys_list.append(s)
                    # assigning the new state in the afd table
                    afd[new_states_list[0]][path_list[i]] = s

            # Removing the first element in the new_states_list
            new_states_list.remove(new_states_list[0])

        print("\nafd :- \n")
        print(afd)  # Printing the afd created
        print("\nPrinting afd table :- ")
        afd_table = pd.DataFrame(afd)
        print(afd_table.transpose())

        afd_states_list = list(afd.keys())
        afd_final_states = []
        for x in afd_states_list:
            for i in x:
                if i in afn_final_state:
                    afd_final_states.append(x)
                    break

        # Printing Final states of afd
        print("\nFinal states of the afd are : ", afd_final_states)

