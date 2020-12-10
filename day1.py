from template import Challenge
import math

FILE = "inputs/day01.txt"

# General solution given N numbers and X target
def entry_search(target, entries, level, result):
    if level == 0:
        return sum(result) == target
    for i in entries:
        result.append(i)
        if entry_search(target, entries, level - 1, result):
            return result
        result.pop()

class Day1(Challenge):
    def execute(self):
        values = []
        result1 = []
        result2 = []
        for i in self.content:
            values.append(int(i.strip()))
        res1 = entry_search(2020, values, 2, result1)
        res2 = entry_search(2020, values, 3, result2)
        
        # Print results
        print("Result for part 1: {}; Multiplication: {}.".format(result1, math.prod(result1)))
        print("Result for part 2: {}; Multiplication: {}.".format(result2, math.prod(result2)))


if __name__ == '__main__':
    d = Day1(FILE)
    d.execute()