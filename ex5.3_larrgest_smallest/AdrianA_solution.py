num_list = []
# largest = big_num   #already commented out
# smallest = small_num    #already commented out

try:
    while True:
        num = input("Enter a number. If done, type 'done'.")
        num_list.append(num)
        if num == 'done':
            break
except:
    print('Invalid input')

print('Maximum is ', max(num_list))
print('Minimum is ', min(num_list))