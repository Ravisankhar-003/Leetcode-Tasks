Class solution(object):
  def twosum(self, nums, target):
    seen={}
    for i,num in enumerate(nums):
      p=target-num
      if p in seen:
        return [seen[p],i]
      seen[num]=i
