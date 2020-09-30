user_list = []

while True:
    num = input("Enter a number. If done entering numbers, enter done.")
    if num == "done":
        break
    try:
        num = int(num)
        user_list.append(num)
    except:
        print("Invalid Input")

largest = max(user_list)
smallest = min(user_list)
print("Maximum is", largest)
print("Minimum is", smallest)