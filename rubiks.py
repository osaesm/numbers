green = 0
white = 1
orange = 2
yellow = 3
red = 4
blue = 5

def comparee(cubeA, cubeB):
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cubeA[i][j][k] != cubeB[i][j][k]:
                    return False
    return True

def copy(cube):
    newCube = []
    for i in cube:
        face = []
        for j in i:
            row = []
            for k in j:
                row.append(k)
            face.append(row)
        newCube.append(face)
    return newCube

def cw(face):
    newFace = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(3):
        for j in range(3):
            newFace[j][2 - i] = face[i][j]
    return newFace

def ccw(face):
    newFace = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(3):
        for j in range(3):
            newFace[2 - j][i] = face[i][j]
    return newFace

def greencw(cube):
    newCube = copy(cube)
    newCube[white][0] = cube[orange][0]
    newCube[red][0] = cube[white][0]
    newCube[yellow][0] = cube[red][0]
    newCube[orange][0] = cube[yellow][0]
    newCube[green] = cw(newCube[green])
    return newCube

def greenccw(cube):
    newCube = copy(cube)
    newCube[white][0] = cube[red][0]
    newCube[orange][0] = cube[white][0]
    newCube[yellow][0] = cube[orange][0]
    newCube[red][0] = cube[yellow][0]
    newCube[green] = ccw(newCube[green])
    return newCube

def whitecw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[orange][i][0] = cube[green][2][i]
        newCube[blue][0][2 - i] = cube[orange][i][0]
        newCube[red][i][2] = cube[blue][0][i]
        newCube[green][2][i] = cube[red][2 - i][2]
    newCube[white] = cw(newCube[white])
    return newCube

def whiteccw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[green][2][i] = cube[orange][i][0]
        newCube[orange][i][0] = cube[blue][0][2 - i]
        newCube[blue][0][i] = cube[red][i][2]
        newCube[red][2 - i][2] = cube[green][2][i]
    newCube[white] = ccw(newCube[white])
    return newCube

def orangecw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[green][i][2] = cube[white][i][2]
        newCube[white][i][2] = cube[blue][i][2]
        newCube[blue][i][2] = cube[yellow][2 - i][0]
        newCube[yellow][i][0] = cube[green][2 - i][2]
    newCube[orange] = cw(newCube[orange])
    return newCube

def orangeccw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[green][i][2] = cube[yellow][2 - i][0]
        newCube[yellow][2 - i][0] = cube[blue][i][2]
        newCube[blue][i][2] = cube[white][i][2]
        newCube[white][i][2] = cube[green][i][2]
    newCube[orange] = ccw(newCube[orange])
    return newCube

def yellowcw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[red][2 - i][0] = cube[green][0][i]
        newCube[blue][2][i] = cube[red][i][0]
        newCube[orange][2 - i][2] = cube[blue][2][i]
        newCube[green][0][i] = cube[orange][i][2]
    newCube[yellow] = cw(newCube[yellow])
    return newCube

def yellowccw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[green][0][i] = cube[red][2 - i][0]
        newCube[red][i][0] = cube[blue][2][i]
        newCube[blue][2][i] = cube[orange][2 - i][2]
        newCube[orange][i][2] = cube[green][0][i]
    newCube[yellow] = ccw(newCube[yellow])
    return newCube

def redcw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[green][i][0] = cube[yellow][2 - i][2]
        newCube[yellow][i][2] = cube[blue][2 - i][0]
        newCube[blue][i][0] = cube[white][i][0]
        newCube[white][i][0] = cube[green][i][0]
    newCube[red] = cw(newCube[red])
    return newCube

def redccw(cube):
    newCube = copy(cube)
    for i in range(3):
        newCube[green][i][0] = cube[white][i][0]
        newCube[white][i][0] = cube[blue][i][0]
        newCube[blue][i][0] = cube[yellow][2 - i][2]
        newCube[yellow][i][2] = cube[green][2 - i][0]
    newCube[red] = ccw(newCube[red])
    return newCube

