#file handler
file = input('Enter a file name: ')
handle = open(file)

lst = list()
counts = dict()
#find target line
for line in handle:
    if line.startswith('Author: ') != True:
        continue
    else:
#collect only email part
        piece = line.split()
        email = piece[1]
        lst.append(email)
#count each email
        for email in lst:
            counts[email] = counts.get(email, 0) + 1

print(counts)
