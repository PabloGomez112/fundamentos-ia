from config import *

def get_pixels_from_coordinates(row, col):
    """
    :param row: The number of col
    :param col: The number of row
    :return: tuple (x, y) in pixels from screen in the center of the cell
    """

    if 0 < row <= CELLS_ROW_SIZE:
        if 0 < col <= CELLS_COLUMN_SIZE:
            return (COLS_PADDING * col), (ROWS_PADDING * row)

