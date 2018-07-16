# @param {Integer} n, a positive integer
# @return {Integer}
def hamming_weight(n)
	weight = 0
	while n != 0
		if n % 2 == 1
			weight += 1
		end
		n /= 2
	end
	return weight
end	
