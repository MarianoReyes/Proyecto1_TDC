from RegexToPostfix import convertExpression
from PostfixToAFN import PostifixToAFN
from AFNtoAFD import AFNtoAFD
from RegexAFD import *
from AFD import AFD
from StringRevision import StringRevision

# main del programa
if __name__ == '__main__':
    # Expresion de prueba: (b|b)*abb(a|b)*
    # Simbolo epsilon  ε
    exp = input("\nIngrese una expresion a convertir: ")
    
    #exp = "(b|b)*abb(a|b)*"
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
    
    #convertir de regex a AFD
    regext = regex(exp,True)
    #print('\n', regext)
    
    prueba=input("\nIngrese el string para la simulacion: ")
    
    syntax = AFD(regext)
    respuesta = syntax.simulate_string(prueba)
    
    

    # instancia de clase para revisar si un string pertenece a una Regex
    verificacion = StringRevision(exp,prueba)
    print(f'\nEl string {prueba} es aceptado en la expresión regular {exp}? -> ', respuesta)
    # llamada a la verificacion de los strings
    verificacion.comprobar()
