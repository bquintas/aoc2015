file1 = open('day2/input', 'r')
total_paper = 0
total_ribbon = 0
while True:
    line = file1.readline().strip()
    if not line:
        break
    ls, ws, hs = (line.split('x'))
    l, w, h = int(ls), int(ws), int(hs)
    smallest_size = min(l*w, l*h, w*h)
    smallest_perimeter = min(2*(l+w), 2*(l+h), 2*(w+h))
    volume = l*w*h
    surface_area = 2*l*w + 2*w*h + 2*h*l
    total_paper += (smallest_size+surface_area)
    total_ribbon += (smallest_perimeter+volume)
print(total_paper, total_ribbon)
