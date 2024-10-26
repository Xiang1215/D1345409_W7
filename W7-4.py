#偶數平方表
nums=list(map(int,input('輸入 : nums= ').split(',')))

a=[]
for i in range(len(nums)):
    if nums[i]%2==0:
        x=nums[i]**2
        a.append(x)

print(a)