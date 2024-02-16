'''.Create a class Counter with an instance method increment() that increments
 a class variable count by 1 using self.'''

class Counter:
    count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
c.increment()
print(c.count)