def telegram1(tuplesonlar: tuple):
    juft_sonlar = list(filter(lambda x: x % 2 == 0, tuplesonlar))
    yigindisi = 0
    for i in juft_sonlar:
        yigindisi += i

    print(yigindisi)


telegram1((1, 2, 3, 4, 5, 6, 7))


# _____________________________________________________________________________

def telegram2(listt: list):
    lis = list(reversed(listt))
    print(lis)


telegram2([1, 2, 3, 5, 4, 6])


# _____________________________________________________________________________

def telegram3(listt2: list):
    sonlar = sorted(listt2, reverse=True)
    ikkinchi_katta = sonlar[1]
    print(ikkinchi_katta)


telegram3([2, 3, 8, 6, 7, 5, 2, 1])


# _______________________________________________________________________________

def telegram4(listt3: list[str]):
    words = []
    for i in listt3:
        words.append(i.capitalize())
    print(words)


telegram4(['hello', 'how'])


# _________________________________________________________________________________

def flatten_telegram5(ttt):
    result = []
    for item in ttt:
        if isinstance(item, (list, tuple)):
            result.extend(flatten_telegram5(item))
        else:
            result.append(item)
    print(result)
    return result


lst = [(1, 2, 3), [4, 3], 'sss']
flatten_telegram5(lst)


# ___________________________________________________________________________________

def telegram6(lstt: list):
    listti = list(dict.fromkeys(lstt))
    print(listti)


lsts = [2, 2, 7, 5, 7, 3, 4, 6]
telegram6(lsts)


# ___________________________________________________________________________________

def telegram7(filist: list):
    number_highest = tuple(sorted(filist, reverse=True))[0]
    number_lowest = tuple(sorted(filist, reverse=False))[0]
    now = ('highest number', number_highest, 'lowest number', number_lowest)

    print(now)


telegram7([3, 5, 8, 9, 2, 8.2])


# ________________________________________________________________________________________

def telegram7_2usul(filist2: list[int | float]):
    highestn = filist2[0]
    lowestn = filist2[0]

    for i in filist2:
        if i > highestn:
            highestn = i
        elif i < lowestn:
            lowestn = i

    aaa = ('highest:', highestn, 'lowest:', lowestn)
    result = tuple(aaa)
    print(result)


telegram7_2usul([2, 3, 4, 5, 6.5, 3])


# ______________________________________________________________________________________

def telegram8(item, lisst: list):
    if item in lisst:
        print(True)
    else:
        print(False)


# element = input('izlamoqchi elementingizni kiriting:')
# listt = [1, 2, 3, 4, 5, 'kitob', 'sss']
# telegram8(element, listt)
# ______________________________________________________________________________________

birlist = [1, 2, 3, 4, 'aaa', 'aaa', 2, 2, 1]


def telegram9(www: list):
    every = set()
    aaa = every.union(www)
    sss = list()
    letter_key = {}

    for i in aaa:
        ddd_v = len(list(filter(lambda x: x == i, www)))
        sss.append(ddd_v)

    for i in www:
        letter_key[i] = www.count(i)
    print(letter_key)


telegram9(birlist)


# __________________________________________________________________________________

def telegram10(set1: set, set2: set):
    answer = set1.intersection(set2)
    # print(answer)


telegram10({1, 3}, {3, 4})


# __________________________________________________________________________________

def telegram11(lstt):
    items = []
    for item in lstt:
        if isinstance(item, set):
            items.extend(telegram11(item))
        else:
            items.append(item)
    print(items)
    return items


lstss = [{123}, 2, 1, 2]
telegram11(lstss)


# __________________________________________________________________________________-

def telegram12(set1: set, set2: set):
    unioni_listi = list(set2.intersection(set1))
    set1listi = list(set1)
    countt = 0
    for i in set1listi:
        if i in unioni_listi:
            countt += 1

    if countt == len(set1listi):
        print(True)
    else:
        print(False)


a = {1, 2}
b = {1, 2, 3}
telegram12(a, b)


# ______________________________________________________________________

def telegram13(strr: str):
    javob = set()
    aa = javob.union(strr)  # o'zini chiqarsa ham bo'lar edi lekin alifbo ketmaketligida chiqarish kk ekan :
    aaaa = set(sorted(aa))
    print(aaaa)


telegram13('absabs')


# ________________________________________________________________________________

def telegram14(dictt: dict):
    inverted_dict = dict(zip(dictt.values(), dictt.keys()))
    print(inverted_dict)


telegram14({'x': 10, 'y': 20})


# 2-usuli
# data = {"a": 1, "b": 2, "c": 3}
#
# inverted_dict = {value: key for key, value in data.items()}
# print(inverted_dict)
# _________________________________________________________________________________

def telegram15(dict1: dict, dict2: dict):
    dict1.update(dict2)
    print(dict1)


info = {"name": "Hasan"}
scores = {"Ali": 78, "Vali": 85}

kkk = scores.get
# print(kkk)
telegram15(info, scores)

# _________________________________________________________________________________________

data = {"Ali": 78, "Vali": 85, "Hasan": 92, "Husan": 88}


def telegram16(data: dict):
    max_item = sorted(data.items(), key=lambda x: x[1])[-1]  # Eng katta element
    sss = max_item[0]

    print(sss)


telegram16(data)

# LEETCODE_______________________________________________________________________________________

sss = "hello how are you heeyy"


def truncateSentence(s: str, k: int) -> str:
    list_split = list(s.split())
    k_count = 0
    answer = []
    for i in range(len(list_split)):
        k_count += 1
        answer.append(list_split[i])
        if k_count == k:
            break
    return " ".join(answer)


print(truncateSentence(sss, 4))

