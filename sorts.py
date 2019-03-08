############################
#                           #
#      2019 IU7 BMSTU       # 
#                           # 
#    All sorts which can    #
#    be asked on eaxams.    #
#                           #
#    Special thanks to:     #
#      @maxim_kozlov        #
#                           #
# Written in Pascal style   #
#                           #
#############################


def insertion(mass):
    len_mass = len(mass)
    for i in range(1, len_mass):
        v = mass[i]
        j = i
        while mass[j - 1] > v and j > 0:
            mass[j] = mass[j - 1]
            j -= 1
        mass[j] = v
    return mass


def barrierInsertion(mass):
    i = 2
    n = len(mass)
    mass.append(mass[0])
    while i <= n:
        if mass[i - 1] > mass[i]:
            mass[0] = mass[i]
            j = i - 1
            while mass[j] > mass[0]:
                mass[j + 1] = mass[j]
                j -= 1
            mass[j + 1] = mass[0]
        i += 1
    del mass[0]
    return mass


def binaryInsertion(mass):
    len_mass = len(mass)
    for i in range(1, len_mass):
        key = mass.pop(i)
        low, up = 0, i
        while low < up:
            mid = (low + up) // 2
            if mass[mid] < key:
                low = mid + 1
            else:
                up = mid
        mass.insert(low, key)
    return mass


def shell(mass):
    len_mass = len(mass)

    t = len_mass // 2
    while t > 0:
        for i in range(len_mass - t):
            j = i
            while j > -1 and mass[j] > mass[j + t]:
                mass[j], mass[j + t] = mass[j + t], mass[j]
                j -= 1
        t //= 2
    return mass


def merge(lst1, lst2):
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)
    merged = [0] * (len_lst1 + len_lst2)

    q = i = j = 0
    while i < len_lst1 and j < len_lst2:
        if lst1[i] <= lst2[j]:
            merged[q] = lst1[i]
            i += 1
        else:
            merged[q] = lst2[j]
            j += 1
        q += 1

    while i < len_lst1:
        merged[q] = lst1[i]
        i += 1
        q += 1
    while j < len_lst2:
        merged[q] = lst2[j]
        j += 1
        q += 1
    return merged


def merge_sort(mass):
    len_mass = len(mass)
    if len_mass < 2:
        return mass
    else:
        m = len_mass // 2
        return merge(merge_sort(mass[:m]), merge_sort(mass[m:]))


def m_merge_sort(mass):
    mass = [[x] for x in mass]
    while len(mass) != 1:
        temp = []
        len_mass = len(mass)
        for j in range(0, len_mass - 1, 2):
            temp.append(merge(mass[j], mass[j + 1]))
        if len_mass % 2:
            t = temp.pop()
            temp.append(merge(t, mass[len_mass - 1]))
        mass = temp

    return mass[0]


def qsort(mass):
    len_mass = len(mass)
    if len_mass < 2:
        return mass

    x = mass[len_mass // 2]

    less, equal, more = [], [], []

    for el in mass:
        if el == x:
            equal.append(el)
        elif el > x:
            more.append(el)
        else:
            less.append(el)
    return qsort(less) + equal + qsort(more)


def quicksort(mass, l, r):
    if l >= r:
        return
    i, j = l, r
    x = mass[(l + r) // 2]
    while i <= j:
        while mass[i] < x:
            i += 1
        while mass[j] > x:
            j -= 1
        if i <= j:
            mass[i], mass[j] = mass[j], mass[i]
            i += 1
            j -= 1

    quicksort(mass, l, j)
    quicksort(mass, i, r)
    return mass


def quicksortNoRec(mass):
    stack = [0, len(mass) - 1]
    while stack:
        r = stack.pop()
        l = stack.pop()

        i, j = l, r
        x = mass[(l + r) // 2]

        while i <= j:
            while mass[i] < x:
                i += 1
            while mass[j] > x:
                j -= 1

            if i <= j:
                mass[i], mass[j] = mass[j], mass[i]
                i += 1
                j -= 1
        if l < j:
            stack.extend([l, j])
        if i < r:
            stack.extend([i, r])
    return mass


def selection(mass):
    len_mass = len(mass)
    for i in range(len_mass):
        min_i = i
        for j in range(i + 1, len_mass):
            if mass[j] < mass[min_i]:
                min_i = j
        mass[min_i], mass[i] = mass[i], mass[min_i]
    return mass


def buble(mass):
    """ with flag! """
    len_mass = len(mass)
    for i in range(len_mass, 0, -1):
        need = False
        for j in range(1, i):
            if mass[j - 1] > mass[j]:
                mass[j - 1], mass[j] = mass[j], mass[j - 1]
                need = True
        if not need:
            break

    return mass


def shaker(mass):
    new_left = left = 0
    new_right = right = len(mass) - 1
    while left <= right:
        for i in range(left, right):
            if mass[i] > mass[i + 1]:
                mass[i + 1], mass[i] = mass[i], mass[i + 1]
                new_right = i
        if new_right == right:
            break
        else:
            right = new_right
        for i in range(right, left, -1):
            if mass[i - 1] > mass[i]:
                mass[i - 1], mass[i] = mass[i], mass[i - 1]
                new_left = i
        if new_left == left:
            break
        else:
            left = new_left
    return mass


def hairbrush(mass):
    len_mass = len(mass)
    gap = len_mass
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap // 1.247))  # minimum gap is 1
        swaps = False
        for i in range(len_mass - gap):
            j = i + gap
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]
                swaps = True
    return mass


def mHairbrush(mass):
    len_mass = len(mass)
    gap = int(len_mass // 1.247)
    while gap:
        if 8 < gap < 11:
            gap = 11
        swaps = False
        for i in range(len_mass - gap):
            j = i + gap
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]
                swaps = True
        gap = int(gap // 1.247) or swaps
    return mass
