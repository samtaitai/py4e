fhand = open('mbox-short.txt')
linelist = []
for line in fhand:
    if line.startswith('From') != True:
        continue
    else:
        piece = line.split()
        email = piece[1]
        linelist.append(email)
        print(email)
