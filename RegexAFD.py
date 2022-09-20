
def regex(expresion, isAFD=False):
    first=[]
    regex_list=[]
    last_index = 0
    i=0
    
    SpecialCases = {
        'positive_closure_group':')+',
        'null_check_group':')?',
        'positive_closure':'+',
        'null_check':'?',
    }
    
    #Primer caso especial 
    if expresion.find(SpecialCases['positive_closure_group']) != -1:
        while i < len(expresion):
            if expresion[i] == '(':
                first.append(expresion[i]) #guarda index
                
            if expresion[i] == ')'and i < len(expresion) -1 : #la posicion actual
                regex_list.append(expresion[i])
                
                if expresion[i+1] == '+': #Para ver si el siguiente elemento es del positive group
                    last_index= i+1 #la siguiente posicion
                    regex_list.append('*')
                    regex_list.append(expresion[first.pop(): last_index])
                    i=i+1
                else:
                    first.pop()
            else:
                regex_list.append(expresion[i]) #si no es el cierre del parentesis lo agrega a la lista
            
            i=i+1 #cambio de i 
            
    #Segundo caso especial
    if expresion.find(SpecialCases['null_check_group']) != -1:
        while i < len(expresion):
            if expresion[i] == '(':
                first.append(i)                        

            if expresion[i] == ')':
                regex_list.append(expresion[i])  # pos actual
                if expresion[i + 1] == '?':     #si la siguiente posicion es ?
                    last_index = i + 1
                    regex_list.append('|')
                    regex_list.append('ε')
                    regex_list.append(')')
                    regex_list.insert(first[-1], '(')
                    i = i + 1
                else:
                    first.pop()

            else:
                regex_list.append(expresion[i])
            i += 1

        expresion = ''.join(regex_list)

    resultado = expresion
    
     #Tercer caso especial
    if expresion.find(SpecialCases['positive_closure']) != -1:
        while resultado.find(SpecialCases['positive_closure']) != -1:
            i = resultado.find('+')
            symbol = resultado[i - 1]

            resultado = resultado.replace(symbol + '+', '(' + symbol + '*' + symbol + ')')

    #Cuarto caso especial
    if expresion.find(SpecialCases['null_check']) != -1:
        while resultado.find(SpecialCases['null_check']) != -1:
            i = resultado.find('?')
            symbol = resultado[i - 1]

            resultado = resultado.replace(symbol + '?', '(' + symbol + '|' + 'ε' + ')')
                
                
    if(isAFD == True):
        final_regex = '(' + final_regex + ')#'
        
    return concatenacion(resultado)
    
def concatenacion(regex):
    valid_operators = ['(','*','|','?','+']
    encadenado = ''
    i = 0
    
    while i < len(regex):
        if i+1 >= len(regex):
            encadenado += regex[-1]
            break
        if regex[i] == '*' and regex[i+1] != ')' and not (regex[i+1] in valid_operators):
            encadenado += regex[i]+'.'
        elif regex[i] == '*' and regex[i+1] == '(':
            encadenado += regex[i]+'.'
        elif regex[i] == '?' and regex[i+1] != ')' and not (regex[i+1] in valid_operators):
            encadenado += regex[i]+'.'
        elif regex[i] == '?' and regex[i+1] == '(':
            encadenado += regex[i]+'.'
        elif not (regex[i] in valid_operators) and regex[i+1] == ')':
            encadenado += regex[i]
        elif (not (regex[i] in valid_operators) and not (regex[i+1] in valid_operators)) or (not (regex[i] in valid_operators) and (regex[i+1] == '(')):
            encadenado += regex[i]+'.'
        else:
            encadenado += regex[i]
        i += 1
        
    return encadenado
    
