import numpy as np


class Shu:
    mark_hang = np.zeros((9, 9), dtype=np.int)
    mark_lie = np.zeros_like(mark_hang, dtype=np.int)
    mark_kuai = np.zeros_like(mark_hang, dtype=np.int)
    shudu = np.zeros((9, 9), dtype=np.int)
    flag = 0

    def __init__(self, shudo):
        shudo = np.reshape(shudo, (9, 9))
        self.mark_hang = np.zeros((9, 9), dtype=np.int)
        self.mark_lie = np.zeros_like(self.mark_hang, dtype=np.int)
        self.mark_kuai = np.zeros_like(self.mark_hang, dtype=np.int)
        self.shudu = shudo
        self.check()

    def mark(self):
        for i in range(9):
            for j in range(9):
                te = self.shudu[i][j] - 1
                if te >= 0:
                    if self.mark_hang[i][te] or self.mark_lie[j][te] or self.mark_kuai[i // 3 * 3 + j // 3][te]:
                        return False
                    else:
                        self.mark_hang[i][te] = 1
                        self.mark_lie[j][te] = 1
                        self.mark_kuai[i // 3 * 3 + j // 3][te] = 1
        return True

    def dfs(self, x, y, num):
        if num == 81:
            self.flag = 1
            return 1
        elif self.shudu[x][y]:
            if y == 8:
                m = self.dfs(x + 1, 0, num + 1)
            else:
                m = self.dfs(x, y + 1, num + 1)
            if m:
                return 1
        else:
            temp = np.zeros(9)
            for i in range(9):
                if self.mark_hang[x][i]:
                    temp[i] = 1
            for i in range(9):
                if self.mark_lie[y][i]:
                    temp[i] = 1
            for i in range(9):
                if self.mark_kuai[x // 3 * 3 + y // 3][i]:
                    temp[i] = 1
            for i in range(9):
                if not temp[i]:
                    self.mark_hang[x][i] = 1
                    self.mark_lie[y][i] = 1
                    self.mark_kuai[x // 3 * 3 + y // 3][i] = 1
                    self.shudu[x][y] = i + 1
                    if y == 8:
                        m = self.dfs(x + 1, 0, num + 1)
                    else:
                        m = self.dfs(x, y + 1, num + 1)
                    if m:
                        return 1
                    self.mark_hang[x][i] = 0
                    self.mark_lie[y][i] = 0
                    self.mark_kuai[x // 3 * 3 + y // 3][i] = 0
                    self.shudu[x][y] = 0

    def check(self):
        re = self.mark()
        if re:
            self.dfs(0, 0, 0)