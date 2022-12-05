file1 = open('day2/input', 'r')
total = 0
while True:
    line = file1.readline().strip()
    if not line:
        break
    ls, ws, hs = (line.split('x'))
    l, w, h = int(ls), int(ws), int(hs)
    smallest_size = min(l*w, l*h, w*h)
    surface_area = 2*l*w + 2*w*h + 2*h*l
    total += (smallest_size+surface_area)
print(total)
