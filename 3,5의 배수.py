nums = range(1,5001)
selfnums = set(nums) - set([sum([int(ii) for ii in str(num)]) + num for num in nums])

print (sum(selfnums))