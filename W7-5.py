#挑戰1.為零的三元組
nums=list(map(int,input('輸入 : nums= ').split(',')))
target=0
ans=[]
nums.sort()
for i in range (len(nums)):
    for j in range (i+1,len(nums)):
        for k in range (j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target :
                ans.append([nums[i],nums[j],nums[k]])
                
for t in range(1,len(ans)):
    if ans[t]==ans[t-1]:
        ans.pop(t-1)

if ans!=[]:
    print('輸出 :',ans)
else:
    print('沒有找到符合的組合')