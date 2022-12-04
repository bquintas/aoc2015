file1 = open('input', 'r')
floor = 0

while True:
    line = file1.readline()
    if not line:
        break
    for c in line:
        if c == ")":
            floor -= 1
        else:
            floor += 1
print(floor)
