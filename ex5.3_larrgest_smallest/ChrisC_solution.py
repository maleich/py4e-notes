calclist = []   # moved from below

while True:
    # calclist = []
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num) # added
        calclist.append(num)
    except:
        print('Invalid input')

largest = max(calclist)
smallest = min(calclist)

print('Maximum is ' + str(largest)) # need a string to go with the words
print('Minimum is ' + str(smallest))