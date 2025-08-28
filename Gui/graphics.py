import pygame
from logic import map
from Gui.utils import get_pixels_from_coordinates

class App:
    def __init__(self, cols, rows, window_height, window_width, map_instance: map.Map, game_controller):
        self._running = True
        self._display_surf = None
        self.background_color = (255, 255, 255)
        self.size = self.width, self.height = window_width, window_height
        pygame.display.set_caption("Agente Aspiradora")
        self.rows = rows
        self.cols = cols
        self.rows_spacing = self.size[1] // self.rows
        self.cols_spacing = self.size[0] // self.cols
        self.map_instance = map_instance
        self.agent_controller = game_controller

        #Resources

        self.robot_image = pygame.image.load('./images/robot.png', "Robot")
        self.robot_image_scaled = pygame.transform.scale(self.robot_image,
                                                         (self.cols_spacing, self.rows_spacing))

        self.garbage_image = pygame.image.load('./images/garbage.png', "Garbage")
        self.garbage_image_scaled = pygame.transform.scale(self.garbage_image,
                                                         (self.cols_spacing, self.rows_spacing))

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
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
        if not self.on_init():
                self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.time.wait(200)
        self.on_cleanup()

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

    def _draw_background(self, color):
        """
        :param color:
        :return:
        """
        self._display_surf: pygame.display
        self._display_surf.fill(color)

    def set_grid_size(self, rows, cols):
        self.rows = rows
        self.cols = cols



    def _draw_map(self):
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.draw_garbage(i, j, self.map_instance.get_cell(i, j))

    def _draw_agent(self, row, col):
        pixel_x, pixel_y = get_pixels_from_coordinates(row, col)

        pixel_x -= self.cols_spacing // 2
        pixel_y -= self.rows_spacing // 2

        image_rect = self.robot_image_scaled.get_rect()
        image_rect.center = (image_rect.x // 2, image_rect.y // 2)
        self._display_surf.blit(self.robot_image_scaled, (image_rect.x + pixel_x, image_rect.y + pixel_y))

    def _draw_grid(self):
        for i in range(self.rows):
            pygame.draw.line(self._display_surf,
                             (0, 0, 0),
                             (self.rows_spacing * i, 0),
                             (self.rows_spacing * i, self.height), 2)
            for j in range(self.cols):
                pygame.draw.line(self._display_surf,
                                 (0, 0, 0),
                                 (0, self.cols_spacing * j),
                                 (self.width, self.cols_spacing * j), 2)
