import random
import datetime


def basic_compare(first, second):
    return first <= second


def merge(lst, compareMethod):
    if len(lst) <= 1:
        return lst
    res1 = merge(lst[:int(len(lst) / 2)], compareMethod)
    res2 = merge(lst[int(len(lst) / 2):], compareMethod)
    lst.clear()
    while len(res1) > 0 and len(res2) > 0:
        if compareMethod(res1[0], res2[0]):
            lst.append(res1.pop(0))
        else:
            lst.append(res2.pop(0))
    lst += res1
    lst += res2
    return lst


def test_merge():
    lst = []
    for i in range(100):
        lst.append(random.randint(-100, 100))
    # lst = [0, 2, -1, 209, 87, -98, -4, 12]
    print(lst)
    print("start")
    start = datetime.datetime.now()
    lst = merge(lst, basic_compare)
    end = datetime.datetime.now()
    print("end")
    print(lst)
    print(end - start)


if __name__ == "__main__":
    test_merge()
