a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

print('\nArithmetic Operations:\n')
print(f'Addition: {a}+{b} = {a+b}\n')
print(f'Subtraction: {a}-{b} = {a-b}\n\t     {b}-{a} = {b-a}\n')
print(f'Multiplication: {a}*{b} = {a*b}\n')
print(f'Division: {a}/{b} = {'Undefined'if b==0 else a/b}\n\t  {b}/{a} = {'Undefined'if a==0 else b/a}\n')