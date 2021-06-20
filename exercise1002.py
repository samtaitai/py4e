#file = input("Enter a file name: ")
hand = open('mbox-short.txt') #not a method, but function

lst = list()
tup = list()
counts = dict()

for line in hand:
    if line.startswith('From ') is True:
        word = line.split()
        piece = word[5]
        timepart = piece.split(':')
        time = timepart[0]
        lst.append(time)
        #make 'counts' dictionary from 'lst' list
        for count in lst:
            counts[time] = counts.get(time, 0) + 1
    else:
        continue
#flip them
for k, v in list(counts.items()):
    tup.append((v, k))
#now count is key, time is value
#Python compare numbers in tuple; in results, Python compare keys(count)
tup.sort(reverse=True)
#flip them back; to print value first and key second
for k, v in tup:
    print(v, k)
