#file handler
file = input('Enter a file name: ')
handle = open(file)

lst = list()
counts = dict()
#find target line
for line in handle:
    if line.startswith('From: ') != True:
        continue
#collect email part and count
    else:
        piece = line.split()
        email = piece[1]
        lst.append(email)
        for email in lst:
            counts[email] = counts.get(email, 0) + 1

#None means no value
bigperson = None
msgcount = None
#max loop in word counter
for key, value in counts.items():
    if msgcount is None or value > msgcount:
        bigperson = key
        msgcount = value

print(bigperson, msgcount)
