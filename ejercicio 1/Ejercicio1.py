pj = ['Yoda' 'Luke Skywalker' 'Han Solo' 'Leia Organa' 'Darth Vader' 'Chewbacca']


def BuscarYoda(vec):
    if len(vec) == 0:
    
def resultadoBusqueda(pj, pos):
    if pos is not None:
        pos = pos - 1
        print('Yoda se encuentra en la posicion: ', pos)
    else:
        print('Yoda no se encuentra en este vector')

resultadoBusqueda(pj, pos )

def barrido(vec, pos):
    if len(vec)<=pos:
        return None
    else:
        print(vec[pos]])
        return barrido(pj, pos+1)

barrido (pj, 0)