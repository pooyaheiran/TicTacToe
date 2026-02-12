import tkinter as tk
import tkinter.font as tkFont

board = [[None] * 3 for _ in range(3)]
turn = 0


def button_disable():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)


def reset_game():
    global board
    global turn
    global is_win
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)
    label.config(text="")
    turn = 0
    is_win = False
    board = [[None] * 3 for _ in range(3)]


is_win = False


def check_win(i, j):
    global turn
    global is_win
    turn += 1
    if turn % 2 == 1:
        buttons[i][j].config(text="X", state=tk.DISABLED, disabledforeground="#FF0E46")
        board[i][j] = "X"
    else:
        buttons[i][j].config(text="O", state=tk.DISABLED, disabledforeground="#00CCFF")
        board[i][j] = "O"

    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            label.config(text=f"{board[i][0]}\nWINNER")
            is_win = True
            button_disable()

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            label.config(text=f"{board[0][i]}\nWINNER")
            is_win = True
            button_disable()

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        label.config(text=f"{board[0][0]}\nWINNER")
        is_win = True
        button_disable()

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        label.config(text=f"{board[0][2]}\nWINNER")
        is_win = True
        button_disable()

    if turn == 9 and is_win is False:
        label.config(text="DRAW")


is_dark = 0


def change_theme():
    global is_dark
    if is_dark == 0:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg="#292929")
                reset_button.config(bg="#FF0077")
                theme_button.config(bg="#1399FF")
                theme_button.config(text="Lightmode")

        is_dark = 1

    else:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg="#F0F0EB")
                reset_button.config(bg="#FF3C97")
                theme_button.config(bg="#43ADFF")
                theme_button.config(text="Darkmode")
        is_dark = 0


root = tk.Tk()
root.resizable(False, False)
custom_font = tkFont.Font(family="", size=16)

buttons = [[None] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        button = tk.Button(
            root,
            text="",
            width=10,
            height=4,
            font=(custom_font),
            command=lambda i=i, j=j: check_win(i, j),
            bg="#ECECEC",
        )
        button.grid(row=i, column=j)
        buttons[i][j] = button

reset_button = tk.Button(
    root,
    text="reset",
    font=custom_font,
    command=reset_game,
    width=10,
    height=2,
    fg="#242121",
    bg="#43ADFF",
)
theme_button = tk.Button(
    root,
    text="Darkmode",
    font=custom_font,
    command=change_theme,
    width=10,
    height=2,
    fg="#242121",
    bg="#FF3C97",
)
theme_button.grid(row=3, column=2)

reset_button.grid(row=3, column=0)

label = tk.Label(
    root,
    text="",
    font=custom_font,
    fg="#242121",
    width=10,
    height=2,
)
label.grid(row=3, column=1)

root.mainloop()
