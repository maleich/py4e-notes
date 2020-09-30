
# Jake's solution

max = 0
min = 100000

while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
        if num > max:
            max = num
        elif num < min:
            min = num
    except:
        if num == 'done':
            print(f'Maximum is {max}')
            print(f'Minimum is {min}')
        else:
            print('Invalid input')

