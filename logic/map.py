import random

class Map:
    DIRTY_FLOOR_CHANCE = 30  # IN PERCENTAGE

    def __init__(self, cols, rows, rows_padding, cols_padding):
        self.cols = cols
        self.rows = rows
        self.map_instance = [[0 for _ in range(rows)] for _ in range(cols)]
        self.generate_map()
        self.print_map()
        self.rows_padding = rows_padding
        self.cols_padding = cols_padding

    def generate_map(self):
        for i in range(self.rows):
            for j in range(self.cols):
                chance = random.randint(0, 100)
                if chance <= self.DIRTY_FLOOR_CHANCE:
                    self.map_instance[i][j] = 1
        self.map_instance[0][0] = 0

    def get_cell(self, row, col):
        if 1 <= row <= self.rows:
            if 1 <= col <= self.cols:
                return self.map_instance[row - 1][col - 1]

    def print_map(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.map_instance[i][j], end=" ")
            print("")