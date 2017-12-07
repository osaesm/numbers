green = 0
white = 1
orange = 2
yellow = 3
red = 4
blue = 5

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
    newCube[white][2] = cube[orange][2]
    newCube[red][2] = cube[white][2]
    newCube[yellow][2] = cube[red][2]
    newCube[orange][2] = cube[yellow][2]
    newCube[blue] = cw(newCube[blue])
    return newCube

def blueccw(cube):
    newCube = copy(cube)
    newCube[white][2] = cube[red][2]
    newCube[orange][2] = cube[white][2]
    newCube[yellow][2] = cube[orange][2]
    newCube[red][2] = cube[yellow][2]
    newCube[blue] = ccw(newCube[blue])
    return newCube



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