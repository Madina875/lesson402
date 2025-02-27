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


def func_medium_1(n: int | float):
    print(True) if n % 2 == 0 else print(False)


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


def func_medium_4(a: int, b: int) -> int | float:
    return a % b


# print(func_medium_4(30, 20))


def func_medium_5(a: int, b: int):
    print(a ** b)


# func_medium_5(2, 4)

# 1
w1 = ["22", 4, 3, 5, 1, True, False, "ddd"]


def func_hard_13(llll: list):
    only_ints = []
    sumofthem = 0
    for i in llll:
        if isinstance(i, int) and not isinstance(i, bool):
            only_ints.append(i)
    for l in only_ints:
        sumofthem += l

    return sumofthem


# print(func_hard_13(w1))

# 2

touple_nums = tuple((1, 2, 8, 4, 5, 5.6))

print(touple_nums[::-1])


def func2(tn: tuple):
    touple_nums_l = list(tn)
    b = tuple(filter(map(lambda x: x, touple_nums_l[::-1])))
    print(b)

    func2(touple_nums)

    # 3


def func3(aaa: list, bbb: list):
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
    print(' same:', bb, '\n', 'not same:', a)


w = ["22", "22", 4, 3, 5, 1, True, False, "ddd"]
wa = [9, 'hhh', 7, 3]

# func3(w, wa)

# 4

www1 = 'sssaaaddffrd'


def func4(www: str):
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

# 5

ls = [1, 2, 3, 4, 5, 3, 2]


def func33(aa: list):
    answer = list(filter(lambda x: x % 3 == 0, aa))
    return list(map(lambda x: x ** 2, answer))

# print(func33(ls))
