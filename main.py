import numpy as np
import tkinter as tk
from Shu import Shu
from fundamental import fundamental

sd = fundamental()
Shudu = sd.shudu

root = tk.Tk()
root.geometry('820x900+100+100')  # 大小和位置
root.title('Sudoku')

btnlst = []
evs = []
answer_old = np.zeros(81, dtype=np.int)
answer_new = answer_old
answer_old = np.reshape(Shudu, 81)
blank = np.arange(81)
np.random.shuffle(blank)
for i in range(81):
    evs.append(tk.IntVar(root, Shudu[i // 9][i % 9]))
for i in range(30):
    evs[blank[i]].set('')
    answer_old[blank[i]] = 0

i = 0
for r in range(9):
    for c in range(9):
        if r > 2 and r < 6 and c > 2 and c < 6:
            btnlst.append(tk.Entry(root, textvariable=evs[i], justify='center', font=('Helvetica', '20')))
        elif r > 2 and r < 6:
            btnlst.append(tk.Entry(root, textvariable=evs[i], justify='center', font=('Helvetica', '20')))
            btnlst[i]['background'] = '#708090'
        elif c > 2 and c < 6:
            btnlst.append(tk.Entry(root, textvariable=evs[i], justify='center', font=('Helvetica', '20')))
            btnlst[i]['background'] = '#708090'
        else:
            btnlst.append(tk.Entry(root, textvariable=evs[i], justify='center', font=('Helvetica', '20')))
        btnlst[i].place(x=5 + c * 90, y=0 + r * 90, width=90, height=90)
        i += 1

y = 0

num = list()
num.append(tk.IntVar(root, 51))
kuang = list()
kuang.append(tk.Entry(root, textvariable=num[0], justify='center', font=('Helvetica', '20')))
kuang[0].place(x=5, y=810, width=180, height=90)
old_num = 51
new_num = 0


def onclick(event):
    global answer_new, answer_old, y, old_num, new_num
    i = y // 9
    j = y % 9
    if (i // 3 * 3 + j // 3) % 2:
        btnlst[y]['background'] = '#708090'
    else:
        btnlst[y]['background'] = '#FFFFFF'

    try:
        new_num = num[0].get()
    except:
        pass
    if new_num-old_num:
        te = fundamental()
        arr = te.shudu
        answer_old = np.reshape(arr, 81)
        blank = np.arange(81)
        np.random.shuffle(blank)
        for i in range(81):
            if i < new_num:
                tem = arr.reshape(81)
                evs[blank[i]].set(tem[blank[i]])
            else:
                evs[blank[i]].set('')
                answer_old[blank[i]] = 0
        old_num = new_num
        return

    for i in range(81):
        try:
            answer_new[i] = evs[i].get()
        except:
            answer_new[i] = 0
    arr = abs(answer_new - answer_old)
    if not sum(arr):
        btnlst[y]['background'] = '#DC143C'
        return
    a = list(arr)
    x = a.index(max(a))
    tt = answer_new.copy()
    temp = Shu(tt)
    if not temp.flag:
        btnlst[x]['background'] = '#DC143C'
    answer_old = answer_new.copy()
    y = x


root.bind('<Return>', onclick)
ranInitBtn = tk.Button(root, text='', command=onclick)  # new one sudo
ranInitBtn.place(x=5, y=710, width=0, height=0)
root.mainloop()