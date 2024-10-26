##挑戰2.找出連續的⼦列表
nums=list(map(int,input('輸入 : nums= ').split(',')))
target=7
ans=[]

for i in range (len(nums)):
    x=0
    for j in range (i,len(nums)):
        x+=nums[j]
        if x>=target:
            ans.append(nums[i:j+1])

                

if ans!=[]:
    print('輸出 :',ans)
else:
    print('沒有找到符合的組合')