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

if __name__ == '__main__':

    print("Número de estudiantes")
    numero_notas = int(input('Introduce las notas de los estudiantes: ').strip())
    notas = []
    for _ in range(numero_notas):
        print("Nota de cada estudiante")
        notas_dadas = int(input().strip())
        notas.append(notas_dadas)

    result = calificacion(notas)