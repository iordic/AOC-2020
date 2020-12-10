from template import Challenge

FILE = "inputs/day03.txt"

class Ski:
    def __init__(self, content, pos, movX, movY):
        self.cols = len(content[0].strip())
        self.rows = len(content)
        self.movX = movX
        self.movY = movY
        self.map = []
        self.pos = pos
        for i in content:
            self.map.append(list(i.strip()))

    def __str__(self):
        """ For debugging """
        map_repr = ""
        for i in self.map:
            map_repr += "".join(i) + "\n"
        return map_repr

    def execute(self):
        trees = 0
        while self.pos[0] < self.rows:
            self.pos[1] %= self.cols   # reset position
            element = self.map[self.pos[0]][self.pos[1]]
            if element == "#":
                self.map[self.pos[0]][self.pos[1]] = 'X'
                trees += 1
            elif element == ".":
                self.map[self.pos[0]][self.pos[1]] = 'O'
            self.pos[0] += self.movX
            self.pos[1] += self.movY
        return trees

class Day3(Challenge):
    def execute(self):
        ski1 = Ski(self.content, [0,0], 1, 1)
        ski2 = Ski(self.content, [0,0], 1, 3)    # First part
        ski3 = Ski(self.content, [0,0], 1, 5)
        ski4 = Ski(self.content, [0,0], 1, 7)
        ski5 = Ski(self.content, [0,0], 2, 1)
        a,b,c,d,e = ski1.execute(), ski2.execute(), ski3.execute(), ski4.execute(), ski5.execute()
        print("Part 1: ", b)
        print("Part 2:", a, "*", b, "*", c, "*", d, "*", e, "=", a*b*c*d*e)

if __name__ == '__main__':
    d = Day3(FILE)
    d.execute()
