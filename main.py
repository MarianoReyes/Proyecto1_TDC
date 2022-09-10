from turtle import pos
from RegexToPostfix import convertExpression
from PostfixToAFN import PostifixToAFN

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

    conversionAFD = PostifixToAFN(postfix)

    conversionAFD.conversion()
