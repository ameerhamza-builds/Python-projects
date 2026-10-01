def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def division(a,b):
    return a / b

def square(a):
    return a * a

def remainder(a,b):
    return a % b
again = "yes"
while again == "yes":
    try:

        num1=float(input("Enter your first number : "))
        
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Division")
        print("5.Square")
        print("6.Remainder")

        choice = input("Enter your choice from 1 to 6 :")

        if choice == "5":
            result = num1 ** 2
        elif choice not in ["1","2","3","4","5","6"]:
            print("enter choice from 1 to 6 only.")
        else:
            num2 = float(input("Enter your second number : "))


        if choice == "1":
            print(add(num1,num2))
        
        elif choice == "2":
            print(subtract(num1,num2))
        
        elif choice == "3":
           print(multiply(num1,num2))
        elif choice == "4":
            print(division(num1,num2))
        
        elif choice == "6":
            print(remainder(num1,num2))
        
    except ValueError:
        print("please enter a valid number")
    except ZeroDivisionError:
        print("cannot be divided by zero.")

    again = input("do you want to use calculator again ? (yes / no ) : ").lower()
print("Thankyou very much for using the calculator . ")