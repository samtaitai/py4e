#file handler
#file = input("Enter a file name: ")
hand = open('mbox-short.txt') #not a method, but function

lst = list()
tup = list()
counts = dict()

for line in hand:
    if line.startswith('From ') is True:
        word = line.split()
        email = word[1]
        #make a list of emails
        lst.append(email) #Don't lst=lst.append(email)
        for count in lst:
            #make a histogram
            #email is key, result of method 'get' is value
            #'get' method is to return the key's value
            counts[email] = counts.get(email, 0) + 1
    else:
        continue
#multiple assignment; pull key-value pair, reverse them, put them into a new list 'tup'
for k, v in list(counts.items()):
    tup.append((v, k))
#put the biggest number(value) as first
tup.sort(reverse=True)
#print 'the most' in the orginal key(email)-value(count) form
for k, v in tup[:1]:
    print(v, k)
