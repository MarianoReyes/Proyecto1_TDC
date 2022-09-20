
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
                
                
    
    return concatenacion(resultado)
    
def concatenacion(regex):
    
    return(encadenado)
