numlist = []
while True:
    submit = input('Enter a number: ')
    if submit == 'done':
        break
    else:
        value = int(submit)
        numlist.append(value)

print('Maximum:', max(numlist))
print('Minimum:', min(numlist))
