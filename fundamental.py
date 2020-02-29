import numpy as np


class fundamental:
    mark_hang = np.zeros((9, 9), dtype=np.int)
    mark_lie = np.zeros_like(mark_hang, dtype=np.int)
    mark_kuai = np.zeros_like(mark_hang, dtype=np.int)
    shudu = np.zeros((9, 9), dtype=np.int)

    def __init__(self):
        self.mark_hang = np.zeros((9, 9), dtype=np.int)
        self.mark_lie = np.zeros_like(self.mark_hang, dtype=np.int)
        self.mark_kuai = np.zeros_like(self.mark_hang, dtype=np.int)
        self.shudu = np.zeros((9, 9), dtype=np.int)
        self.dfs(0, 0, 0)

    def dfs(self, x, y, num):
        if num == 81:
            # print(self.shudu)
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
            tt = np.arange(9)
            np.random.shuffle(tt)
            for i in tt:
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