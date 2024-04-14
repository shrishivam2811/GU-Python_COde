fruits_dict = {'apple': 3, 'banana': 5, 'orange': 2}

sorted_list = sorted([(value, key) for key, value in fruits_dict.items()])

sorted_fruits = {key: value for value, key in sorted_list}

print(sorted_fruits)