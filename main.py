from RegexToPostfix import convertExpression
from PostfixToAFN import PostifixToAFN
from AFNtoAFD import AFNtoAFD
from RegexAFD import *
from AFD import AFD
from minimizar import minimizar

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
    
    #Lista para Minimizacion de AFD
    estadosAFD = conversionAFD.estados_afd
    estados_finalesAFD = conversionAFD.estados_finales_afd
    estado_inicialesAFD = conversionAFD.estados_iniciales_afd
    simbolosAFD = conversionAFD.simbolos_afn
    afd = conversionAFD.afd

    
    # instacia de clase para Minimizacion de AFD
    minimizacion = minimizar(estadosAFD, estados_finalesAFD, 
                            estado_inicialesAFD, simbolosAFD, afd)

    # llamada al metodo para convertir a AFD
    minimizacion.reIstanciate()

    #convertir de regex a AFD
    regext = regex(exp,True)
    syntax = AFD(regext)
    
    # simulacion de string
    print('\nIngrese un string para simular si es aceptable o no en la expresión regular: ',exp)
    prueba=input("-> ")
    respuesta = syntax.simulate_string(prueba)
    print(f'\nEl string {prueba} es aceptado en la expresión regular {exp}? -> ', respuesta)

    print('\nPrograma finalizado con éxito!!')
    print('GG\'s guys and see you next time! :D')
    
    
