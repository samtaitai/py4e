#import regular expression library
import re

#open a file
fhand = open('regex_sum_1264914.txt')
#print(fhand)

alist = []
blist = []
clist = []
for line in fhand:
    num = re.findall('[0-9]+', line)
    alist.append(num)
#print(len(alist))
for iterv in range(len(alist)):
    #remove empty lists
    if len(alist[iterv]) == 0:
        continue
    else:
        blist.append(alist[iterv])
#print(blist)
#merge sublists
for iterv2 in range(len(blist)):
    for i in range(len(blist[iterv2])):
        clist.append(int(blist[iterv2][i]))
print(sum(clist))
