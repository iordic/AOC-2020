from template import Challenge
from abc import ABC, abstractmethod

FILE = "inputs/day02.txt"

# Abstract class for both parts, they have same structure but different algorithms
class TCPolicy(ABC):
    def __init__(self, character, a, b, password):
        self.a = a
        self.b = b
        self.character = character
        self.password = password

    @abstractmethod
    def check(self):
        return NotImplemented

# Part 1
class TCPolicy1(TCPolicy):
    def check(self):
        c = 0
        for i in self.password:
            if self.character == i:
                c += 1
        return c >= self.a and c <= self.b

# Part 2
class TCPolicy2(TCPolicy):
    def check(self):
        index = 1
        c = 0
        for i in self.password:
            if i == self.character and (index == self.a or self.b == index):
                c += 1
            index += 1
        return c == 1

class Day2(Challenge):
    def execute(self):
        count1 = 0
        count2 = 0
        for i in self.content:
            values = i.strip().split(" ")
            pwd = values[-1]
            character = values[1].rstrip(":")
            param1 = int(values[0].split("-")[0])
            param2 = int(values[0].split("-")[1])

            tcpol1 = TCPolicy1(character, param1, param2, pwd)
            tcpol2 = TCPolicy2(character, param1, param2, pwd)

            check1 = tcpol1.check()
            check2 = tcpol2.check()
            #print(i.strip(),"-", check)    # Debugging
            if check1:
                count1 += 1
            if check2:
                count2 += 1

        print("Count from part1: {}".format(count1))
        print("Count from part2: {}".format(count2))

if __name__ == '__main__':
    d = Day2(FILE)
    d.execute()
