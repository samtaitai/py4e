name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
counts = dict()
for line in handle:
    if line.startswith("From ") == True:
        line = line.split()
        tpart = line[5]
        tpart = tpart.split(":")
        time = tpart[0]
        lst.append(time)
    else:
        continue
for iterv in lst:
    counts[iterv] = counts.get(iterv, 0) + 1
tup = list()
#flip; tuple as value in a list
for key, value in counts.items():
    tup.append((key, value))
#from the smallest
tup.sort()
for k, v in tup:
    print(k, v)
