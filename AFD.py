
from Node import Node
from leaf import Leaf


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
        for x in self.nodes:
            if x.name == '#':
                self.final_state = x.position #Lo setea como final de la expresion
                break
        
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
                
            elif operator != '*' and operator != '+' and operator != '?':
                left = values.pop()
                
                if left not in self.symbols and left != 'ε' and left != '@' and left != '#':
                    self.self.symbols.append(left)
                    
            elif operator == '|': 
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
        