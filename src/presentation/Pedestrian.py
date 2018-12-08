import random
import threading
from heapq import heappush, heappop


class Pedestrian:
    def __init__(self, pid, board, position):
        self.id = pid
        self.board = board
        self.shops = board.get_shops()
        self.x = position[0]
        self.y = position[1]
        self.step = 1
        self.path = []
        self.generating_path = False
        self.threads = []

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

    def _increment_for(self, new_x, new_y):
        if new_x in range(0, self.board.max_width):
            if new_y in range(0, self.board.max_height):
                self.board.visited_points[new_x][new_y] += 25

    def move(self):
        radius = 2
        for i in range(self.x - radius, self.x + radius):
            for j in range(self.y - radius, self.y + radius):
                self._increment_for(i, j)

        if not self.generating_path:
            self.generating_path = True
            destination = random.choice(self.shops)
            t = threading.Thread(target=self._generate_path, args=(destination[0: 2],))
            t.start()
            self.threads.append(t)
        if not self.path:
            self.random_move()
        else:
            self.set_position(self.path.pop(0))
            if not self.path:
                timer = threading.Timer(random.randint(1, 5), self._mark_generating_path_as_done)
                timer.start()

    def _mark_generating_path_as_done(self):
        self.generating_path = False

    def set_position(self, a):
        self.x = a[0]
        self.y = a[1]

    def _generate_path(self, destination):
        # print("Generating Path for: " + str(self))
        self.path = self._astar((self.x, self.y), destination)
        # print("Created Path: " + str(self.path))
        return self.path

    def _heuristic(self, a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

    def _astar(self, destination, start):
        neighbors = [(0, self.step), (0, -self.step), (self.step, 0), (-self.step, 0)]
        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: self._heuristic(start, destination)}
        oheap = []

        heappush(oheap, (fscore[start], start))

        while oheap:
            current = heappop(oheap)[1]
            if current == destination:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self._heuristic(current, neighbor)
                if not self.board.is_destination_available(neighbor[0], neighbor[1]):
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self._heuristic(neighbor, destination)
                    heappush(oheap, (fscore[neighbor], neighbor))
        return False
