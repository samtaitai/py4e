import string

#file = input("Enter a file name: ")
file = input('Enter a flie name: ' )
hand = open(file) #not a method, but function

counts = dict()

#make a list of single words
for line in hand:
    #str.maketrans; If three arguments are passed, each character in the third argument is mapped to None.
    #every digits and punctuation should be None
    line = line.translate(str.maketrans('','',string.digits))
    line = line.translate(str.maketrans('','',string.punctuation))
    #every uppercase should be lowercase
    line = line.lower()
    words = line.split()

#word counter in form of dictionary
for word in words:
    counts[word] = counts.get(word, 0) + 1

#flip
temp = list()
for k, v in list(counts.items()):
    temp.append((v, k))

#sort in decreasing order
temp.sort(reverse=True)

#flip back and print
for k, v in temp:
    print(v)
