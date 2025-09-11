import random

import pygame.time

from logic.map import Map
from config import CELLS_ROW_SIZE, CELLS_COLUMN_SIZE

class AgentController:
    def __init__(self, map_instance: Map):
        self.map_instance = map_instance
        self.agent_x = 1
        self.agent_y = 1
<<<<<<< HEAD
        self.movement_count=0;
=======
>>>>>>> 5e9092c5f9014c8d2ba8776bc3824ff4159c5deb

    def update(self):
        f = random.choice([self.move_agent_left, self.move_agent_down, self.move_agent_right,
                          self.move_agent_up])
<<<<<<< HEAD
        self.movement_count+=1
=======

>>>>>>> 5e9092c5f9014c8d2ba8776bc3824ff4159c5deb
        f()

        pass

    def move_agent_left(self):
        if self._can_move_left():
            self.agent_x -= 1

    def move_agent_right(self):
        if self._can_move_right():
            self.agent_x += 1

    def move_agent_up(self):
        if self._can_move_down():
            self.agent_y += 1

    def move_agent_down(self):
        if self._can_move_up():
            self.agent_y -= 1

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
<<<<<<< HEAD
        return self.agent_x, self.agent_y
=======
        return self.agent_x, self.agent_y

>>>>>>> 5e9092c5f9014c8d2ba8776bc3824ff4159c5deb
