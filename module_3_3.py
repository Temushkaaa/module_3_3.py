def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# print_params(b = 25)
# print_params(c = [1,2,3])

values_list = [305, False, 'winter']
values_dict = {'a': 52, 'b': True, 'c': 'mouse'}
# print_params(*values_list)
# print_params(**values_dict)

values_list_2 = ['music', 92]
print_params(*values_list_2, 42)