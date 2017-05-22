laberinto = (('x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' '),
             ('x',' ','x',' ','x','x','x','x','x',' ','x',' '),
             ('x',' ','x',' ','x',' ',' ',' ',' ',' ','x',' '),
             ('x',' ','x',' ','x',' ','x',' ','x','x',' ',' '),
             (' ',' ',' ',' ','x',' ','x','x','x','x',' ',' '),
             ('x',' ','x',' ','x',' ',' ',' ','x',' ',' ','x'),
             ('x',' ','x',' ','x',' ','x',' ','x','x',' ','x'),
             ('x',' ','x',' ','x','x','x',' ','x',' ',' ','x'),
             ('x',' ',' ',' ',' ',' ',' ',' ','x','x',' ','x'),
             ('x','x','x',' ','x','x','x','x','x',' ',' ',' '),
             ('x','x','x',' ','x',' ','x','x','x',' ','x',' '),
             (' ','x','x',' ','x',' ','x',' ',' ',' ','x',' '),
             (' ','x','x',' ','x',' ','x','x','x',' ','x',' '),
             (' ','x','x',' ','x',' ',' ',' ',' ',' ',' ',' '),
             (' ',' ',' ',' ','x','x','x','x','x','x','x','x'),
             (' ','x','x',' ','x','x','x',' ','x',' ','x',' '),
             (' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' '),
             (' ','x','x',' ','x','x','x',' ','x','x','x','x')) 

pila=[]
visitados=[]
raton = (1,4)
salida = (5,3)

def imprimirLaberinto(x, raton, salida):
    for i in range(0,17):
        print("|",end="")
        for j in range(0,11):
            if (i,j) == raton:
                print("  R  ",end="")
            else:
                if (i,j) == salida:
                    print("  S  ",end="")
                else:
                    print(" ",x[i][j]," ",end="")
        print("|")
        
def push(pila,p):
    pila.append(p)
    
def pop(pila):
    try:
        pila.pop()
    except:
        print("Pila vacía")
        
def tos(pila):
    return pila[len(pila)-1]
    

def visitado(pos):
    return pos in visitados

def camino(pos):
    if laberinto[pos[0]][pos[1]] == " ":
        return True
    else:
        return False
                    
def movimiento(raton):
    pos = (raton[0] - 1,raton[1])
    if (camino(pos) and visitado(pos)==False):
        visitado.append(pos)
        return pos
    pos = (raton[0] + 1, raton[1])
    if (camino(pos) and visitado(pos)==False):
        visitado.append(pos)
        return pos
    pos = (raton[0], raton[1] + 1)
    if (camino(pos) and visitado(pos)==False):
        visitado.append(pos)
        return pos
    pos = (raton[0], raton[1] - 1)
    if (camino(pos) and visitado(pos)==False):
        visitado.append(pos)
        return pos
    return ()
        

def main():
    imprimirLaberinto(laberinto, raton, salida)

    
main()