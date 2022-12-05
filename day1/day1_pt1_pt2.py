file1 = open('day1/input', 'r')
floor = 0
position = 0
basement = []
while True:
    line = file1.readline()
    if not line:
        break
    for c in line:
        position += 1
        if c == ")":
            floor -= 1
        else:
            floor += 1
        if floor == -1:
            basement.append(position)

print("Floor", floor)
print("Position", basement[0])
