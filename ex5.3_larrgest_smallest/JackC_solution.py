largest = None
smallest = None
List = []

while True:
    try:
        num = input("Enter a number: ")
        if num != "done":
            num = int(num) #added
            List.append(num)
        elif num == "done":
            break

    except:
        print("Invalid input")

smallest = min(List)
largest = max(List)
print("Maximum is " + str(largest))
print("Minimum is " + str(smallest))