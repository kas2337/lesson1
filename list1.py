list_1 = [3, 5, 7, 9, 10.5]
print(list_1)
list_1.append('Python')
print(list_1)
print(len(list_1))
print()
for i in list_1:
    if i == 'Python':
        print(i, end='\n')
    else:
        print(i, end=', ')
print()    
print(list_1[0])
print(list_1[-1])
print(list_1[2:5])
list_1.remove("Python")
print(list_1)