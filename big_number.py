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
        num = int(lst1[i]) + int(lst2[i]) + is_one
        if num > 999:
            lst.insert(0, str(num % 1000))
            is_one = 1
        else:
            lst.insert(0, str(num))
            is_one = 0
    for i in range(len(lst)):
        if len(lst[i]) == 2:
            lst[i] = "0" + lst[i]
        elif len(lst[i]) == 1:
            lst[i] = "00" + lst[i]
    return lst


print(big_number_plus("1234560", "66694300"))
print(1234560 + 66694300)


def big_number_minus(str1, str2):
    res = []
    lst1, lst2 = str_to_lst(str1), str_to_lst(str2)
    if len(lst1) > len(lst2):
        for i in range(len(lst1) - len(lst2)):
            lst2.insert(0, "000")
    elif len(lst2) > len(lst1):
        for i in range(len(lst2) - len(lst1)):
            lst1.insert(0, "000")
    is_one = 0
    for i in range(len(lst1) - 1, -1, -1):
        lst1[i] = str(int(lst1[i]) - is_one)
        if int(lst1[i]) < int(lst2[i]):
            lst1[i] = str(int(lst1[i]) + 1000)
            num = int(lst1[i]) - int(lst2[i])
            res.insert(0, str(num))
            is_one = 1
        else:
            num = int(lst1[i]) - int(lst2[i])
            res.insert(0, str(num))
            is_one = 0
    for i in range(len(res)):
        if len(res[i]) == 2:
            res[i] = "0" + res[i]
        elif len(res[i]) == 1:
            res[i] = "00" + res[i]
    return res


print(2598599 - 2589)
print(big_number_minus("2598599", "2589"))
