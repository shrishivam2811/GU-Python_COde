num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f'{num1} in binary {bin(num1)}')
print(f'{num2} in binary {bin(num2)}')

bitwise_and = num1 & num2
print(f'Bitwise AND: {bitwise_and} = {bin(bitwise_and)}')

bitwise_or = num1 | num2
print(f'Bitwise OR: {bitwise_or} = {bin(bitwise_or)}')

bitwise_xor = num1 ^ num2
print(f'Bitwise XOR: {bitwise_xor} = {bin(bitwise_xor)}')

bitwise_complement_num1 = ~num1
bitwise_complement_num2 = ~num2
print(f'Bitwise complement of first number: {bitwise_complement_num1} = {bin(bitwise_complement_num1)}')
print(f'Bitwise complement of second number: {bitwise_complement_num2} = {bin(bitwise_complement_num2)}')