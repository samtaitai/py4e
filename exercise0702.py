fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    floatn = 0
    count = 0
    if line.find('X-DSPAM-Confidence') != -1:
        count = count + 1
        spamn = line[20:]
        floatn = floatn + float(spamn)

print('Average Spam Confidence:', floatn / count)
