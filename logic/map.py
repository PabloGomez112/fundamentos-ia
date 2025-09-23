import random

class Map:
    DIRTY_FLOOR_CHANCE = 10  # %
    BLOCK_WALL_CHANCE = 15

    def __init__(self, cols, rows, rows_padding=0, cols_padding=0):
        self.cols = cols
        self.rows = rows
        self.rows_padding = rows_padding
        self.cols_padding = cols_padding
        self.dirty_cells_count = 0

        # [rows][cols]  <-- clave
        self.map_instance = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.generate_map()


    def set_value_of_cell(self, row, col, value):
        self.map_instance[row][col]  = value

    def generate_map(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if random.randint(1, 100) <= self.DIRTY_FLOOR_CHANCE:
                    self.map_instance[r][c] = 1
                    self.dirty_cells_count += 1

                elif random.randint(1, 100) <= self.BLOCK_WALL_CHANCE:
                    self.map_instance[r][c] = 2

                else:
                    self.map_instance[r][c] = 0
        self.map_instance[0][0] = 0

    def get_cell(self, row, col):  # 1-based
        if 1 <= row <= self.rows and 1 <= col <= self.cols:
            return self.map_instance[row - 1][col - 1]
        return None

    def print_map(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.map_instance[r][c], end=" ")
            print()

