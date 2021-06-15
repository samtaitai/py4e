#file handler
fhand = open('mbox-short.txt')
linelist = []
#find target line
for line in fhand:
    if line.startswith('From') != True:
        continue
#collect email part and make email list
    else:
        piece = line.split()
        email = piece[1]
        linelist.append(email)
print(linelist)
