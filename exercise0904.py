file = input('Enter a file name: ')
handle = open(file)

lst = list()
counts = dict()
for line in handle:
    if line.startswith('From: ') != True:
        continue
    else:
        piece = line.split()
        email = piece[1]
        lst.append(email)
        for email in lst:
            counts[email] = counts.get(email, 0) + 1

bigperson = None
msgcount = None
for key, value in counts.items():
    if msgcount is None or value > msgcount:
        bigperson = key
        msgcount = value

print(bigperson, msgcount)
