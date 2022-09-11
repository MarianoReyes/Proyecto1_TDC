from turtle import pos
from RegexToPostfix import convertExpression
from PostfixToAFN import PostifixToAFN
from AFNtoAFD import AFNtoAFD

# main del programa
if __name__ == '__main__':
    # Expresion de prueba: (b|b)*abb(a|b)*
    # Simbolo epsilon  ε
    exp = "(b|b)*abb(a|b)*"
    conversion = convertExpression(len(exp))

    # llamada de funcion para convertir a postfix
    conversion.RegexToPostfix(exp)
    print("Regex: ", exp)
    postfix = conversion.res
    print("Postfix: ", postfix)

    # instancia de clase para convertir a AFN
    conversionAFN = PostifixToAFN(postfix)
    # llamada a metodo para convertir afn
    conversionAFN.conversion()

    # listas de estados y transiciones del AFN
    estados = conversionAFN.estados
    transiciones = conversionAFN.transiciones_splited

    # instacia de clase para convertir AFN a AFD
    conversionAFD = AFNtoAFD(estados, transiciones)
    # llamada al metodo para convertir a AFD
    conversionAFD.conversion()
