from Gui import graphics as game_graphic_engine
from logic import map as game_map
from config import *
from agent_controller import AgentController

if __name__ == "__main__":
    main_map = game_map.Map(rows=CELLS_ROW_SIZE,
                            cols=CELLS_COLUMN_SIZE,
                            rows_padding=ROWS_PADDING,
                            cols_padding=COLS_PADDING)

    agent_controller = AgentController(map_instance=main_map)

    main_environment = game_graphic_engine.App(rows=CELLS_ROW_SIZE,
                                               cols=CELLS_COLUMN_SIZE,
                                               window_width=WINDOW_WIDTH,
                                               window_height=WINDOW_HEIGHT,
                                               map_instance=main_map,
                                               game_controller=agent_controller)


    main_environment.set_background_color((189, 236, 255))
    main_environment.on_execute()