def bluecw(cube):
    newCube = copy(cube)
    newCube[white][2] = cube[red][2]
    newCube[orange][2] = cube[white][2]
    newCube[yellow][2] = cube[orange][2]
    newCube[red][2] = cube[yellow][2]
    newCube[blue] = ccw(newCube[blue])
    return newCube

def blueccw(cube):
    newCube = copy(cube)
    newCube[white][2] = cube[orange][2]
    newCube[red][2] = cube[white][2]
    newCube[yellow][2] = cube[red][2]
    newCube[orange][2] = cube[yellow][2]
    newCube[blue] = cw(newCube[blue])
    return newCube

def pickTurn(preMove, index):
    if index == 0:
        return greencw(preMove)
    elif index == 1:
        return greenccw(preMove)
    elif index == 2:
        return whitecw(preMove)
    elif index == 3:
        return whiteccw(preMove)
    elif index == 4:
        return orangecw(preMove)
    elif index == 5:
        return orangeccw(preMove)
    elif index == 6:
        return yellowcw(preMove)
    elif index == 7:
        return yellowccw(preMove)
    elif index == 8:
        return redcw(preMove)
    elif index == 9:
        return redccw(preMove)
    elif index == 10:
        return bluecw(preMove)
    else:
        return blueccw(preMove)

