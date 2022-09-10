# ESTE ES UN ARCHIVO DE PRUEBA NADA MAS
# ------------------------------------
from sys import implementation
import pandas as pd


class PostifixToAFN():
    def __init__(self, postfix):
        self.postfix = postfix

    def operando(self, caracter):
        if(caracter.isalpha() or caracter == "ε"):
            return True
        else:
            return False

    def conversion(self):
        simbolos = []
        postfix = self.postfix
        for i in postfix:
            if self.operando(i):
                if i not in simbolos:
                    simbolos.append(i)

        simbolos = sorted(simbolos)

        print("Símbolos: ", simbolos)

        s = []
        stack = []
        start = 0
        end = 1

        counter = -1
        c1 = 0
        c2 = 0

        # implementation del algoritmo de thompson

        for i in postfix:
            if i in simbolos:
                counter = counter+1
                c1 = counter
                counter = counter+1
                c2 = counter
                s.append({})
                s.append({})
                stack.append([c1, c2])
                s[c1][i] = c2
            elif i == '*':
                r1, r2 = stack.pop()
                counter = counter+1
                c1 = counter
                counter = counter+1
                c2 = counter
                s.append({})
                s.append({})
                stack.append([c1, c2])
                s[r2]['ε'] = (r1, c2)
                s[c1]['ε'] = (r1, c2)
                if start == r1:
                    start = c1
                if end == r2:
                    end = c2
            elif i == '.':
                r11, r12 = stack.pop()
                r21, r22 = stack.pop()
                stack.append([r21, r12])
                s[r22]['ε'] = r11
                if start == r11:
                    start = r21
                if end == r22:
                    end = r12
            else:
                counter = counter+1
                c1 = counter
                counter = counter+1
                c2 = counter
                s.append({})
                s.append({})
                r11, r12 = stack.pop()
                r21, r22 = stack.pop()
                stack.append([c1, c2])
                s[c1]['ε'] = (r21, r11)
                s[r12]['ε'] = c2
                s[r22]['ε'] = c2
                if start == r11 or start == r21:
                    start = c1
                if end == r22 or end == r12:
                    end = c2

        print(pd.DataFrame(s))
