def max_end3(nums):
  first = nums[0]
  last = nums[len(nums)-1]
  greater = 0
  if first > last:
    greater = first
  else:
    greater = last
    
  for x in range(0, len(nums)):
    nums[x] = greater
  return nums
