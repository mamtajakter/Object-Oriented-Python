
def all_same(l: list) -> bool:
    _size = len(l)
    for i in range(_size-1):
        if l[i]==l[i+1]:
            pass
        else:
            return False
    return True


def dedup(l: list) -> list:
    _size = len(l)
    if _size==0:
        return []
    dl = []
    temp = l[0]
    i=0
    for i in range(_size-1):
        if temp==l[i+1]:
            pass
        else:
            dl.append(temp)
            temp = l[i+1]
    dl_size = len (dl)
    if (dl[dl_size-1]==temp):
        pass
    else:
        dl.append(temp)
    return dl


def max_run(l: list) -> int:
    _size = len(l)
    if _size==0:
        return 0
    temp = l[0]
    run = 1
    maxrun = 1
    for i in range(_size-1):
        if temp==l[i+1]:
            run +=1
        else:
            if (run >= maxrun):
                maxrun = run
            run =1
            temp = l[i+1]
    if (run >= maxrun):
        maxrun = run
    return maxrun