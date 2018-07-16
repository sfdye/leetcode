require 'set'
# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
  return nums.to_set.to_a.size != nums.size if nums.size > 0 else false
end


