fruit_dict = {'apple':5, 'banana': 12, 'mango':10, 'orange':9}

fruit_name = input('Enter the name of fruit: ').lower()

if fruit_name in fruit_dict:
    print(f'The quantity of {fruit_name} is {fruit_dict[fruit_name]}')
else:
    print(f'{fruit_name} is not available')