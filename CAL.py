
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b ==0:
        print("cannot devide by zero")
    return a/b

while True:

    print("welcome to the calculator program:")
    print("1. Add")
    print("2. subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice= input("Pleaase select an option (1-5): ")

    if choice =="5":
        print("EXIT! GOODBYE!!!")
        break

    a= float(input("Enter first number: "))
    b= float(input("Enter second number:"))

    if choice =="1":
        print(f"Result: {add(a,b)}")
    elif choice =="2":
        print(f"Result: {sub(a,b)}")

    elif choice =="3":
        print(f"Reuslt: {multiply(a,b)}")
    elif choice  =="4":
        print(f"Result: {divide(a,b)}")

    else:
        print("INVALID CHOICE>>>>")