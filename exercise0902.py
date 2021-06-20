#file handler
handle = open('mbox-short.txt')

lst = list()
count = dict()
#find target line
for line in handle:
    if line.startswith('From ') == True:
        words = line.split()
        #find target word part
        day = words[2]
        lst.append(day)
        #count words; histogram trick 
        for day in lst:
            count[day] = count.get(day, 0) + 1
print(count)
