#切片和範圍取值
nums = [10, 20, 30, 40, 50, 60, 70, 80]
ranges = [(1, 4), (3, 6), (5, 8)]
lst=[]
for i in range(len(ranges)):
    lst.extend(nums[ranges[i][0]:ranges[i][1]])
    
for j in range(1,len(lst)-1):
    if lst[j-1]==lst[j-2]:
        lst.remove(lst[j-1])
print(lst)