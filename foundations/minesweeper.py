import random

class MineField():
    def __init__(self):
        self.sz = int(input())
        self.n_mines = int(input())
        if self.n_mines > self.sz**2:
            raise ValueError("too much mines given field size")
        self.mat = self._construct_matrix()
        self._populate()

    def _construct_matrix(self):
        mat = []
        for row in range(self.sz):
            mat.append([0 for col in range(self.sz)])
        print(mat)
        return mat

    def _populate(self):
        pass


if __name__ == "__main__":
    mf = MineField()