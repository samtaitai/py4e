handle = open('mbox-short.txt')

lst = list()
count = dict()
for line in handle:
    if line.startswith('From ') == True:
        words = line.split()
        day = words[2]
        lst.append(day)
        for day in lst:
            count[day] = count.get(day, 0) + 1
print(count)
