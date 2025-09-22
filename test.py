print("simple_calculator")
print("Enter the first number : ")
a = float(input())
print("Enter the second number : ")
b = float(input())
print("Select Operator: + - * / % **")
op = input()
if(op == '+'):
    print(a+b)
elif(op == '-'):
    print(a-b)
elif(op == '*'):
    print(a*b)
elif(op == '/'):
    print(a/b)
elif(op == '%'):
    print(a%b)
elif(op == "**"):
    print(a**b)