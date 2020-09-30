# Chien's solution

# change order to be able to add all 5 inputs before program exits
int_list = []
# move next 2 lines after while loop
# print(f'Maximum is {largest}')
# print(f'Minimum is {smallest}')

try:
    while True:
        num = int(input('Enter a number: '))
        if num == 'done':
            break
        # int_list()   # needs argument
        int_list.append(num)
except:
    print('Invalid input')

largest = max(int_list)
smallest = min(int_list)
print(f'Maximum is {largest}')
print(f'Minimum is {smallest}')
print(int_list)


