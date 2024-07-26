'''Given a binary array nums,return the maximum number of consecutive 1's in the
array.'''

nums=list(map(int,input().split()))
count=0
maxC=0

'''for i in nums:
    if i==1:
        count+=1
        maxC=max(maxC,count)
    else:
        count=0
print(maxC)'''

for i in nums:
    if i==1:
        count+=1
        if count > maxC:
            maxC=count
    else:
        count=0
print(maxC)

