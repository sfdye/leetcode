# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    nums.sort!
    nums.push(9999999)
    max_count = 0
    max_ele = nums[0]
    cur_count = 1
   	for i in 1..nums.size
   		if nums[i] == nums[i-1]
   			cur_count += 1
   		else
   			if cur_count > max_count
   				max_count = cur_count
   				max_ele = nums[i-1]
   			end
   			cur_count = 1
   		end
   	end
   	return max_ele
end
