def rotate_left3(nums):
  n = nums[0]
  nums = nums[1:]
  nums.append(n)
  return nums
