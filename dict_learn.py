d = {f'key_{i}':f'value_{i}' for i in range(0, 10)}
#print(d)

dict_1 = {
    'key' : 'value'
}

print(len(d))

d['key_1'] = 'some'
a = d.pop('key_2')
print(a)
d['new_key'] = 'new_value'
print(d)

CONST = '<nothing>'
obj = d.get('nothing', CONST)
if obj == CONST:
    pass
else:
    pass

