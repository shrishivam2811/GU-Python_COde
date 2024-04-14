set1 = set(map(int,input('Enter the elenemt of set separated by single space: ').split()))
set2 = set(map(int,input('Enter the element of set separated by single space: ').split()))

print(f'Intersection of sets {set1} ∩ {set2} : {set1.intersection(set2)}')
print(f'Union of sets {set1} ∪ {set2} : {set1.union(set2)}')
print(f'Difference of sets {set1} - {set2} : {set1.difference(set2)}')
print(f'Difference of sets {set2} - {set1} : {set2.difference(set1)}')
