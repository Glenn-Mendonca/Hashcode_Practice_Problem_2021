#Functions
import sys

# Variable input
M,T2,T3,T4 = input().split()
ingredients = [] 
for i in range(int(M)): 
    col = []  
    col = (input().split(' '))
    col.append(i)
    ingredients.append(col)

ingredients=sorted(ingredients, key=lambda x:x[0], reverse=True) 

# Set Conversion
ingred_set=[]
for i in range(int(M)):
    a=set()
    for j in range(1,len(ingredients[i])):
        a.add(ingredients[i][j])
    ingred_set.append(a)


# All variables
inter = -1

del_4_team = 0
pizdel4arr = []
pd4 = True

del_3_team = 0
pizdel3arr = []
pd3 = True

del_2_team = 0
pizdel2arr = []
pd2 = True

# Loop to deliver pizzas as much available
while((int(M)>1 and int(T2)>0) or (int(M)>3 and int(T4)>0) or  (int(M)>2 and int(T3)>0)):

# Number of intersections allowed
    inter  = inter + 1

# Resetting pd's
    pd4 = True
    pd3 = True
    pd2 = True

# 4 membered team
    while(pd4):
        if((int(T4) > 0) and (int(M) > 3)):
            for i in range(int(M)-3):
                for j in range(int(i+1),int(M)-2):
                    for k in range(int(j+1),int(M)-1):
                        for l in range(int(k+1),int(M)):    
                            pd4 = False
                            templist = [ingred_set[i],ingred_set[j],ingred_set[k],ingred_set[l]]
                            temp4inter = {0}
                            for a1 in range(3):
                                for b1 in range(int(i+1),4):
                                    temp4inter = temp4inter.union(templist[a1].intersection(templist[b1]))
                            temp=len(temp4inter)-1
                            if(temp == inter) and (int(T4) > 0):
                                M = int(M) - 4
                                T4 = int(T4) - 1
                                temp4 = []
                                for intcheck in ingred_set[i]:
                                    if type(intcheck) is int:
                                        temp4.append(intcheck)
                                for intcheck in ingred_set[j]:
                                    if type(intcheck) is int:
                                        temp4.append(intcheck)
                                for intcheck in ingred_set[k]:
                                    if type(intcheck) is int:
                                        temp4.append(intcheck)
                                for intcheck in ingred_set[l]:
                                    if type(intcheck) is int:
                                        temp4.append(intcheck)
                                pizdel4arr.append(temp4)
                                ingred_set.pop(i)
                                ingred_set.pop(j-1)
                                ingred_set.pop(k-2)
                                ingred_set.pop(l-3) 
                                del_4_team = del_4_team + 1
                                pd4 = True
                            if pd4:
                                break
                        if pd4:
                                break
                    if pd4:
                        break
                if pd4:
                    break
        else:
            pd4 = False

# 3 membered team
    while(pd3):
        if((int(T3) > 0) and (int(M) > 2)):
            for i in range(int(M)-2):
                for j in range(int(i+1),int(M)-1):
                    for k in range(int(j+1),int(M)):
                        pd3 = False
                        templist = [ingred_set[i],ingred_set[j],ingred_set[k]]
                        temp3inter = {0}
                        for n in range(2):
                            for m in range(int(i+1),3):
                                temp3inter = temp3inter.union(templist[n].intersection(templist[m]))
                        temp=len(temp3inter)-1
                        if(temp == inter) and (int(T3) > 0):
                            M = int(M) - 3
                            T3 = int(T3) - 1
                            temp3 = []
                            for intcheck in ingred_set[i]:
                                if type(intcheck) is int:
                                    temp3.append(intcheck)
                            for intcheck in ingred_set[j]:
                                if type(intcheck) is int:
                                    temp3.append(intcheck)
                            for intcheck in ingred_set[k]:
                                if type(intcheck) is int:
                                    temp3.append(intcheck)
                            pizdel3arr.append(temp3)
                            ingred_set.pop(i)
                            ingred_set.pop(j-1)
                            ingred_set.pop(k-2) 
                            del_3_team = del_3_team + 1
                            pd3 = True
                        if pd3:
                            break
                    if pd3:
                        break
                if pd3:
                    break
        else:
            pd3 = False
    
# 2 membered team                      
    while(pd2):
        if((int(T2) > 0) and (int(M) > 1)):
            for i in range(int(M)-1):
                for j in range(int(i+1),int(M)):
                    pd2 = False
                    temp = len(ingred_set[i].intersection(ingred_set[j]))
                    if((int(temp) == inter) and (int(T2) > 0)):
                        M = int(M) - 2
                        T2 = int(T2) - 1
                        temp2 = []
                        for intcheck in ingred_set[i]:
                            if type(intcheck) is int:
                                temp2.append(intcheck)
                        for intcheck in ingred_set[j]:
                            if type(intcheck) is int:
                                temp2.append(intcheck)
                        pizdel2arr.append(temp2)
                        ingred_set.pop(i)
                        ingred_set.pop(j-1)
                        del_2_team = del_2_team + 1
                        pd2 = True
                    if pd2:
                        break
                if pd2:
                    break
        else:
            pd2 = False

# Output
outputfile = open('test.txt', 'w')
print(del_4_team + del_3_team + del_2_team,file = outputfile)
for i in range(del_2_team):
    print(2,end=' ',file = outputfile)
    for j in range(2):
        print(pizdel2arr[i][j],end=' ',file = outputfile)
    print(file = outputfile)
for i in range(del_3_team):
    print(3,end=' ',file = outputfile)
    for j in range(3):
        print(pizdel3arr[i][j],end=' ',file = outputfile)
    print(file = outputfile)
for i in range(del_4_team):
    print(4,end=' ',file = outputfile)
    for j in range(4):
        print(pizdel4arr[i][j],end=' ',file = outputfile)  
    print(file = outputfile)     
outputfile.close()
