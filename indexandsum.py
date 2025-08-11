# 3. Count and Index Methods:
# Given a tuple nums = (1, 2, 3, 2, 4, 2, 5), use tuple methods to:
# ● Count how many times 2 occurs
# ● Find the index of the first occurrence of 2

nums = (1, 2, 3, 2, 4, 2, 5)
count=0
index=0
for x in nums:
    if x == 2:
        index=nums.index(x)
        count +=1
print(f"count of the number 2 is {count} , index is {index} ")

# another method wouldve been 
print(nums.count(2))
# to calc the 2nd occurence
print(f"2nd index of number 2 is: {nums.index(2,2)}")