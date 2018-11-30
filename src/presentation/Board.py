import pickle

class Board:
    def __init__(self):
        with open("./points.txt", "rb") as fp:
            self.board = pickle.load(fp)
        self.shops = [x for x in self.board if (x[2] == 'Shop')]
        self.entrances = [x for x in self.board if (x[2] == 'Entrances')]
        self.max_width = 800
        self.max_height = 200
        self.min_width = 1
        self.min_height = 1

    def is_destination_available(self, new_x, new_y):
        new_point = (new_x, new_y, 'Wall')
        is_valid = False if new_point in self.board else True
        return is_valid and self._in_the_board(new_x, new_y)

    def _in_the_board(self, new_x, new_y):
        if new_y in range(0, self.max_height):
                if new_x in range(0, self.max_width):
                    return True
        return False

    def get_shops(self):
        return self.shops


