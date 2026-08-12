"""You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# 2 pointer

for i in nums:
    print(i)

enumerate -  for i,v in enumerate(nums):
                print(i,v)
                if target == nums[i1] + nums[i2]:
                    return [i1,i2]

"""

# nums = [2,11,15,7,0,4,5]
# [3,3,4,5] target = 6
# [0,1] [0,0]

nums = [3, 5, 2, 8, 1, 4, 7, 6, 10, 9]

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums.sort()
print(nums)
#our ans = [7,9] [7,8]
target = 15

# target = 9

break_loops = False

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        print(i,j)
        print(nums[i] + nums[j])
        if nums[i] + nums[j] == target:
            print(f' the result is - {[i,j]}')
            break_loops = True
            break
    if break_loops:
        break