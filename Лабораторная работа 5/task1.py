from pprint import pprint
dict_comprehension = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(0, 16)]
pprint(dict_comprehension)
# task1
