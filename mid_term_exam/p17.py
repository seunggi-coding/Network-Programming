mylist = []

mylist = input("Enter numbers separated by spaces: ").split(" ")

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
    
result = map(lambda x: x**2, mylist)
print(f"Squared numbers: {list(result)}")