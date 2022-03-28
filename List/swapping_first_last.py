# write a Python program to swap first and last element of the list.


def swap_list(list1):
    first = list1[0]
    last = list1[-1]
    list1[0] = last
    list1[-1] = first
    return list1


list2 = [1, 2, 3, 4, 5, 6]
print(swap_list(list2))


def swap_list(list2):
    first = list2.pop(0)
    last = list2.pop(-1)
    list2.insert(0, last)
    list2.append(first)
    return list2


list2 = [1, 2, 3, 4, 5, 6]
print(swap_list(list2))
