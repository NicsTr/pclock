import random
from pclock import PClock


class TriangularPClock(PClock):
    def __init__(self, lower_limit, upper_limit):
        super(TriangularPClock, self).__init__()
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    @property
    def distrib_name(self):
        return "triangular"

    def shift_gen(self):
        return random.triangular(self.lower_limit, self.upper_limit)

