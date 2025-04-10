nums = [1,3,5,6]
target = 7

result = 0
def a(nums,target):
    for i,v in enumerate(nums):
        if v >= target:
            return i
    return i + 1

print(a(nums,target)) 
