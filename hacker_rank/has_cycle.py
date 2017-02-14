
class Node(object):
    def __init__(self, data = None, next_node = None):
       self.data = data
       self.next = next_node

def has_cycle(head):
   
   node = head
   keeping_track = {}

   while node is not None:
       if keeping_track.get(node.data,None) != None:
           return True
       else:
           keeping_track[node.data] = 1
           node = node.next
   return False
           