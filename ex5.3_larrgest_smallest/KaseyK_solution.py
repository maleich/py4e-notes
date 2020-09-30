list = []

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num = int(num)
        list.append(num)
    except:
        print("Invalid input")

print("Maximum is", max(list))
print("Minimum is", min(list))