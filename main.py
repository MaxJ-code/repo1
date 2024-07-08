import numpy as np

class Part:
  def __init__(self, name, x, y, z):
    self.name = name
    self.x = x
    self.y = y
    self.z = z


def create():
  p0 = None
  p1 = None
  p2 = None
  p3 = None
  p4 = None
  p5 = None
  p6 = None
  p7 = None
  p8 = None
  p9 = None
  p10 = None
  p11 = None
  p12 = None
  p13 = None
  p14 = None
  p15 = None
  p16 = None
  p17 = None
  p18 = None
  p19 = None
  p20 = None
  p21 = None
  p22 = None
  p23 = None
  p24 = None
  p25 = None
  p26 = None
  parts = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26]
  x1 = -1
  y1 = -1
  z1 = -1
  count = 0
  while z1 < 2:
    parts[count] = Part(str(count), x1, y1, z1)
    x1 += 1
    if x1 > 1:
      y1 += 1
      x1 = -1
    if y1 > 1:
      z1 += 1
      y1 = -1
    count += 1
  print(count)
  return parts

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

#def calc(pfr, direction):




def rotate(parts, axis, slot, direction):
  #pfr = parts for rotation
  #rp = rotated parts
  pfr = sort(parts, axis, slot)
  rp = calc(pfr, direction)
  return parts







a_matrix = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
b_matrix = np.array([[0], [1], [0]])
c_matrix = np.array(a_matrix*b_matrix)
print(c_matrix)


parts = create()

axis = "x"
slot = 1
direction = "l"
pfr = rotate(parts, axis, slot, direction)



for coor in pfr:
  print(coor.name)
