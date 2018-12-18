#LIST is mutable
list_a = []
list_b = list()

print(list_a)
print(list_b)

print(len(list_a))
print(len(list_b))

if list_a:
    pass

#LIST COMPREHENSION
list_c = [1, 2, 3, 4, 5]
list_d = [i*2 for i in list_c]
print(list_d)


#LIST OPERATION
empty_list = list()
empty_list.append('a')
empty_list.append('b')
print(empty_list)


