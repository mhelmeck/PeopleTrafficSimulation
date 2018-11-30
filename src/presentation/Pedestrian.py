import random
import threading

max_height = 800
max_width = 200


class Pedestrian:
    def __init__(self, pid, board, position):
        self.id = pid
        self.board = board
        self.shops = board.get_shops()
        self.x = position[0]
        self.y = position[1]
        self.step = 5
        self.size = 5
        self.path = []

    # Aka toString
    def __repr__(self):
        return 'ID: {} on {} {}'.format(str(self.id), str(self.x), str(self.y))

    def _set_new_position(self, direction):
        if direction == "N":
            if self.board.is_destination_available(self.x, self.y - self.step):
                self.y -= self.step
        if direction == "S":
            if self.board.is_destination_available(self.x, self.y + self.step):
                self.y += self.step
        if direction == "W":
            if self.board.is_destination_available(self.x - self.step, self.y):
                self.x -= self.step
        if direction == "E":
            if self.board.is_destination_available(self.x + self.step, self.y):
                self.x += self.step

    def random_move(self):
        val = random.randint(1, 4)
        if val == 1:
            return self._set_new_position("N")
        if val == 2:
            return self._set_new_position("E")
        if val == 3:
            return self._set_new_position("S")
        if val == 4:
            return self._set_new_position("W")

    def _generate_path(self, destination):
        return self.path

    def move(self):
        destination = random.choice(self.shops)
        t = threading.Thread(target=self._generate_path, args=(destination,))
        t.start()
        t.join()
        if not self.path:
            self.random_move()
        else:
            self._set_new_position(self.path.pop(0))
        # new Thread & execute a* algorithm creating List of Strings e.g. ["N", "E", "E", ...]
        # if path == [] then random_move
