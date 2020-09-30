input_list = []

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        input_list.append(num)
    except:
        print("Invalid input")

largest = max(input_list)
smallest = min(input_list)

print("Maximum is", largest)
print("Minimum is", smallest)