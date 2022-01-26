def impares():
    valor = 1
    while True:
        yield valor
        valor += 2
def sem_from():
    for valores in [1,2,3,5,4,65]:
        yield valores
def com_from():
    yield from [1,2,3,5,4,65]
