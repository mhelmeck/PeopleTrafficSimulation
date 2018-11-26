import pickle

class Board:
    def __init__(self):
        with open("./points.txt", "rb") as fp:
            self.board = pickle.load(fp)
        self.max_width = 800
        self.max_height = 200
        self.min_width = 1
        self.min_height = 1

    def is_destination_available(self, new_x, new_y):
        new_point = (new_x, new_y, 'Wall')
        is_valid = False if new_point in self.board else True
        return is_valid
