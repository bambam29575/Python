#MINI CALCULATOR
print(" 1-> Addition ")
print(" 2-> Subtraction")
print(" 3 -> multiplication")
print(" 4 -> division")
print(" 5 -> Remainder")
num1 = int(input("Enter number1 : "))
choice = int(input("Enter your choice : "))
num2 = int(input("Enter number2 : "))
result = 0
flag = 0
if(choice == 1):
    result = num1 + num2
elif(choice == 2):
    result = num1 - num2
elif(choice == 3):
    result = num1*num2
elif(choice == 4):
    if(num2 > 0):
        result = num1/num2
    else:
        print("UNdefined")
        flag = 1
elif(choice == 5):
    if(num2 > 0):
        result = num1%num2
    else:
      print("Undefined")
      flag = 1
if(flag == 0):
    print("result : ", result)
