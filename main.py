def func_easy_1():
    return 4 * 53


def func_easy_2():
    v1, v2 = 4, 5.6
    return v1 + v2


def func_easy_3(word: str) -> bool:
    if word.islower():
        return True
    return False


def func_easy_4(son1: int | float, son2: int | float) -> int | float:
    return son1 if son1 > son2 else son2


def func_easy_5(son3: int | float):
    if son3 < 0:
        print('manfiy son kiritdingiz')
    else:
        print('musbat son kiritdingiz')


def func_medium1(son: int) -> bool:
    dividers = 0
    for i in range(1, son, +1):
        if son % i == 0:
            dividers += 1
    if dividers == 2:
        return True
    else:
        return False


def func_medium_2(n: int | float):
    l1: list[int] = []
    for i in range(1, n, +1):
        if i % 2 == 0:
            l1.append(i)
    answer = (sorted(l1, reverse=True))
    print(*answer)


# func_medium_2(20)


def func_medium_3(n1: int | float) -> int | float:
    count = 0
    for i in range(1, n1, +1):
        count += i
    return count


# print(func_medium_3(8))

def ekub(a, b):
    return a if b == 0 else ekub(b, a % b)


# print(ekub(36, 60))


def ekub2usul(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# print(ekub2usul(36, 60))


def func_medium_5(a: int, b: int):
    print(a ** b)


# func_medium_5(2, 4)


w1 = ["22", 4, 3, 5, 1, True, False, "ddd"]

def func1(birlist: list) -> int:
    butun_sonlarr = list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), birlist))
    sum_them = 0

    for i in butun_sonlarr:
        sum_them += i

    return sum_them

print(func1(w1))

touple_nums2 = tuple((1, 2, 8, 4, 5, 5.6))


def func2(tn: tuple):
    touple_nums_l = list(tn)
    b = tuple(map(lambda x: x, touple_nums_l[::-1]))
    return b

print(func2(touple_nums2))


def telegram3(aaa: list, bbb: list):
    w_set = set(aaa)
    wa_set = set(bbb)
    same_s = set()
    not_same_s = set()
    diference1 = w_set.difference(wa_set)
    difference2 = wa_set.difference(w_set)
    diference = diference1.union(difference2)

    same = wa_set.intersection(w_set)

    a = not_same_s.union(diference)
    bb = same_s.union(same)
    ddict = {"union": bb, "unique": a}
    return ddict


w = ["22", "22", 4, 3, 5, 1, True, False, "ddd"]
wa = [9, 'hhh', 7, 3]

# print(func3(w, wa))


www1 = 'sssaaaddffrd'


def telegram4(www: str):
    words_in = set()
    aaa = words_in.union(list(www))
    lss = []
    letter_key = dict()

    for i in aaa:
        ddd_v = len(list(filter(lambda x: x == i, www)))
        lss.append(ddd_v)

    for i in www:
        letter_key[i] = www.count(i)
    print(letter_key)


# func4(www1)

ls = [1, 2, 3, 4, 5, 3, 2]


def telegram5(aa: list):
    answer = list(filter(lambda x: x % 3 == 0, aa))
    return list(map(lambda x: x ** 2, answer))
# print(func33(ls))
