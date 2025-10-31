from tkinter import *
import logic

def play(move = 0):
    if logic.player:
        x = logic.play(move)
    else:
        x = logic.play(logic.random_valid_move())
    board.config(text= logic.display_board())
    if x:
        print(logic.evalWinner())
        rate.config(text= "Win Rate: " + logic.calc_rate())
        b1.pack_forget()
        b2.pack_forget()
        b3.pack_forget()
        b.pack_forget()
        #board.config(text= logic.display_board())
        return
    #enemy move
    if logic.ai: #########
        print('this shouldnt be activating')
        return
    else:
        logic.play(logic.random_valid_move())
    
    board.config(text= logic.display_board())
    if x:
        print(logic.evalWinner())
        rate.config(text= "Enemy Win Rate: " + logic.calc_rate())
        b1.pack_forget()
        b2.pack_forget()
        b3.pack_forget()
        b.pack_forget()
        #board.config(text= logic.display_board())

def AIFunc():
    pass
#     if logic.ai:
#         toggleAI.config(text='Play an AI')
#     else:
#         toggleAI.config(text='Play against Random')
#     logic.newGame(True)

def playerFunc():
    if logic.player:
        togglePlayer.config(text='Play as You')
        b1.pack_forget()
        b2.pack_forget()
        b3.pack_forget()
        b.pack(side='left', padx=3, pady=3)
    else:
        togglePlayer.config(text='Play Randomly')
        b.pack_forget()
        b1.pack(side='left', padx=3, pady=3)
        b2.pack(side='left', padx=3, pady=3)
        b3.pack(side='left', padx=3, pady=3)
    logic.newGame(False)
        
################### TKinter UI

window = Tk()
window.geometry('700x500')
#window.resizable(False, False)
window.title('Mancala')
window.config(bg='#FFFFFF')

header = Label(window, text='Mancala', font=('Times New Roman', 40), bg='#FFFFFF')
header.pack(side='top', anchor='center', pady=10)

rate = Label(window, text='AI Win Rate: 100%', font=('Times New Roman', 20), bg='#FFFFFF')
rate.pack(side='top', anchor='center', pady=10)

frame1 = Frame(window, bg='#FFFFFF')
frame1.pack(side='top')

togglePlayer = Button(frame1, text="Play Randomly", font=('Times New Roman', 17), width=12, command= playerFunc)
togglePlayer.pack(side='left')

toggleAI = Button(frame1, text="Play an AI", font=('Times New Roman', 17), width=10, command= AIFunc)
toggleAI.pack(side='left')

resetAI = Button(frame1, text="Reset AI", font=('Times New Roman', 17), width=10, command= logic.resetAI())
resetAI.pack(side='left')

frame = Frame(window, bg='#FFFFFF')
frame.pack(side='bottom', anchor='center', pady = 50)

#board = Label(window, text = logic.display_board(), width=500, height=300, bg='#593004')
board = Label(frame, text = logic.display_board(), font=('Times New Roman', 20), bg='#FFFFFF')
board.pack(side='top', pady = 10)

buttons = Frame(frame, bg='#FFFFFF')
buttons.pack(side='top')

b1 = Button(buttons, text="Pit 1", font=('Times New Roman', 17), command= lambda: play(0), padx=10, pady=5, bg='#FFFFFF')
b1.pack(side='left', padx=3, pady=3)
b2 = Button(buttons, text="Pit 2", font=('Times New Roman', 17), command= lambda: play(1), padx=10, pady=5, bg='#ffffff')
b2.pack(side='left', padx=3, pady=3)
b3 = Button(buttons, text="Pit 3", font=('Times New Roman', 17), command= lambda: play(2), padx=10, pady=5, bg='#ffffff')
b3.pack(side='left', padx=3, pady=3)

b = Button(buttons, text="Make Random Move", font=('Times New Roman', 17), command=play, padx=10, pady=5, bg='#FFFFFF')
#b.pack(side='left', padx=3, pady=3)

window.mainloop()



































"""
import logic as l

def updatePits():
    pass

def play(move = 0):
    if logic.player:
        logic.play(move)
    else:
        logic.play(logic.random_valid_move())
    logic.display_board()
    #enemy move
    if logic.ai:
        print('why?')
        return
    else:
        logic.play(logic.random_valid_move())
    logic.display_board()

def newGame(ai = logic.ai, player = logic.player):
    if player !=  logic.player and not player:
        b1 = Label(board, text=l.stones, padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#999999')
    logic.newGame(ai, player)
    updatePits()
    

window = Tk()
window.geometry('1000x600')
#window.resizable(False, False)
window.title('Mancala')
window.config(bg='#FFFFFF')

header = Label(window, text='Mancala', font=('Times New Roman', 40), bg='#FFFFFF')
header.pack(side='top', anchor='center', pady=10)

board = Frame(window, width=500, height=300, bg='#593004')
board.pack(side='bottom', anchor='center',pady=200)
board.grid_rowconfigure(1, minsize=20)

m1 = Label(board, text=l.stones, padx=15, highlightthickness=0,bg='#ffffff')
m1.grid(row=0, column=0, rowspan=3, padx=5, pady=5, sticky='ns')
l1 = Label(board, text=l.stones, padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#ffffff')
l1.grid(row=0, column=1, padx=3, pady=3)
l2 = Label(board, text=l.stones, padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#ffffff')
l2.grid(row=0, column=2, padx=3, pady=3)
l3 = Label(board, text=l.stones, padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#ffffff')
l3.grid(row=0, column=3, padx=3, pady=3)

b1 = Button(board, text=l.stones, command= lambda: print(1), padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#ffffff')
b1.grid(row=2, column=1, padx=3, pady=3)
b2 = Button(board, text=l.stones, command= lambda: print(2), padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#ffffff')
b2.grid(row=2, column=2, padx=3, pady=3)
b3 = Button(board, text=l.stones, command= lambda: print(3), padx=10, pady=5, borderwidth=0, highlightthickness=0,bg='#ffffff')
b3.grid(row=2, column=3, padx=3, pady=3)
m2 = Label(board, text=l.stones, padx=15, highlightthickness=0,bg='#ffffff')
m2.grid(row=0, column=4, rowspan=3, padx=5, pady=5, sticky='ns')

#canvas = Canvas(window, width=1000, height=300, borderwidth=0, highlightthickness=0,bg='blue')
#canvas = Canvas(window, width=1000, height=300, borderwidth=0, highlightthickness=0)
#canvas.pack(side='bottom', anchor='center',pady=100)

restart = Button(window, text='Restart Game', command= lambda: newGame())
restart.pack(side='bottom', anchor='center',pady=0)

window.mainloop()
"""