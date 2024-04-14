element = input('Enter the element of list separated by single space: ')
split_ele = element.split()
l1 = []

for i in split_ele:
    int_i = int(i)
    l1.append(int_i)

print(f'List: {l1}')
print(f'Sum of list is {sum(l1)}')