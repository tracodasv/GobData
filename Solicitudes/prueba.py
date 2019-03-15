def acortarCadenas(texto="""""",caracteresPorLinea=100,variacion=5):
    limMax=caracteresPorLinea
    posicionSalto = 0
    inicioLinea = 0
    limMin = caracteresPorLinea-variacion
    bandera = 0
    nuevo_texto=""""""
    lineas=1
    if len(texto)>caracteresPorLinea:
        while bandera == 0:
            saltoLinea = texto[limMin:limMax]
            linea = texto[inicioLinea:limMax]
            if "\n" in linea:
                posicionSalto = linea.index("\n")+inicioLinea
                inicioLinea = posicionSalto + 1
                limMax = inicioLinea + caracteresPorLinea
                limMin = inicioLinea + caracteresPorLinea - variacion
                nuevo_texto=texto
                lineas += 1

            elif " " in saltoLinea :
                posicionSalto = saltoLinea.index(" ") + limMin
                texto = texto[:posicionSalto]+"\n"+texto[posicionSalto:]
                inicioLinea = posicionSalto+1
                limMax = inicioLinea + caracteresPorLinea
                limMin = inicioLinea + caracteresPorLinea - variacion
                nuevo_texto=texto
                lineas += 1

            elif " " not in saltoLinea:
                while saltoLinea.find(" ") == -1:
                     limMin = limMin-variacion
                     saltoLinea = texto[limMin:limMax]
                posicionSalto = saltoLinea.index(" ") + limMin
                texto = texto[:posicionSalto]+"\n"+texto[posicionSalto:]
                inicioLinea = posicionSalto+1
                limMax = inicioLinea + caracteresPorLinea
                limMin = inicioLinea + caracteresPorLinea - variacion
                nuevo_texto=texto
                lineas += 1

            if limMax >= len(texto): 
                bandera = 1
                return(nuevo_texto,lineas)    
        return(nuevo_texto,lineas)    
    return(texto,lineas)



def acotarCadenas(texto="""""",maxCararcteres=100,variacion=10):
    totalCaracteres = len(texto)
    limMin = maxCararcteres - variacion
    limMax = maxCararcteres
    lineas = 1
    pocisionSalto = 0
    while limMax < totalCaracteres + maxCararcteres and maxCararcteres>100:
        if totalCaracteres>maxCararcteres:
            textoInicial = texto
            salto = texto[limMin:limMax]
            pocisionSalto = int(salto.find(' '))
            while pocisionSalto == -1:
                limMin = limMin - 5
                salto = texto[limMin:limMax]
                pocisionSalto = int(salto.find(' '))
                print(pocisionSalto)
            pocisionSalto = pocisionSalto + int(limMin)
            texto = texto[:pocisionSalto]+'''
            '''+texto[pocisionSalto+1:]
            limMin = limMin + maxCararcteres
            limMax = limMin + variacion
            lineas = lineas + 1
    resultado = (texto,lineas)
    return resultado