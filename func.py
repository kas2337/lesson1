def get_summ(one, two, delimiter='&'):
    str_1 = str(one) + str(delimiter) + str(two)
    return str_1.upper()

print(get_summ('learn', 'python'))


