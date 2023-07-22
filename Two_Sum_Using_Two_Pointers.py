arr=[-4,-1,1,3,5,6,8,11]
target=-1
arr.sort()
i=0
j=len(arr)-1
while(i<j):
    if (arr[i]+arr[j]) < target:
        i+=1
    elif (arr[i]+arr[j]) > target:
        j-=1
    else:
        print([arr[i],arr[j]])
        break
