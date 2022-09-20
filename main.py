from turtle import pos
from RegexToPostfix import convertExpression
from PostfixToAFN import PostifixToAFN
from AFNtoAFD import AFNtoAFD

# main del programa
if __name__ == '__main__':
    # Expresion de prueba: (b|b)*abb(a|b)*
    # Simbolo epsilon  ε
    exp = "(b|b)*abb(a|b)*"
    print("\nRegex: ", exp)

    conversion = convertExpression(len(exp))

    # llamada de funcion para convertir a postfix
    conversion.RegexToPostfix(exp)

    postfix = conversion.res
    print("\nPostfix: ", postfix)

    # instancia de clase para convertir a AFN
    conversionAFN = PostifixToAFN(postfix)
    # llamada a metodo para convertir afn
    conversionAFN.conversion()

    # listas de estados, simbolos, estado inicial, estado final y transiciones del AFN
    estados = conversionAFN.estados
    transiciones = conversionAFN.transiciones_splited
    estado_inicial = conversionAFN.e0
    estado_final = conversionAFN.ef
    simbolos = conversionAFN.simbolos
    afn = conversionAFN.afn_final

    # instacia de clase para convertir AFN a AFD
    conversionAFD = AFNtoAFD(estados, transiciones,
                             estado_inicial, estado_final, simbolos, afn)
                             
    # llamada al metodo para convertir a AFD
    conversionAFD.conversion()
