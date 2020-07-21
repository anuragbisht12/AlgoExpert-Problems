# O(2^n) time and O(2^n) space complexity
def find_subsets(nums):
  subsets=[]
  subsets.append([])
  for currentnum in nums:
    for i in range(len(subsets)):
      set=list(subsets[i])
      set.append(currentnum)
      subsets.append(set)
  return subsets
