arr=[-4,-1,1,3,5,6,8,11]
target=10
dic={}
for i in arr:
    if target-i in dic:
        print ([i,target-i])
    else:
        dic[i]=True    
