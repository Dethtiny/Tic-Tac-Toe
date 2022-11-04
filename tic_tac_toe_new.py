from tkinter import *
from tkinter import messagebox
board = [i+1 for i in range(9)]
player = 'X'
status='none'
step=0
game='yes'
x_score=0
o_score=0

def move (x):
    global board, step,player
    if board[x-1]!='X' and board[x-1]!='O':
        board[x-1]=player
        button[x-1].configure(text=player)
        if player=='X':
            player='O'
            lbl.config(text=f'Ход игрока {player}')
        else:
            player='X'
            lbl.config(text=f'Ход игрока {player}')
        step+=1
    else:
        messagebox.showinfo('Ошибка', 'Поле занято')
    status_check()

def status_check():
    global board,status
    for i in range (0,9,3):
        if board[i]==board[i+1]==board[i+2] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
            status='win'
    for i in range (3):
        if board[i]==board[i+3]==board[i+6]:
            status='win'
    if step>=9 and status=='none':
            status='lose'
    endgame()

def endgame():
    global status, player, o_score, x_score, board,step
    if status =='win':
        if player=='X':
            player='O'
            o_score+=1
        else:
            player='X'
            x_score+=1
        messagebox.showinfo('Победа', f'!!!ИГРОК {player} ПОБЕДИЛ!!!\nСУММА ОЧКОВ:\nИГРОК X: {x_score}\nИГРОК O: {o_score}')
        for i in button:
            i.configure(text='')
            board = [i + 1 for i in range(9)]
            status='none'
            step=0
    elif status=='lose':
        messagebox.showinfo('Ничья',f'!!!НИЧЬЯ!!\nСУММА ОЧКОВ:\nИГРОК X: {x_score}\nИГРОК O: {o_score}')
        for i in button:
            i.configure(text='')
            board = [i + 1 for i in range(9)]
            status = 'none'
            step = 0

window = Tk()
window.title("Игровое поле")
window.geometry('240x290')
lbl = Label(window, text="Ход игрока X", font=("Arial Bold", 14))
lbl.grid(column=1, row=5,columnspan=3)
button=[Button(window, text="",height=5,width=10,command=lambda x=i: move(x)) for i in range (1,10)]

i=0
for col in range (1,4):
    for row in range (1,4):
        button[i].grid(row=row,column=col)
        i+=1

window.mainloop()