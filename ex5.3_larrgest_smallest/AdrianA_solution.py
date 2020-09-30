num_list = []

while True:
    num = input("Enter a number. If done, type 'done'.")
    if num == 'done':
        break
    try:
        num = int(num)
        num_list.append(num)

    except:
        print('Invalid input')

print('Maximum is ', max(num_list))
print('Minimum is ', min(num_list))