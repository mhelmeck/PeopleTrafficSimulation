import random

max_height = 800
max_width = 200


class Pedestrian:
    def __init__(self, pid, board, position):
        self.id = pid
        self.board = board
        self.x = position[0]
        self.y = position[1]
        self.step = 5
        self.size = 5

    # Aka toString
    def __repr__(self):
        return 'ID: {} on {} {}'.format(str(self.id), str(self.x), str(self.y))

    def _set_new_position(self, direction):
        print(str(self.x), str(self.y), str(self.size))
        if direction == "N":
            if self.y >= self.step and self.board.is_destination_available(self.x, self.y - self.step):
                self.y -= self.step
        if direction == "S":
            new_step = self.size + self.step
            if self.y <= max_height - new_step and self.board.is_destination_available(self.x, self.y + self.step):
                self.y += self.step
        if direction == "W":
            if self.x >= self.step and self.board.is_destination_available(self.x - self.step, self.y):
                self.x -= self.step
        if direction == "E":
            new_step = self.size + self.step
            if self.x <= max_width - new_step and self.board.is_destination_available(self.x + self.step, self.y):
                self.x += self.step

    def random_move(self):
        val = random.randint(1, 40)
        if val in range(1, 11):
            return self._set_new_position("N")
        if val in range(11, 21):
            return self._set_new_position("E")
        if val in range(21, 31):
            return self._set_new_position("S")
        if val in range(31, 41):
            return self._set_new_position("W")
