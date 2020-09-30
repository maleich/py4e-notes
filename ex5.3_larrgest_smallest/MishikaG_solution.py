num_list = []

while True:
    try:
        x = input("Enter a number: ")
        if x == "done":
            break
        x = int(x)
        num_list.append(x)

    except:
        print("Invalid input")

biggest = max(num_list)
smallest = min(num_list)

print("Maximum is", biggest)
print("Minimum is", smallest)