a = []
b = list()
d = [f'a(i)' for i in 'some']
print(d)

a.append(2)
print(a)
l = list(range(1, 10))
print(l[:4])
print(l[1:4:2])
print(l[-4:-2])
print(l[:])
print(l[::-1])
print(l.index(4))
print(5 in l)
l.remove(2)
print(l)
del l[4]
print(l)