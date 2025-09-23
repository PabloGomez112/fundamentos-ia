from logic.map import Map
from config import CELLS_ROW_SIZE, CELLS_COLUMN_SIZE


def is_equal_coord(a, b):
    return a[0] == b[0] and a[1] == b[1]

def already_visited(node, visited):
    for v in visited:
        if is_equal_coord(v, node):
            return True

    return False


class AgentController:
    def __init__(self, map_instance: Map):
        self.map_instance = map_instance
        self.agent_x = 1
        self.agent_y = 1

        self.pathfinder_position = (1, 1)

        self.movement_count=0
        self.garbage_founded = 0

        self.state = "right"
        self.finding_path = True
        self.path = []
        self.current_cursor = 0

        self.path_find()
        print(self.path)
        self.previous_position = None

    def update(self):
        if not self.is_clean():
            self.clear()
        if self.previous_position is not None:
            self.burn_cell()

        if self.current_cursor < len(self.path):
            self.agent_move_direct(self.path[self.current_cursor])
            self.current_cursor += 1

        self.previous_position = self.get_agent_position()


    def path_find(self):
        #Current, Path, Visited, Garbage
        stack = [(self.pathfinder_position, [self.pathfinder_position], [], 0)]
        best = None

        while stack:
            node, path, visited, garbage_found = stack.pop()

            _visited = visited.copy()

            _visited.append(node)

            # print(garbage_found, ' / ', self.map_instance.dirty_cells_count)


            if not self.is_clean_coord(node):
                garbage_found += 1
                if best is None or best[3] < garbage_found:
                    best = (node, path, _visited, garbage_found)

                if garbage_found == self.map_instance.dirty_cells_count:
                    self.path = path
                    return True

            left = (node[0] - 1, node[1])
            right = (node[0] + 1, node[1])
            up = (node[0], node[1] + 1)
            down = (node[0], node[1] - 1)

            directions = (left, right, up, down)

            for next_move in directions:
                if self.is_valid_coord(next_move) and not already_visited(next_move, _visited):
                    stack.append((next_move, path + [next_move], _visited, garbage_found))

        self.path = best[1]


    def clear(self):
        self.map_instance.set_value_of_cell(self.agent_y-1, self.agent_x-1, 0)

    def move_agent_left(self):
        if self._can_move_left():
            self.agent_x -= 1
            return True

        return False

    def move_agent_right(self):
        if self._can_move_right():
            self.agent_x += 1
            return True
        return False

    def move_agent_up(self):
        if self._can_move_up():
            self.agent_y -= 1
            return True
        return False

    def move_agent_down(self):
        if self._can_move_down():
            self.agent_y += 1
            return True
        return False

    def _can_move_right(self):
        if self.agent_x + 1 <= CELLS_COLUMN_SIZE:
            can_move = True
        else:
            can_move = False

        return can_move

    def _can_move_left(self):
        if self.agent_x - 1 > 0:
            can_move = True
        else:
            can_move = False

        return can_move

    def _can_move_up(self):
        if self.agent_y - 1 > 0:
            can_move = True
        else:
            can_move = False

        return can_move

    def _can_move_down(self):
        if self.agent_y + 1 <= CELLS_ROW_SIZE:
            can_move = True
        else:
            can_move = False

        return can_move

    def get_agent_position(self):
        return self.agent_x, self.agent_y

    def is_clean(self):
        value = self.map_instance.get_cell(self.agent_y,self.agent_x)
        return value == 0

    def is_clean_coord(self, coord):
        value = self.map_instance.get_cell(coord[1], coord[0])
        return value == 0 or value == 2

    def agent_move_direct(self, coords):
        self.agent_x, self.agent_y = coords[0], coords[1]

    def is_valid_coord(self, coord):
        return (1 <= coord[0] <= CELLS_COLUMN_SIZE and 1 <= coord[1] <= CELLS_ROW_SIZE and
                self.map_instance.get_cell(coord[1], coord[0]) != 2)

    def burn_cell(self):
        self.map_instance.set_value_of_cell(self.previous_position[1] - 1, self.previous_position[0] - 1, 3)
