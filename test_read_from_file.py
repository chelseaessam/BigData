def count(arry_x,mim):
    count_arry=[]
    cou=0
    for x in arry_x :
        if ((x,cou)in count_arry)==0:
            cou=arry_x.count(x)
            if cou >= mim:
                Support=cou/len(arry_x)
                E=(x,Support)
                count_arry.append(E)
    return count_arry
f = open("ticdata2000.txt", "r")
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]

for x in f:
    #m=x[6:28]
    data = x.split("\t")
    A.append(int(data[5]))
    B.append(int(data[6]))
    C.append(int(data[7]))
    D.append(int(data[8]))
    E.append(int(data[9]))
    F.append(int(data[10]))
    G.append(int(data[11]))
    H.append(int(data[12]))
    I.append(int(data[13]))
    J.append(int(data[14]))
    K.append(int(data[15]))
    L.append(int(data[16]))


        
  