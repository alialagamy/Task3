print("****************Hello in My Task************\n")
list = []
n = int(input("Enter length list : \n"))
mod = int(input("Enter Divisible : \n"))

for i in range(n):
    element=int(input("Enter The Element : \n"))
    list.append(element)
print("The list elements :",list)

for element in list:
    if element % mod == 0:
        print("The result : ",element)
    else:
        print("not found")