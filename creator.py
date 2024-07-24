class Part:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

def create():
    for part_white in range(0, 9):
        globals()[f'p{part_white}'] = Part(part_white, 0, 0, 0)
        print(f'p{part_white}')
    
    
    return parts




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