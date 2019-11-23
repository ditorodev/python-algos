import sys

class MaxStack:
  def __init__(self):
    # Fill this in.
    self.values = []

  def push(self, val):
    # Fill this in.
    self.values.append(val);
    return val

  def pop(self):
    # Fill this in.
    if not len(self.values) > 0:
        return None 

    lastValue = self.values[-1];
    self.values = self.values[:len(self.values) - 1]

    return lastValue;

  def max(self):
    # Fill this in.
    max = -1 - sys.maxsize
    for val in self.values:
        if val > max:
            max = val
    return max

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2