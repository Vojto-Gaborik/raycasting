import random
from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**4)


class Map:
    def __init__(self, size):
        self.size = size + 2
        self.grid = self.make_map()
        self.random_labyrinth([1, 1])
        #for i in range(len(self.grid)):
        #    print(self.grid[i])
        #print('')
        self.define_endpoint()
        #for i in range(len(self.grid)):
        #    print(self.grid[i])
        #print('')
        self.endpoint = self.find_endpoint()

    def make_map(self):
        grid = []
        for y in range(self.size):
            array = []
            for x in range(self.size):
                if y == 0 or y == self.size - 1:
                    array.append(1)
                elif x == 0 or x == self.size - 1:
                    array.append(1)
                else:
                    array.append(0)
            grid.append(array)
        return grid

    def random_labyrinth(self, position):
        choices = []
        if self.grid[position[1] - 1][position[0]] == 0:
            choices.append('up')
        if self.grid[position[1] + 1][position[0]] == 0:
            choices.append('down')
        if self.grid[position[1]][position[0] + 1] == 0:
            choices.append('right')
        if self.grid[position[1]][position[0] - 1] == 0:
            choices.append('left')
        self.grid[position[1]][position[0]] = 2

        while len(choices) != 0:
            choice = random.choice(choices)
            if choice == 'up':
                if self.grid[position[1] - 1][position[0]] == 0:
                    if self.grid[position[1]][position[0] - 1] == 0:
                        self.grid[position[1]][position[0] - 1] = 1
                    if self.grid[position[1]][position[0] + 1] == 0:
                        self.grid[position[1]][position[0] + 1] = 1
                    self.random_labyrinth([position[0], position[1] - 1])
                choices.pop(choices.index('up'))
            elif choice == 'down':
                if self.grid[position[1] + 1][position[0]] == 0:
                    if self.grid[position[1]][position[0] - 1] == 0:
                        self.grid[position[1]][position[0] - 1] = 1
                    if self.grid[position[1]][position[0] + 1] == 0:
                        self.grid[position[1]][position[0] + 1] = 1
                    self.random_labyrinth([position[0], position[1] + 1])
                choices.pop(choices.index('down'))
            elif choice == 'right':
                if self.grid[position[1]][position[0] + 1] == 0:
                    if self.grid[position[1] - 1][position[0]] == 0:
                        self.grid[position[1] - 1][position[0]] = 1
                    if self.grid[position[1] + 1][position[0]] == 0:
                        self.grid[position[1] + 1][position[0]] = 1
                    self.random_labyrinth([position[0] + 1, position[1]])
                choices.pop(choices.index('right'))
            elif choice == 'left':
                if self.grid[position[1]][position[0] - 1] == 0:
                    if self.grid[position[1] - 1][position[0]] == 0:
                        self.grid[position[1] - 1][position[0]] = 1
                    if self.grid[position[1] + 1][position[0]] == 0:
                        self.grid[position[1] + 1][position[0]] = 1
                    self.random_labyrinth([position[0] - 1, position[1]])
                choices.pop(choices.index('left'))

    def define_endpoint(self):
        choices = deque()
        if self.grid[2][1] == 2:
            choices.append([[1, 2], 4])
        if self.grid[1][2] == 2:
            choices.append([[2, 1], 4])
        self.grid[1][1] = 3
        while len(choices) != 0:
            choice = choices.popleft()
            self.grid[choice[0][1]][choice[0][0]] = choice[1]
            if self.grid[choice[0][1] - 1][choice[0][0]] == 2:
                choices.append([[choice[0][0], choice[0][1] - 1], choice[1] + 1])
            if self.grid[choice[0][1] + 1][choice[0][0]] == 2:
                choices.append([[choice[0][0], choice[0][1] + 1], choice[1] + 1])
            if self.grid[choice[0][1]][choice[0][0] + 1] == 2:
                choices.append([[choice[0][0] + 1, choice[0][1]], choice[1] + 1])
            if self.grid[choice[0][1]][choice[0][0] - 1] == 2:
                choices.append([[choice[0][0] - 1, choice[0][1]], choice[1] + 1])

    def find_endpoint(self):
        maximum = 0
        endpoint = None
        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] != 1:
                    if self.grid[y][x] > maximum:
                        maximum = self.grid[y][x]
                        endpoint = [x, y]
        for y in range(self.size):
            for x in range(self.size):
                #if self.grid[y][x] == maximum and [x, y] == endpoint:
                #    self.grid[y][x] = 0
                if self.grid[y][x] != 1:
                    self.grid[y][x] = 0
        return endpoint


#map = Map(6)
#print('')
#for i in range(len(map.grid)):
#    print(map.grid[i])

