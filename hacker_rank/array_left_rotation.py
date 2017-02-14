def array_left_rotation(a, n, k):
  
    new_array = a[k:] + a[:k]
    return new_array
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

# def check_binary_search_tree_(root):
#     return check_bst(root,None,None)

# def check_bst(node,mini,maxi):
#     right, left = True, True
#     if (maxi is not None and node.data >= maxi):
#         return False
#     if (mini is not None and node.data <= mini):
#         return False
#     if node.right:
#         if mini == None:
#             mini = node.data
#         right = check_bst(node.right,min(mini,node.data),maxi)
#     if node.left:
#         left = check_bst(node.left,mini,max(maxi,node.data))
#     return right and left



