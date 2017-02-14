class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if len(self.second) != 0:
            a1 = self.second.pop()
            self.second.append(a1)
            return a1
            
        while len(self.first)!=0:
            self.second.append(self.first.pop())
        return self.second[-1]
        
        
    def pop(self):
        if len(self.second) != 0:
            return self.second.pop()
        while len(self.first)!=0:
            self.second.append(self.first.pop())
        self.second.pop()
        
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
