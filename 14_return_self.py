# call functions in cascade
class Counter(object):
    def __init__(self, start=1):
        self.val = start
    def increment(self):
        self.val += 1
        return self
    def decrement(self):
        self.val -= 1
        return self
    
c=Counter()
c.increment().increment().decrement().decrement() #cascade

print(c.val)
