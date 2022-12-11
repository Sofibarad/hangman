from tkinter import *
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200
MARGIN = 100
BG_COLOR = "azure"
BG_COLOR2 ="green"
LINES_COLOR = "aquamarine3"
BTN_COLOR = "white"
BTN_COLOR2 = "green"
TXT_COLOR = "black"
TXT_TRIES = "red"
TXT_TRIES2 = "red"
SPEC_COLOR = "red"
HEAD_COLOR = "#FFFFB6"
BODY_COLOR = "green"
HAND_COLOR = "#0000B2"
HAND_COLOR2 = "VioletRed1"
FOOT_COLOR1 = "#7C7CFC"
FOOT_COLOR2 = "orange"
FG_COLOR ="black"
label_word = []
btn_alpha = []


#creating an alphabet buttons:
def start_pos_alphabet()-> None:
    shift_x =0
    shift_y = 0
    count = 0

    for letter in range(ord("A"), ord("Z")+1):
        btn = Button(text=chr(letter), bg=BTN_COLOR, foreground=TXT_COLOR, activebackground ="aquamarine3", font = "Arial 15", relief =SOLID )
        btn.place(x=WINDOW_HEIGHT-MARGIN*8 + shift_x, y=MARGIN*6 - shift_y)
        btn.bind("<Button-1>", lambda event: check_alpha(event, word))
        btn_alpha.append(btn)
        shift_x += 50
        count +=1

        if(count==9):
            shift_x = count = 0
            shift_y-=50

            
#guess word from the dictionary word.txt           
def start_word() -> str:
    readfile = open("words.txt")
    count = 0

    for lines in readfile:
        count +=1
    
    num_word=random.randint(1, count) # [1; count] choose a random word
    word = ""
    count = 0

    readfile=open("words.txt")

    for lines in readfile:
        count+=1

        if(count == num_word):
            word = lines[:len(lines) -1:]

    word = word.upper()
    print(word)
    return word

#creating a line of guess word
def start_pos_word(word: list) -> None:
    shift = 0

    for dashes in range(len(word)):
        label_under = Label(window, text = "__", font = "Arial 15", bg = BG_COLOR, fg=FG_COLOR)
        label_under.place(x=WINDOW_HEIGHT-MARGIN*8 + shift, y=MARGIN*5)
        shift +=50
        label_word.append(label_under)

#draw hangman       
def draw(lifes: int)->None:
    if(lifes == 9):
        line_1=canvas.create_line(MARGIN, WINDOW_HEIGHT - MARGIN, MARGIN, MARGIN, width=4, fill=LINES_COLOR)
    elif(lifes == 8):
        line_2=canvas.create_line(MARGIN, MARGIN, WINDOW_WIDTH//3, MARGIN, width=4, fill=LINES_COLOR)
    elif(lifes == 7):
        line_3=canvas.create_line(WINDOW_WIDTH//3, MARGIN, WINDOW_WIDTH//3,MARGIN*2, width=4, fill=LINES_COLOR)
    elif(lifes == 6):
        line_4=canvas.create_line(MARGIN+100,MARGIN, MARGIN, MARGIN//3+150, width=4, fill=LINES_COLOR)
    elif(lifes == 5):
        head = canvas.create_oval(WINDOW_WIDTH // 3 - 30, MARGIN * 1.5, WINDOW_WIDTH //3 + 30, MARGIN * 2, fill=HEAD_COLOR)
    elif(lifes == 4):
        body = canvas.create_oval(WINDOW_WIDTH // 3 - 20, MARGIN * 2, WINDOW_WIDTH //3 + 20 , MARGIN * 3, fill=BODY_COLOR)
    elif(lifes == 3):
        l_hand = canvas.create_line(WINDOW_WIDTH// 3 - 10, MARGIN * 2.1, WINDOW_WIDTH // 3 - 70, MARGIN *2.4, width=6, fill=HAND_COLOR)
    elif(lifes == 2):
        r_hand = canvas.create_line(WINDOW_WIDTH// 3 + 10, MARGIN * 2.1, WINDOW_WIDTH // 3 + 70, MARGIN *2.4, width=6, fill=HAND_COLOR2)
    elif(lifes == 1):
        l_foot = canvas.create_line(WINDOW_WIDTH// 3 - 15, MARGIN * 2.8, WINDOW_WIDTH // 3 - 70, MARGIN *3.4, width=7, fill=FOOT_COLOR1)
    elif(lifes == 0):
        r_foot = canvas.create_line(WINDOW_WIDTH// 3 + 15, MARGIN * 2.8, WINDOW_WIDTH // 3 + 70, MARGIN *3.4, width=7, fill=FOOT_COLOR2)
        game_over("lose")

#check letter in our word
def check_alpha(event: str, word: list)->None:
    alpha = event.widget['text']
    pos =[]

    for position in range(len(word)):
        if (word[position] == alpha):
            pos.append(position)
            btn = (BG_COLOR2)

    if(pos):
        for position in pos:
            label_word[position].config(text = "{}".format(word[position]))

        count_alpha = 0

        for position in label_word:
            if(position["text"].isalpha()):
                count_alpha +=1
        
        if(count_alpha == len(word)):
            game_over("win")
    else:
        lifes = int(label_life.cget("text"))-1

        if(lifes >= 0):
            label_life.config(text = " {}" .format(lifes))

        draw(lifes)

def game_over(status: str)->None:
    for btn in btn_alpha:
        btn.destroy()


    if(status == "win"):
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 50 , font = "Arial 30", text="YOU WIN!!!", fill = SPEC_COLOR)

    else:
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 20, font = "Arial 30", text="SORRY, TRY ONE MORE TIME:)", fill = SPEC_COLOR)


window = Tk()
window.title("Hangman")

window.resizable(False, False)

#
lifes = 10

label_text = Label(window, text = "TRIES: ", font ="Arial 25", foreground = TXT_TRIES)
label_text.place(x=930,y=10)
label_life = Label(window, text=" {}".format(lifes), font="Arial 25", foreground=TXT_TRIES2)
label_life.place(x=1110, y=10)

canvas = Canvas(window, bg=BG_COLOR, height = WINDOW_HEIGHT, width=WINDOW_HEIGHT)
canvas.place(x=0, y=70)
window.geometry("1200x800")

start_pos_alphabet()
word = start_word()
start_pos_word(word)
print(word)
window.mainloop()