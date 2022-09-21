
from turtle import st
from Node import Arbol
from leaf import Leaf
import functools
import os.path



class AFD():
    def __init__(self, regex):

        self.count = 0
        self.rounds = 1
        self.states = []
        self.symbols = []
        self.transitions = []
        self.acc_states = []
        self.init_state = None
        self.nodes = [] #Tiene el conjunto de hojas
        self.root = None
        self.id = 0
        self.final_state = None
        self.follow_pos = {}
        
        self.build_tree(regex) #Se construye el arbol con la expresion dada
        
        #Funcion que termina proceso al encontrar el simbolo 
        #que significa el final de la expresion
        for n in self.nodes:
            if n.name == '#':
                self.final_state = n.position
                break
        
        self.calculate_followpow()
        # print(self.follow_pos)
        self.create_dfa()
        self.estados=[]
        self.simbolos=[]
        for state in self.states:
            self.estados.append(state.name)
        for hoja in self.symbols:
            if isinstance(hoja, str):
                self.simbolos.append(hoja)
            else:
                pass
        if os.path.exists("afd_directo.txt"):
            print("\nArchivo AFD existente")

        else:
            with open('afd_directo.txt', 'a', encoding="utf-8") as f:
                f.write("AFD a partir de un regex -->")
                f.write("\n")
                f.write("Símbolos: "+ str(self.simbolos))
                f.write("\n")
                f.write("Estados:  " + str(self.estados))
                f.write("\n")
                f.write("Estado inicial: " + str(self.init_state))
                f.write("\n")
                # f.write("Estados de aceptación:" + str(estados_finales) )
                # f.write("\n")
                f.write("Transiciones: " + str(self.transitions))

            print("\nArchivo de AFD directo escrito con éxito")

        
    def build_tree(self,regex):
        stack =[] #guarda simbolos
        op = [] #guarda operadores
        
        for character in regex:
            if self.is_symbols(character):
                stack.append(character)
            elif character == '(':
                op.append('(')
            elif character == ')':
                last_in = self.peek_stack(op)
                while last_in is not None and last_in != '(' :
                    root = self.operate(op,stack)
                    stack.append(root)
                    last_in = self.peek_stack(op)
                op.pop()
            else:
                last_in = self.peek_stack(op)
                while last_in is not None and last_in not in '()' and self.preceding_operator(last_in, character):
                    root = self.operate(op,stack)
                    stack.append(root)
                    last_in = self.peek_stack(op)
                op.append(character)
                
        while self.peek_stack(op) is not None:
            root = self.operate(op,stack)
            stack.append(root)
        self.root=stack.pop()
        
    # Obtiene la precedencia entre dos operadores
    def preceding_operator(self, op1, op2):
        order = ['|','.','*']
        if order.index(op1) >= order.index(op2):
            return True
        else:
            return False
    #Funcion que identifica si es 'ε', letra o numero
    def is_symbols(self,character):
        symbols = 'ε'+'abcdefghijklmnopqrstuvwxyz0123456789'
        return symbols.find(character) != -1 #si no lo encuentra regresa vacio
    
    #funcion que regresa ultimo elemento del stack
    def peek_stack(self, stack):
        if stack:
            return stack[-1] #Ultimo elemento
        else:
            return None
        
    # Obtiene el ID del nodo
    def get_id(self):
        self.id = self.id + 1
        return self.id
    
    #Funcion que dependiendo si es simbolo u operador realiza un append
    # o realiza la operacion
    def operate(self,operators,values):
        operator=operators.pop()
        right = values.pop()
        left = '@'
        
        if right not in self.symbols and right != 'ε' and right !='@' and right !='#':
            self.symbols.append(right)
            
        if operator != '*' and operator != '+' and operator != '?':
            left = values.pop()
            
            if left not in self.symbols and left != 'ε' and left != '@' and left != '#':
                self.symbols.append(left)
                
        if operator == '|': 
            return self.operator_or(left, right)
        elif operator == '.': 
            return self.operator_concat(left, right)
        elif operator == '*': 
            return self.operator_kleene(right)
        
    #Funcion del operador or
    def operator_or(self,left,right):
        operator = '|'
        
        if isinstance(left, Leaf) and isinstance(right, Leaf):
            root = Leaf(operator, None, True, [left, right], left.nullable or right.nullable)
            self.nodes += [root]
            return root

        elif not isinstance(left, Leaf) and not isinstance(right, Leaf):
            id_left = None
            id_right = None
            if left != 'ε':
                id_left = self.get_id()
            if right != 'ε':
                id_right = self.get_id()

            left_leaf = Leaf(left, id_left, False, [], False)
            right_leaf = Leaf(right, id_right, False, [], False)
            root = Leaf(operator, None, True, [left_leaf, right_leaf], left_leaf.nullable or right_leaf.nullable)

            self.nodes += [left_leaf, right_leaf, root]

            return root

        elif isinstance(left, Leaf) and not isinstance(right, Leaf):
            id_right = None
            if right != 'ε':
                id_right = self.get_id()
            
            right_leaf = Leaf(right, id_right, False, [], False)
            root = Leaf(operator, None, True, [left, right_leaf], left.nullable or right_leaf.nullable)

            self.nodes += [right_leaf, root]
            return root

        elif not isinstance(left, Leaf) and isinstance(right, Leaf):
            id_left = None
            if left != 'ε':
                id_left = self.get_id()
            
            left_leaf = Leaf(left, id_left, False, [], False)
            root = Leaf(operator, None, True, [left_leaf, right], left_leaf.nullable or right.nullable)

            self.nodes += [left_leaf, root]
            return root
        
    # Operacion kleen
    def operator_kleene(self, leaf):
        operator = '*'
        if isinstance(leaf, Leaf):
            root = Leaf(operator, None, True, [leaf], True)
            self.nodes += [root]
            return root

        else:
            id_left = None
            if leaf != 'ε':
                id_left = self.get_id()

            left_leaf = Leaf(leaf, id_left, False, [], False)
            root = Leaf(operator, None, True, [left_leaf], True)
            self.nodes += [left_leaf, root]

            return root
        
    # Operacion concatenacion
    def operator_concat(self, left, right):
        operator = '.'
        if isinstance(left, Leaf) and isinstance(right, Leaf):
            root = Leaf(operator, None, True, [left, right], left.nullable and right.nullable)
            self.nodes += [root]
            return root

        elif not isinstance(left, Leaf) and not isinstance(right, Leaf):
            id_left = None
            id_right = None
            if left != 'ε':
                id_left = self.get_id()
            if right != 'ε':
                id_right = self.get_id()

            left_leaf = Leaf(left, id_left, False, [], False)
            right_leaf = Leaf(right, id_right, False, [], False)
            root = Leaf(operator, None, True, [left_leaf, right_leaf], left_leaf.nullable and right_leaf.nullable)

            self.nodes += [left_leaf, right_leaf, root]
            return root

        elif isinstance(left, Leaf) and not isinstance(right, Leaf):
            id_right = None
            if right != 'ε':
                id_right = self.get_id()
            
            right_leaf = Leaf(right, id_right, False, [], False)
            root = Leaf(operator, None, True, [left, right_leaf], left.nullable and right_leaf.nullable)

            self.nodes += [right_leaf, root]
            return root
        
        elif not isinstance(left, Leaf) and isinstance(right, Leaf):
            id_left = None
            if left != 'ε':
                id_left = self.get_id()
            
            left_leaf = Leaf(left, id_left, False, [], False)
            root = Leaf(operator, None, True, [left_leaf, right], left_leaf.nullable and right.nullable)

            self.nodes += [left_leaf, root]
            return root
        
        
    # Se realiza el calculo de followpos
    def calculate_followpow(self):
        for n in self.nodes:
            if not n.is_operator and not n.nullable:
                self.add_followpos(n.position, [])

        for n in self.nodes:
            if n.name == '.':
                c1, c2 = [*n.children]

                for i in c1.last_pos:
                    self.add_followpos(i, c2.first_pos)

            elif n.name == '*':
                for i in n.last_pos:
                    self.add_followpos(i, n.first_pos)    
    
    # Agrega un followpos
    def add_followpos(self, pos, val):
        if pos not in self.follow_pos.keys():
            self.follow_pos[pos] = []

        self.follow_pos[pos] += val
        self.follow_pos[pos] = {i for i in self.follow_pos[pos]}
        self.follow_pos[pos] = [i for i in self.follow_pos[pos]]  
        
    # Obtiene el nombre para asignarlo al nodo
    def get_name(self):
        if self.count == 0:
            self.count += 1
            return 'S' # Starting node!

        available_letters = ' ABCDEFGHIJKLMNOPQRTUVWXYZ'
        name = available_letters[self.count]
        self.count += 1

        if self.count == len(available_letters):
            self.rounds += 1
            self.count = 0

        return name * self.rounds          

    # Genera los nodos y transiciones para el AFD
    def create_dfa(self):
        s0 = self.root.first_pos
        # print(s0)
        s0_AFD = Arbol(self.get_name(), s0, True)
        self.states.append(s0_AFD)
        self.init_state = s0_AFD.name

        if self.final_state in [u for u in s0_AFD.conjunto_nodos]:
            self.acc_states.append(s0_AFD.name)

        while not self.state_is_marked():
            T = self.state_is_unmarked()
            
            T.Mark()

            for s in self.symbols:
                fp = []
                
                for u in T.conjunto_nodos:
                    if self.get_leaf(u).name == s:
                        fp += self.follow_pos[u]
                fp = {a for a in fp}
                fp = [a for a in fp]
                if len(fp) == 0:
                    continue

                U = Arbol(self.get_name(), fp, True)

                if U.id not in [n.id for n in self.states]:
                    # print(fp)
                    if self.final_state in [u for u in U.conjunto_nodos]:
                        self.acc_states.append(U.name)
                    
                    self.states.append(U)
                    # print((T.conjunto_nodos, s, U.conjunto_nodos))
                    self.transitions.append((T.name, s, U.name))
                else:
                    self.count -= 1
                    for estado in self.states:
                        if U.id == estado.id:
                            self.transitions.append((T.name, s, estado.name))
                            # print((T.conjunto_nodos, s, estado.conjunto_nodos))
                            
        
    
    # Obtiene el estado unmarked
    def state_is_unmarked(self):
        for n in self.states:
            if not n.isMarked:
                return n


     # Revisa si existe algun estado desmarcado
    def state_is_marked(self):
        marks = [n.isMarked for n in self.states]
        return functools.reduce(lambda a, b: a and b, marks)
    
    # Obtiene la hoja a traves de su nombre
    def get_leaf(self, name):
        for n in self.nodes:
            if n.position == name:
                return n
    
    # Crea las transiciones del grafo
    def create_transitions(self):
        f = {}
        for t in self.transitions:
            i, s, fi = [*t]

            if i not in f.keys():
                f[i] = {}
            f[i][s] = fi

        return f
    
    # Implementacion de Move para la simulacion
    def simulate_move(self, Nodo, symbol):
        move = None
        for i in self.transitions:
            if i[0] == Nodo and i[1] == symbol:
                move = i[2]

        return move
    
    # Simulacion de AFD
    def simulate_string(self, exp):
        start = self.init_state
        for e in exp:
            start = self.simulate_move(start, e)
            if start == None:
                return 'no'
        if start in self.acc_states:
            return 'yes'
        return 'no'

        