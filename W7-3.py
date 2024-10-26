#兩和
nums=list(map(int,input('輸入 : nums= ').split(',')))
target=int(input('target= '))
ans=[]
if len(nums)==2:
    if nums[0]+nums[1]==target :
            ans=[0,1]
else:
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i]+nums[j]==target :
                ans.append(nums.index(nums[i]))
                ans.append(nums.index(nums[j]))
                break
        if ans!=[]:
            break
if ans!=[]:
    print('輸出 :',ans)
else:
    print('沒有找到符合的組合')