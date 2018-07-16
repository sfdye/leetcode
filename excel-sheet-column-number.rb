# @param {String} s
# @return {Integer}
def title_to_number(s)
  sum = 0
  a = 1
  s.chars.reverse.each do |c|
    sum += (c.ord - 'A'.ord + 1) * a
    a *= 26
  end
  return sum
end
