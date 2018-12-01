class PedestrianRepository:
    class __PedestrianRepository:
        def __init__(self, arg):
            self.val = arg
            self.pedestrians = arg[0]
            self.repo_name = arg[1]

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not PedestrianRepository.instance:
            PedestrianRepository.instance = PedestrianRepository.__PedestrianRepository(arg)
        else:
            PedestrianRepository.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __repr__(self):
        return str(self.repo_name) + str(self.pedestrians)

    def move_all(self):
        # should be runned on multiple threads depending on system capacity
        for pedestrian in self.pedestrians:
            pedestrian.move()
