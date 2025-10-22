d = {
  'k1': 123,
  'k2': [1, 2, 3],
  'k3': {'key': 100},
  'k4': ['a', 'b', 'c']
}

# print(d['k2'][2])
# print(d['k3']['key'])
# print(d['k4'][1].upper())

my_dict = {
  'k1': 100,
  'k2': 200,
  'k3': 300
}

my_dict['k4'] = 400
my_dict['k1'] = 'One Hundread'

# print(my_dict.keys())  #dict_keys(['k1', 'k2', 'k3', 'k4'])
# print(my_dict.values())  #dict_values(['One Hundread', 200, 300, 400])
print(my_dict.items())  #dict_items([('k1', 'One Hundread'), ('k2', 200), ('k3', 300), ('k4', 400)])