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

        afn_final = []
        stack = []
        start = 0
        end = 1

        counter = -1
        c1 = 0
        c2 = 0

        estados = []
        estados_list = []
        e0 = 0
        ef = None
        transiciones = []
        transiciones_splited = []

        # implementation del algoritmo de thompson

        for i in postfix:
            # si es un simbolo
            if i in simbolos:
                counter = counter+1
                c1 = counter
                if c1 not in estados:
                    estados.append(c1)
                counter = counter+1
                c2 = counter
                if c2 not in estados:
                    estados.append(c2)
                afn_final.append({})
                afn_final.append({})
                stack.append([c1, c2])
                afn_final[c1][i] = c2
                transiciones_splited.append([c1, i, c2])
            # si es un kleene
            elif i == '*':
                r1, r2 = stack.pop()
                counter = counter+1
                c1 = counter
                if c1 not in estados:
                    estados.append(c1)
                counter = counter+1
                c2 = counter
                if c2 not in estados:
                    estados.append(c2)
                afn_final.append({})
                afn_final.append({})
                stack.append([c1, c2])
                afn_final[r2]['ε'] = (r1, c2)
                afn_final[c1]['ε'] = (r1, c2)
                if start == r1:
                    start = c1
                if end == r2:
                    end = c2
                transiciones_splited.append([r2, "ε", r1])
                transiciones_splited.append([r2, "ε", c2])
                transiciones_splited.append([c1, "ε", r1])
                transiciones_splited.append([c1, "ε", c2])
            # si es una concatenacion
            elif i == '.':
                r11, r12 = stack.pop()
                r21, r22 = stack.pop()
                stack.append([r21, r12])
                afn_final[r22]['ε'] = r11
                if start == r11:
                    start = r21
                if end == r22:
                    end = r12
                transiciones_splited.append([r22, "ε", r11])

            # si es un or
            elif i == "|":
                counter = counter+1
                c1 = counter
                if c1 not in estados:
                    estados.append(c1)
                counter = counter+1
                c2 = counter
                if c2 not in estados:
                    estados.append(c2)
                afn_final.append({})
                afn_final.append({})
                r11, r12 = stack.pop()
                r21, r22 = stack.pop()
                stack.append([c1, c2])
                afn_final[c1]['ε'] = (r21, r11)
                afn_final[r12]['ε'] = c2
                afn_final[r22]['ε'] = c2
                if start == r11 or start == r21:
                    start = c1
                if end == r22 or end == r12:
                    end = c2
                transiciones_splited.append([c1, "ε", r21])
                transiciones_splited.append([c1, "ε", r11])
                transiciones_splited.append([r12, "ε", c2])
                transiciones_splited.append([r22, "ε", c2])

        # print(afn_final)
        df = pd.DataFrame(afn_final)
        for i in range(len(transiciones_splited)):
            transiciones.append(
                "(" + str(transiciones_splited[i][0]) + " - " + str(transiciones_splited[i][1]) + " - " + str(transiciones_splited[i][2]) + ")")
        transiciones = ', '.join(transiciones)

        for i in range(len(estados)):
            if i == len(estados)-1:
                ef = i
            estados_list.append(str(estados[i]))
        estados_list = ", ".join(estados_list)

        with open('afn_regex.txt', 'a', encoding="utf-8") as f:
            string_afn = df.to_string()

            f.write("AFN  a partir de la Expresión Regular-->")
            f.write("\n")
            f.write("Símbolos: "+', '.join(simbolos))
            f.write("\n")
            f.write("Estados:  " + str(estados_list))
            f.write("\n")
            f.write("Estado inicial: { " + str(e0) + " }")
            f.write("\n")
            f.write("Estados de aceptación: { " + str(ef) + " }")
            f.write("\n")
            f.write("Transiciones: " + str(transiciones))
            f.write("\n")
            f.write(string_afn)
