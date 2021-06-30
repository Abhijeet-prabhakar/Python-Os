import random

while True:
    a = random.randrange(0, 1)
    print(a)
    b = 0
    c = 1
    d = 0
    e = 1

    list1 = [b, c, d, e]
    random_number = random.choice(list1)
    print(random_number)

    list2 = [e, d, c, b]
    random_number = random.choice(list2)
    print(random_number)

    list3 = [e, c, d, b]
    random_number = random.choice(list3)
    print(random_number)

    list4 = [b, d, c, e]
    random_number = random.choice(list4)
    print(random_number)

    list5 = [b, c, d, e]
    random_number = random.choice(list5)
    print(random_number)

    # list6 = list2, list1, list3, list4, list5
    # random_number = random.choice(list6)
    # print(random_number)

    if a == 1:
        print(0)
    elif a == 0:
        print(1)
    elif a == 0+1:
        print(0)
    elif a == 1-1:
        print(1)
    elif a > 0:
        print(1)
    elif a < 0:
        print(0)
    if a > 0:
        a + 0
        print(a)
    elif a == 0:
        a + 1
        print(a)
    print(a + 1)