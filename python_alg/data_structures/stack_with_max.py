'''
Implement a stack that keeps track of the max value in the stack
'''
# All methods have time complexity of O(1)
# additional space is added

class Stack:
    ElementwithCachedMax =  collections.namedtuple(
        'ElementwithCachedMax', ('element', 'max')
    )

    def __init__(self):
        self._element_with_cached_max = []

    def is_empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.is_empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.is_empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element
    
    def push(self, x):
        self._element_with_cached_max.append(
            Stack.ElementwithCachedMax(x,x if self.is_empty() else max(x, self.max())
        )