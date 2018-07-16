# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(p, q)
	ret = true
    if dfs(p, q) == false then 
    	ret = false
    end
    return ret
end

def dfs(root_p, root_q)
	if root_p == nil and root_q != nil then 
		return false
	elsif root_p != nil and root_q == nil then 
		return false
	elsif root_p == nil and root_q == nil
		return true
	else
		if root_p.val != root_q.val then
			return false
		else 
			return dfs(root_p.left, root_q.left) && dfs(root_p.right, root_q.right)
		end
	end
end