def doMoves(solve, step, compare):
    
    if comparee(solve, compare):
        return 0
    
    if step == 1:

        for a in range(12):
            if comparee(pickTurn(solve, a), compare):
                return 1

        step += 1
        return doMoves(solve, step, compare)

    if step == 2:
        for a in range(12):
            current = pickTurn(solve, a)            
            for b in range(12):
                if comparee(pickTurn(current, b), compare):
                    return 2

        step += 1
        return doMoves(solve, step, compare)

    if step == 3:
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    if comparee(pickTurn(currentB, c), compare):
                        return 3

        step += 1
        return doMoves(solve, step, compare)

    if step == 4:
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        if comparee(pickTurn(currentC, d), compare):
                            return 4
        
        step += 1
        return doMoves(solve, step, compare)

    if step == 5:
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            if comparee(pickTurn(currentD, e), compare):
                                return 5
        
        step += 1
        return doMoves(solve, step, compare)

    if step == 6:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                if comparee(pickTurn(currentE, f), compare):
                                    return 6
        
        step += 1
        return doMoves(solve, step, compare)

    if step == 7:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    if comparee(pickTurn(currentF, g), compare):
                                        return 7
        
        step += 1
        return doMoves(solve, step, compare)
    
    if step == 8:
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        if comparee(pickTurn(currentG, h), compare):
                                            return 8
                
        step += 1
        return doMoves(solve, step, compare)

    if step == 9:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            if comparee(pickTurn(currentH, i), compare):
                                                return 9
        
        step += 1
        return doMoves(solve, step, compare)

    if step == 10:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                if comparee(pickTurn(currentI, j), compare):
                                                    return 10

        step += 1
        return doMoves(solve, step, compare)

    if step == 11:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    if comparee(pickTurn(currentJ, k), compare):
                                                        return 11

        step += 1
        return doMoves(solve, step, compare)

    if step == 12:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        if comparee(pickTurn(currentK, l), compare):
                                                            return 12

        step += 1
        return doMoves(solve, step, compare)

    if step == 13:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            if comparee(pickTurn(currentL, m), compare):
                                                                return 13

        step += 1
        return doMoves(solve, step, compare)

    if step == 14:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                if comparee(pickTurn(currentM, n), compare):
                                                                    return 14

        step += 1
        return doMoves(solve, step, compare)

    if step == 15:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    if comparee(pickTurn(currentN, o), compare):
                                                                        return 15

        step += 1
        return doMoves(solve, step, compare)

    if step == 16:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        if comparee(pickTurn(currentO, p), compare):
                                                                            return 16

        step += 1
        return doMoves(solve, step, compare)

    if step == 17:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            if comparee(pickTurn(currentP, q), compare):
                                                                                return 17

        step += 1
        return doMoves(solve, step, compare)

    if step == 18:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                if comparee(pickTurn(currentQ, r), compare):
                                                                                    return 18

        step += 1
        return doMoves(solve, step, compare)

    if step == 19:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    if comparee(pickTurn(currentR, s), compare):
                                                                                        return 19

        step += 1
        return doMoves(solve, step, compare)

    if step == 20:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    currentS = pickTurn(currentR, s)
                                                                                    for t in range(12):
                                                                                        if comparee(pickTurn(currentS, t), compare):
                                                                                            return 20

        step += 1
        return doMoves(solve, step, compare)

    if step == 21:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    currentS = pickTurn(currentR, s)
                                                                                    for t in range(12):
                                                                                        currentT = pickTurn(currentS, t)
                                                                                        for u in range(12):
                                                                                            if comparee(pickTurn(currentT, u), compare):
                                                                                                return 21

        step += 1
        return doMoves(solve, step, compare)

    if step == 22:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    currentS = pickTurn(currentR, s)
                                                                                    for t in range(12):
                                                                                        currentT = pickTurn(currentS, t)
                                                                                        for u in range(12):
                                                                                            currentU = pickTurn(currentT, u)
                                                                                            for v in range(12):
                                                                                                if comparee(pickTurn(currentU, v), compare):
                                                                                                    return 22

        step += 1
        return doMoves(solve, step, compare)

    if step == 23:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    currentS = pickTurn(currentR, s)
                                                                                    for t in range(12):
                                                                                        currentT = pickTurn(currentS, t)
                                                                                        for u in range(12):
                                                                                            currentU = pickTurn(currentT, u)
                                                                                            for v in range(12):
                                                                                                currentV = pickTurn(currentU, v)
                                                                                                for w in range(12):
                                                                                                    if comparee(pickTurn(currentV, w), compare):
                                                                                                        return 23
        
        step += 1
        return doMoves(solve, step, compare)

    if step == 24:
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    currentS = pickTurn(currentR, s)
                                                                                    for t in range(12):
                                                                                        currentT = pickTurn(currentS, t)
                                                                                        for u in range(12):
                                                                                            currentU = pickTurn(currentT, u)
                                                                                            for v in range(12):
                                                                                                currentV = pickTurn(currentU, v)
                                                                                                for w in range(12):
                                                                                                    currentW = pickTurn(currentV, w)
                                                                                                    for x in range(12):
                                                                                                        if comparee(pickTurn(currentW, x), compare):
                                                                                                            return 24
        
        step += 1
        return doMoves(solve, step, compare)

    if step == 25:        
        for a in range(12):
            currentA = pickTurn(solve, a)
            for b in range(12):
                currentB = pickTurn(currentA, b) 
                for c in range(12):
                    currentC = pickTurn(currentB, c)
                    for d in range(12):
                        currentD = pickTurn(currentC, d)
                        for e in range(12):
                            currentE = pickTurn(currentD, e)
                            for f in range(12):
                                currentF = pickTurn(currentE, f)
                                for g in range(12):
                                    currentG = pickTurn(currentF, g)
                                    for h in range(12):
                                        currentH = pickTurn(currentG, h)
                                        for i in range(12):
                                            currentI = pickTurn(currentH, i) 
                                            for j in range(12):
                                                currentJ = pickTurn(currentI, j)
                                                for k in range(12):
                                                    currentK = pickTurn(currentJ, k)
                                                    for l in range(12):
                                                        currentL = pickTurn(currentK, l)
                                                        for m in range(12):
                                                            currentM = pickTurn(currentL, m)
                                                            for n in range(12):
                                                                currentN = pickTurn(currentM, n)
                                                                for o in range(12):
                                                                    currentO = pickTurn(currentN, o)
                                                                    for p in range(12):
                                                                        currentP = pickTurn(currentO, p)
                                                                        for q in range(12):
                                                                            currentQ = pickTurn(currentP, q)
                                                                            for r in range(12):
                                                                                currentR = pickTurn(currentQ, r)
                                                                                for s in range(12):
                                                                                    currentS = pickTurn(currentR, s)
                                                                                    for t in range(12):
                                                                                        currentT = pickTurn(currentS, t)
                                                                                        for u in range(12):
                                                                                            currentU = pickTurn(currentT, u)
                                                                                            for v in range(12):
                                                                                                currentV = pickTurn(currentU, v)
                                                                                                for w in range(12):
                                                                                                    currentW = pickTurn(currentV, w)
                                                                                                    for x in range(12):
                                                                                                        currentX = pickTurn(currentW, x)
                                                                                                        for y in range(12):
                                                                                                            if comparee(pickTurn(currentX, y), compare):
                                                                                                                return 25

        step += 1
        return doMoves(solve, step, compare)
    for a in range(12):
        currentA = pickTurn(solve, a)
        for b in range(12):
            currentB = pickTurn(currentA, b) 
            for c in range(12):
                currentC = pickTurn(currentB, c)
                for d in range(12):
                    currentD = pickTurn(currentC, d)
                    for e in range(12):
                        currentE = pickTurn(currentD, e)
                        for f in range(12):
                            currentF = pickTurn(currentE, f)
                            for g in range(12):
                                currentG = pickTurn(currentF, g)
                                for h in range(12):
                                    currentH = pickTurn(currentG, h)
                                    for i in range(12):
                                        currentI = pickTurn(currentH, i) 
                                        for j in range(12):
                                            currentJ = pickTurn(currentI, j)
                                            for k in range(12):
                                                currentK = pickTurn(currentJ, k)
                                                for l in range(12):
                                                    currentL = pickTurn(currentK, l)
                                                    for m in range(12):
                                                        currentM = pickTurn(currentL, m)
                                                        for n in range(12):
                                                            currentN = pickTurn(currentM, n)
                                                            for o in range(12):
                                                                currentO = pickTurn(currentN, o)
                                                                for p in range(12):
                                                                    currentP = pickTurn(currentO, p)
                                                                    for q in range(12):
                                                                        currentQ = pickTurn(currentP, q)
                                                                        for r in range(12):
                                                                            currentR = pickTurn(currentQ, r)
                                                                            for s in range(12):
                                                                                currentS = pickTurn(currentR, s)
                                                                                for t in range(12):
                                                                                    currentT = pickTurn(currentS, t)
                                                                                    for u in range(12):
                                                                                        currentU = pickTurn(currentT, u)
                                                                                        for v in range(12):
                                                                                            currentV = pickTurn(currentU, v)
                                                                                            for w in range(12):
                                                                                                currentW = pickTurn(currentV, w)
                                                                                                for x in range(12):
                                                                                                    currentX = pickTurn(currentW, x)
                                                                                                    for y in range(12):
                                                                                                        currentY = pickTurn(currentX, y)
                                                                                                        for z in range(12):
                                                                                                            if comparee(pickTurn(currentY, z), compare):
                                                                                                                return 26
    
    return 27

solved = []
solved.append([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
solved.append([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
solved.append([
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
])
solved.append([
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
])
solved.append([
    [4, 4, 4],
    [4, 4, 4],
    [4, 4, 4]
])
solved.append([
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
])

cube = []

cube.append([
    [white, orange, white],
    [yellow, green, yellow],
    [yellow, blue, orange]
    ])

cube.append([
    [green, red, blue],
    [blue, white, orange],
    [green, yellow, blue]
])

cube.append([
    [yellow, red, red],
    [white, orange, blue],
    [yellow, green, white]
])

cube.append([
    [blue, green, blue],
    [orange, yellow, white],
    [green, red, green]
])

cube.append([
    [orange, orange, red],
    [green, red, yellow],
    [yellow, blue, red]
])

cube.append([
    [white, green, red],
    [white, blue, red],
    [orange, white, orange]
])

rotated = greencw(greencw(yellowcw(redccw(whiteccw(orangecw(blueccw(solved)))))))

print(doMoves(solved, 1, cube))