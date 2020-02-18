Waldo = 'W'
Other = '.'

def all_row_exists_waldo(l):

    temp =0
    for lst in l:
        if Waldo in lst:
            temp=1
        else:
            return False
    return True

def all_col_exists_waldo(l):
    #l=[[Other, Waldo, Other], [Waldo, Other, Other], [Other, Waldo, Waldo]]
    # l=[[Waldo, Other, Other],[Other, Waldo, Other], [Waldo, Other, Other]]
    temp =0
    colsize = 0
    for lst in l:
        colsize = len(lst)
        break


    if len(l) is 0:
        return True
    for lst in l:
        if len(lst) is 0:
            return True


    colList =[]
    for j in range(colsize):
        for i in range(len(l)):
            colList += [ l[i][j] ]

        # print (colList)
        if Waldo in colList:
            colList =[]
        else:
            return False
    # print ("done")
    return True




    # temp = 0
    # for lst in l:
    #     for x in lst:
    #         if x is Waldo:
    #             temp =1
    #     if temp is 1:
    #         temp=0
    #     else:
    #         return False
    # return True

def all_row_all_waldo(l):
    temp = 0
    for lst in l:
        for x in lst:
            if x is Waldo:
                temp+=1
        if temp is len(lst):
            temp=0
        else:
            return False
    return True

def all_col_all_waldo(l):
    temp = 0
    for lst in l:
        for x in lst:
            if x is Waldo:
                temp +=1
        if temp is len(lst):
            temp=0
        else:
            return False
    return True


def exists_row_exists_waldo(l):
    temp = 0
    for lst in l:
        if Waldo in lst:
            return True
    return False

def exists_col_exists_waldo(l):
    temp = 0
    for lst in l:
        for x in lst:
            if x is Waldo:
                return True
    return False

def exists_row_all_waldo(l):
    # l=[[Other, Waldo, Other], [Waldo, Waldo, Waldo], [Other, Other, Other]]
    temp = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] is Waldo:
                temp+=1
        if temp is len(l[i]):
            return True
        else:
            temp=0
    return False

def exists_col_all_waldo(l):
    # l=[[Other, Waldo, Other],[Waldo, Waldo, Other],  [Other, Waldo, Waldo]]
    # l= [[Waldo, Waldo, Waldo],[Waldo, Other, Waldo], [Other, Waldo, Other]]
    temp =0
    colsize = 0
    for lst in l:
        colsize = len(lst)
        break


    if len(l) is 0:
        return False
    for lst in l:
        if len(lst) is 0:
            return False


    colList =[]
    for j in range(colsize):
        for i in range(len(l)):
            colList += [ l[i][j] ]

        # print (colList)
        temp=0
        for x in colList:
            if x is Waldo:
                temp+=1
        if temp is len(colList):
            return True
        colList =[]
    # print ("done")
    return False


# if __name__ == "__main__":
#     print(exists_col_all_waldo([]))
