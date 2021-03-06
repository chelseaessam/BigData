from tabulate import tabulate
from itertools import combinations


def first(arry_x, mim, suportA):
    count_arry = []
    refranc = []
    get_index = 0
    Support = 0
    for x in arry_x:

        if (x in refranc) == 0:
            cou = arry_x.count(x)
            if cou >= mim:
                Support = cou / len(arry_x)

                refranc.append(x)
                count_arry.append([[x], Support, [get_index]])
                suportA.append([[x], Support])
        else:
            index1 = refranc.index(x)
            count_arry[index1][2].append(get_index)
        get_index = get_index + 1;
    return count_arry

############################################

def SupportItemSet(SupportA, SupportB, total, minSupport):
    index = []
    supportArray = []
    count = 0
    for firstIndex in SupportA:
        A = firstIndex[2]
        for secondIndex in SupportB:
            B = secondIndex[2]
            for row in A:
                if row in B:
                    count = count + 1
                    index.append(row)

            support = count / total

            if (support >= minSupport):
                firsttuple = firstIndex[0] + secondIndex[0]
                supportArray.append([firsttuple, support, index])

            index = []
            count = 0

    return supportArray

###################################################3


def get_first(original, min_count, SupportAar):
    first_set = []
    for i in original:
        ary = first(i, min_count, SupportAar)
        if len(ary) != 0:
            first_set.append(ary)
    return first_set

def get_Item(first_set, Any_list, Total_count, min_support):
    set_A = []
    for i in Any_list:
        for j in first_set:
            ch = j[0][0][0][0]
            count = 0

            for char in i[0][0]:
                if char[0] < ch:
                    count = count + 1

            if count == len(i[0][0]):
                ary = SupportItemSet(i, j, Total_count, min_support)
                if len(ary) != 0:
                    set_A.append(ary)

    return set_A

#####################################################
#####################################################

def Lift(SupportA, SupportB, SupportAB):
    return (SupportAB) / (SupportA * SupportB)

def Leverage(SupportA, SupportB, SupportAB):
    return SupportAB - (SupportA * SupportB)

def Confidence(supportXY, supportX):
    return (supportXY / supportX) * 100

#####################################################

def sortlift(elem):
    return elem[2]

def sortlev(elem):
    return elem[3]

def implies(X, Y):
    ru = ""
    for j in X:
        j=lable(j)
        ru = ru + j + " , "
    ru = ru[:len(ru) - 3] + "  ------>  "

    for j in Y:
        j=lable(j)
        ru = ru + j + " , "
    ru = ru[:len(ru) - 3]
    return ru

#####################################################
def lable(j):
    if j[0] == "A":
        if j[1] == '0':
            j = "MGODRK Roman catholic see " +j[1] + " (0%)"
        elif j[1] == '1':
            j = "MGODRK Roman catholic see " +j[1] + " (1 - 10%)"
        elif j[1] == '2':
            j = "MGODRK Roman catholic see " +j[1] + " (11 - 23%)"
        elif j[1] == '3':
            j = "MGODRK Roman catholic see " +j[1] + " (24 - 36%)"
        elif j[1] == '4':
            j = "MGODRK Roman catholic see " +j[1]+ " (37 - 49%)"
        elif j[1] == '5':
            j = "MGODRK Roman catholic see " +j[1]+ " (50 - 62%)"
        elif j[1] == '6':
            j = "MGODRK Roman catholic see " +j[1]+ " (63 - 75%)"
        elif j[1] == '7':
            j = "MGODRK Roman catholic see " +j[1] + " (76 - 88%)"
        elif j[1] == '8':
            j = "MGODRK Roman catholic see " +j[1] + " (89 - 99%)"
        elif j[1] == '9':
            j = "MGODRK Roman catholic see " +j[1] + " (100%)"
    elif j[0] =="B":
        j = "MGODPR Protestant "+j[1]
    elif j[0] =="C":
        j= "MGODOV Other religion "+j[1]
    elif j[0] =="D":
        j= "MGODGE No religion "+j[1]
    elif j[0] =="E":
        j= "MRELGE Married "+j[1]
    elif j[0] =="F":
        j= "MRELSA Living together "+j[1]
    elif j[0] =="G":
        j= "MRELOV Other relation "+j[1]
    elif j[0] =="H":
        j= "MFALLEEN Singles "+j[1]
    elif j[0] =="I":
        j= "MFGEKIND Household without children "+j[1]
    elif j[0] =="J":
        j= "MFWEKIND Household with children "+j[1]
    elif j[0] =="K":
        j= "MOPLHOOG High level education "+j[1]
    elif j[0] =="L ":
        j = "MOPLMIDD Medium level education "+j[1]
    return j
#####################################################

def get_Rules(original):
    SupportAar = []
    lows = []

    only_first = 0
    Total_count = len(original[0])

    min_count = int(input("please input min count "))
    min_Confidence = int(input("please input min Confidence (%) "))
    min_support = min_count / Total_count

    first_set = get_first(original, min_count, SupportAar)
    final_list = first_set

    while True:
        temp = get_Item(first_set, final_list, Total_count, min_support)
        if len(temp) != 0:
            only_first = 1
            final_list = temp
            for j in final_list:
                for i in j:
                    SupportAar.append([i[0], i[1]])
        else:
            break

    if only_first == 1:
        for G in final_list:
            for i in G:
                ran = len(i[0])
                com = []
                for k in range(1, ran):
                    com.append(list(combinations(i[0], k)))

                for F in com:
                    for j in F:
                        X = list(j)
                        Y = list(set(i[0]) - set(X))
                        Y.sort()
                        for XY in SupportAar:
                            if X == XY[0]:
                                supportX = XY[1]
                            elif Y == XY[0]:
                                supportY = XY[1]

                        con = Confidence(i[1], supportX)
                        if con >= min_Confidence:
                            lif = Lift(supportX, supportY, i[1])
                            lev = Leverage(supportX, supportY, i[1])
                            lows.append([implies(X, Y), lif, lev, con])

        if len(lows) == 0:
            print("There are no Rules have Confidence more than or equal min Confidence")
        else:
            #lable()

            lows.sort(key=sortlift)
            print("Rules sorted bY lift :\n")
            print(tabulate(lows, headers=['Rule', 'Lift', 'Leverage', 'Confidence'], tablefmt="fancy_grid"))

            lows.sort(key=sortlev)
            print("\n\n\nRules sorted bY Leverage :\n")
            print(tabulate(lows, headers=['Rule', 'Lift', 'Leverage', 'Confidence'], tablefmt="fancy_grid"))

    else:
        print("The rules are in the first item set")

#####################################################


f = open("ticdata2000.txt", "r")
original = [[], [], [], [], [], [], [], [], [], [], [], []]

for x in f:
    # m=x[6:28]
    data = x.split("\t")
    original[0].append('A' + data[5])
    original[1].append('B' + data[6])
    original[2].append('C' + data[7])
    original[3].append('D' + data[8])
    original[4].append('E' + data[9])
    original[5].append('F' + data[10])
    original[6].append('G' + data[11])
    original[7].append('H' + data[12])
    original[8].append('I' + data[13])
    original[9].append('J' + data[14])
    original[10].append('K' + data[15])
    original[11].append('L' + data[16])

while 1 :
    get_Rules(original)
