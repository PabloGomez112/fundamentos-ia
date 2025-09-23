# Gui/graphics.py
import pygame
from logic import map
from Gui.utils import get_pixels_from_coordinates

class App:
    def __init__(self, cols, rows, window_height, window_width, map_instance: map.Map, game_controller):
        # En __init__ solo declaramos las variables, no usamos funciones de pygame
        self._running = True
        self._display_surf = None
        self.background_color = (255, 255, 255)
        self.size = self.width, self.height = window_width, window_height
        self.rows = rows
        self.cols = cols
        self.rows_spacing = self.size[1] // self.rows
        self.cols_spacing = self.size[0] // self.cols
        self.map_instance = map_instance
        self.agent_controller = game_controller

        self.robot_image_scaled = None
        self.garbage_image_scaled = None
        self.rock_image_scaled = None
        self.barrier_image_scaled = None


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        pygame.display.set_caption("Agente Aspiradora")

        robot_image = pygame.image.load('./images/robot.png', "Robot")
        self.robot_image_scaled = pygame.transform.scale(robot_image,
                                                         (self.cols_spacing, self.rows_spacing))

        garbage_image = pygame.image.load('./images/garbage.png', "Garbage")
        self.garbage_image_scaled = pygame.transform.scale(garbage_image,
                                                         (self.cols_spacing, self.rows_spacing))

        rock_image = pygame.image.load('./images/rock.png', 'Rock')
        self.rock_image_scaled = pygame.transform.scale(rock_image, (self.cols_spacing, self.rows_spacing))

        barrier_image = pygame.image.load('./images/barrier.png', 'Barrier')
        self.barrier_image_scaled = pygame.transform.scale(barrier_image, (self.cols_spacing, self.rows_spacing))

        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.agent_controller.update()

    def on_render(self):
        self._draw_background(self.background_color)
        self._draw_grid()
        self._draw_map()
        col, row = self.agent_controller.get_agent_position()
        self._draw_agent(row, col)


        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.time.wait(400)

        self.on_cleanup()


    def _draw_background(self, color):
        self._display_surf.fill(color)

    def _draw_grid(self):
        color = (0, 0, 0)

        for c in range(self.cols + 1):
            x = c * self.cols_spacing
            pygame.draw.line(self._display_surf, color, (x, 0), (x, self.height), 2)

        for r in range(self.rows + 1):
            y = r * self.rows_spacing
            pygame.draw.line(self._display_surf, color, (0, y), (self.width, y), 2)

    def _draw_map(self):
        # Map.get_cell usa indices 1-based
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self._draw_garbage(i, j, self.map_instance.get_cell(i, j))

    def _draw_garbage(self, row, col, cell_content):
        if cell_content == 1:
            px, py = get_pixels_from_coordinates(row, col, center=True, one_based=True)
            rect = self.garbage_image_scaled.get_rect(center=(px, py))
            self._display_surf.blit(self.garbage_image_scaled, rect.topleft)
        elif cell_content == 2:
            px, py = get_pixels_from_coordinates(row, col, center=True, one_based=True)
            rect = self.rock_image_scaled.get_rect(center=(px, py))
            self._display_surf.blit(self.rock_image_scaled, rect.topleft)
        elif cell_content == 3:
            px, py = get_pixels_from_coordinates(row, col, center=True, one_based=True)
            rect = self.barrier_image_scaled.get_rect(center=(px, py))
            self._display_surf.blit(self.barrier_image_scaled, rect.topleft)

        else:
            return

    def _draw_agent(self, row, col):
        px, py = get_pixels_from_coordinates(row, col, center=True, one_based=True)
        rect = self.robot_image_scaled.get_rect(center=(px, py))
        self._display_surf.blit(self.robot_image_scaled, rect.topleft)

    def draw_garbage(self, row, col, cell_content):
        if cell_content != 1:
            return

        pixel_x, pixel_y = get_pixels_from_coordinates(row, col)

        pixel_x -= self.cols_spacing // 2
        pixel_y -= self.rows_spacing // 2


        image_rect = self.garbage_image_scaled.get_rect()
        image_rect.center = (image_rect.x // 2, image_rect.y // 2)

        self._display_surf.blit(self.garbage_image_scaled, (image_rect.x + pixel_x, image_rect.y + pixel_y))

    def set_background_color(self, color: tuple):
        self.background_color = color
    def set_grid_size(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.rows_spacing = self.height // self.rows
        self.cols_spacing = self.width  // self.cols