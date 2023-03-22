#Funcion que calcula el digito verificador tomando los digitos anterior a este
def validarDigito(rutSinDigito):
    #Validacion a lo ingresado por parametro
    if rutSinDigito == int and len(rutSinDigito.strip()) == 7 or len(rutSinDigito.strip()) == 8:
        
        ##Lo dejo en una lista para recorrer cada letra y usar el metodo pop para tomar el ultimo
        sinDigito =list(rutSinDigito)
        resultMul=0
        n=2

        while len(sinDigito) > 0:
            numero = sinDigito.pop()
            result = int(numero) * n
            resultMul = resultMul + result
            n = n+1
            if n == 8:
                n= 2

        #Obtengo el resto entre resultado de la multiplicación y el número 11
        resulRest = resultMul % 11

        #Aquí defino el resultado final que es la resta de 11 menos el resultado de la división
        resultFinal = 11 - resulRest

        #Cuando el resultado final es 11 entonces el digito será 0
        if resultFinal  == 11:
            return str(f'{rutSinDigito}0')
        #Cuando el resultado final es 10 entonces el digito será 0
        elif resultFinal == 10:
            return str(f'{rutSinDigito}k')
        else:
            return str(f'{rutSinDigito}{resultFinal}')
        
    else:
        print('Verifique nuevamente los valores por parametro')
        

#Funcion que verifica si el rut otorgado existe
def validarRut(rut):
        
        sinDigito = rut[:-1]
        if validarDigito(sinDigito) == rut.lower():
            return True
        else:
            return False
        