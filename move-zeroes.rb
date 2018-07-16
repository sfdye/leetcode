# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
	size_before = nums.size
	nums.each do |num|
		if num == 0 then 
			nums.delete(num)
		end
	end
	for i in 0..size_before-nums.size-1
		nums.push(0)
	end
    return nums
end

