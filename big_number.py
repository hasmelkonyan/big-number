def div_by_three(str):
    len_str = len(str)
    if len_str % 3 == 1:
        str = "00" + str
    elif len_str % 3 == 2:
        str = "0" + str
    return str


def str_to_lst(my_str):
    lst = []
    my_str = div_by_three(my_str)
    i = 0
    while i < len(my_str):
        lst.append((my_str[i: i + 3]))
        i += 3
    return lst


def big_number_plus(str1, str2):
    lst = []
    is_one = 0
    lst1 = str_to_lst(str1)
    lst2 = str_to_lst(str2)
    if len(lst1) > len(lst2):
        for i in range(len(lst1) - len(lst2)):
            lst2.insert(0, "000")
    elif len(lst2) > len(lst1):
        for i in range(len(lst2) - len(lst1)):
            lst1.insert(0, "000")

    for i in range(len(lst1) - 1, -1, -1):
        print(lst1[i], lst2[i])
        if int(lst1[i]) + int(lst2[i]) + is_one > 999:
            lst.insert(0, (int(lst1[i]) + int(lst2[i]) + is_one) % 1000)
            is_one = (int(lst1[i]) + int(lst2[i]) + is_one) // 1000
        else:
            lst.insert(0, (int(lst1[i]) + int(lst2[i]) + is_one))
    return lst


print(big_number_plus("123456", "666943"))

