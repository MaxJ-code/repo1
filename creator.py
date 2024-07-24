class Part:
    def __init__(self, name, x, y, z, c):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.c = c
        
def create(parts):
    create_white(parts)
    create_red(parts)
    create_blue(parts)
    create_yellow(parts)
    create_orange(parts)
    create_green(parts)
    return parts
    
def create_white(parts):
    for part_white in range(0, 3):
        for val_y in range(0, 3):
            globals()[f'{part_white}'] = Part(f'{(part_white*3)+val_y}', part_white-1, val_y-1, -2, "white")
            parts.append(globals()[f'{part_white}'])
    return parts

def create_red(parts):
    for part_red in range(0, 3):
        for val_y in range(0, 3):
            globals()[f'{part_red}'] = Part(f'{(part_red*3)+val_y+9}', 2, part_red-1, val_y-1, "red")
            parts.append(globals()[f'{part_red}'])
    return parts

def create_blue(parts):
    for part_blue in range(0, 3):
        for val_y in range(0, 3):
            globals()[f'{part_blue}'] = Part(f'{(part_blue*3)+val_y+18}', part_blue-1, 2, val_y-1, "blue")
            parts.append(globals()[f'{part_blue}'])
    return parts

def create_yellow(parts):
    for part_yellow in range(0, 3):
        for val_y in range(0, 3):
            globals()[f'{part_yellow}'] = Part(f'{(part_yellow*3)+val_y+27}', part_yellow-1, val_y-1, 2, "yellow")
            parts.append(globals()[f'{part_yellow}'])
    return parts

def create_green(parts):
    for part_green in range(0, 3):
        for val_y in range(0, 3):
            globals()[f'{part_green}'] = Part(f'{(part_green*3)+val_y+36}', -2, part_green-1, val_y-1, "green")
            parts.append(globals()[f'{part_green}'])
    return parts

def create_orange(parts):
    for part_orange in range(0, 3):
        for val_y in range(0, 3):
            globals()[f'{part_orange}'] = Part(f'{(part_orange*3)+val_y+45}', part_orange-1, -2, val_y-1, "orange")
            parts.append(globals()[f'{part_orange}'])
    return parts







parts = []
create(parts)

for i in parts:
    print(i.name)


#    for i in range(0, 125):
#         globals()[f'p{i}'] = None
#     parts = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26]
#     x1 = -2
#     y1 = -2
#     z1 = -2
#     count = 0
#     while z1 < 2:
#         parts[count] = Part(str(count + 1), x1, y1, z1)
#         x1 += 1
#         if x1 > 1:
#             y1 += 1
#             x1 = -1
#         if y1 > 1:
#             z1 += 1
#             y1 = -1
#         count += 1