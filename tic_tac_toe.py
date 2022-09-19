board = [i+1 for i in range(9)]
player = 'X'
status='none'
step=0
game='yes'
x_score=0
o_score=0
def move (x):
    global board, step,player
    if x.lower()=='restart':
        board =[i+1 for i in range(9)]
        step = 0
        player = "X"
    elif x in ['1','2','3','4','5','6','7','8','9']:
        x=int(x)
        if 1<=x<=9 and board[x-1]!='X' and board[x-1]!='O':
            board[x-1]=player
            if player=='X':
                player='O'
            else:
                player='X'
            step+=1
        else:
            print('Поле занято')
    else:
        print('Ошибка ввода')
def status_check():
    global status
    for i in range (0,9,3):
        if board[i]==board[i+1]==board[i+2] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
            status='win'
    for i in range (3):
        if board[i]==board[i+3]==board[i+6]:
            status='win'
    if step>=9 and status=='none':
            status='lose'
def endgame():
    global player,o_score,x_score
    for i in range (0,9,3):
        print(board[i],board[i+1],board[i+2])
    if status=='lose':
        print('!!!НИЧЬЯ!!!','СУММА ОЧКОВ',f'ИГРОК X: {x_score}',f'ИГРОК O: {o_score}',sep='\n')
    if status =='win':
        if player=='X':
            player='O'
            o_score+=1
        else:
            player='X'
            x_score+=1
        print('!!!ИГРОК '+player+' ПОБЕДИЛ!!!','СУММА ОЧКОВ',f'ИГРОК X: {x_score}',f'ИГРОК O: {o_score}',sep='\n')
def replay():
    global game,status,board,player,step
    if player=='X':
        player='O'
    else:
        player='X'
    while game not in ['yes','no']:
        game=input('Введите "yes" или "no"')
def main():
    global game,status,board,player,step
    while game=='yes':
        status='none'
        board = [i+1 for i in range(9)]
        step=0
        while status=='none':
            for i in range (0,9,3):
                print(board[i],board[i+1],board[i+2])
            x=input('Куда поставить '+player+'?')
            move(x)
            if step>4:
                status_check()
        endgame()
        game = input('Вы хотите продолжить?').lower()
        replay()
main()
print('!!!ИГРА ЗАВЕРЕШНА!!!')
