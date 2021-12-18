import os

def calificacion(notas):
    list = []
    for nota in (notas):
        list.append(notafinal(nota))
    return list

def notafinal(notas):
    redondeo = 0
    if(notas < 40):
        redondeo = notas
    else:
        cociente = int(notas/5 + 1)
        multiplo = cociente * 5
        if(multiplo - notas < 3):
            redondeo = multiplo
        else:
            redondeo = notas
    return redondeo