dict_1 = {'city':'Moscow', 'temperature':"20"}
print(dict_1['city'])
dict_1['temperature'] = str(int(dict_1['temperature']) - 5)
print(dict_1)

print(dict_1.get('country','Russia'))
dict_1['date']= '27.05.2019'
print(len(dict_1))
print(dict_1)
