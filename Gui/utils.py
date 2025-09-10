from config import CELLS_ROW_SIZE, CELLS_COLUMN_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT

CELL_W = WINDOW_WIDTH  // CELLS_COLUMN_SIZE
CELL_H = WINDOW_HEIGHT // CELLS_ROW_SIZE

def get_pixels_from_coordinates(row, col, center=True, one_based=True):
    # valida indices
    if one_based:
        if not (1 <= row <= CELLS_ROW_SIZE and 1 <= col <= CELLS_COLUMN_SIZE):
            return None
        row -= 1; col -= 1
    else:
        if not (0 <= row < CELLS_ROW_SIZE and 0 <= col < CELLS_COLUMN_SIZE):
            return None

    x = col * CELL_W
    y = row * CELL_H
    if center:
        x += CELL_W // 2
        y += CELL_H // 2
    return x, y

