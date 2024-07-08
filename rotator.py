import numpy as np

def sort(parts, axis, slot):
    out = []
    for item in parts:
        if axis == "x":
            if item.x == slot:
                out.append(item)
        if axis == "y":
            if item.y == slot:
                out.append(item)
        if axis == "z":
            if item.z == slot:
                out.append(item)
    return out

def calc(const, pfr, axis):
    if axis == "x":
        a = const[0]
    if axis == "y":
        a = const[1]
    if axis == "z":
        a = const[2]    
    for part in pfr:
        print(part.name, part.x, part.y, part.z)
        b = np.array([part.x, part.y, part.z])
        c = np.array(a * b)
        c = np.array([c[0][0]+c[0][1]+c[0][2], c[1][0]+c[1][1]+c[1][2], c[2][0]+c[2][1]+c[2][2]])
        part.x = c[0]
        part.y = c[1]
        part.z = c[2]
        print(part.name, part.x, part.y, part.z)
    




def rotate(parts, axis, slot):     #pfr = parts for rotation       #rp = rotated parts
    x = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
    ])
    y = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ])
    z = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ])
    const = [x, y, z]
    pfr = sort(parts, axis, slot)
    rp = calc(const, pfr, axis)
    return parts
