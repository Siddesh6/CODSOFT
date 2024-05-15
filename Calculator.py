def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return " Opps! the number is divisible by zero is not defined ."
    else :
        return x/y
    
print ("please select a opperator to perfom a calculation :")
print ("1. Addidtion ")
print ("2. substract")
print ("3. multiplication ")
print ("4. Division")

while True:
    choice =input(" Select one among  (1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter a first number  :"))
        num2 = float(input("Enter a second  number "))
        
        if choice == '1':
            print("solution:",add(num1,num2))
        elif choice == '2':
            print("solution:", sub(num1,num2))
        elif choice == '3':
            print("solution:", multiply(num1,num2))
        elif choice == '4':
            print("solution :",divide (num1,num2))
        break
    else:
        print("Not a invalid input")