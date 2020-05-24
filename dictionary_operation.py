dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# print only a
print(dict['a'])
# print all list element
print(dict)
# add new value
dict['e'] = 50
print(dict)
# update the value of a
dict['a'] = 100
print(dict)
# return the null object no error while running
print(dict.get('k'))
# return the k value as default value
print(dict.get('k', 150))
# print all the aelemnet again
print(dict)
# remove the mapping of the elemnet
del dict['a']
print(dict)
# pop the value from the list element
val = dict.pop('b')
print(val)
# will only print the rest elemnet poping out B
print(dict)
# pop the value from the list element
val1 = dict.pop('a', 1000)
print(val1)
# print all again
print(dict)
# will remove random value form the list elemnet
val3 = dict.popitem()
print(val3)  # its the tuple object
print(dict)
# hashing function
val2 = dict.setdefault('l', 400)
print(val2)
print(dict)  # will add new L in the list
val2 = dict.setdefault('d', 400)  # will not change the value for D it will remain the same
print(val2)
new_val = dict.fromkeys(['x', 'm', 'n'],300)
print(new_val)
print(dict)
# let me chrate new dictionary
d1 = {'j': 70, 'h': 20, 'g': 30, 'y': 40}
dict.update(d1)
print(dict)
# copy function  # for working on duplicate value main will not effected
d2 = dict.copy()
print(d2)
for key in dict:
    print(key)
    print(dict[key])
    print("key ={},value={}". format(key, dict[key]))
    print('key=%s, value = value= $s'%(key,dict[key]))
