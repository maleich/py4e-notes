# Chien's solution

int_list = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
        # int_list()   # needs argument
        int_list.append(num)
    except:
        print('Invalid input')

largest = max(int_list)
smallest = min(int_list)
print("Maximum is", largest)
print("Minimum is", smallest)



