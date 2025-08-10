# given a list of numbers, checks to see if any 2 of then add up to a target

nums = [3,2,4]
target = 6
hash_map = {}
for i, num in enumerate(nums):
    looking_for = target - num
    if looking_for in hash_map:
        print(hash_map[looking_for], i)
    hash_map[num] = i