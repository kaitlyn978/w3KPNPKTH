from tkinter import*
from PIL import ImageTk,Image
import random
root=Tk()
root.title("Endless Pokemon Game")
root.geometry("600x500")
img=ImageTk.PhotoImage(Image.open("pikachu.jpg", "squirtle.png", "charizard.jpg"))
pokemon=["pikachu","charizard","squirtle"]
power=[60,120,50]
label=Label(root)
label2=Label(root)
p1s=Label(root)
p2s=Label(root)
player1_score=0
def player1():
    global player1_score
    r1=random.randint(1,2)
    player1_score=player1_score+powerr
    random_pokemon=random[r1]
    powerr=power[r1]
    label["image"]=random_pokemon
    p1s["text"]="Player's 1 score is "+str(player1_score)
btn1=Button(root,image=img,command=player1)
btn1.place(relx=0.1,rely=0.6,anchor=CENTER)
player2_score=0
def player2():
    global player2_score
    r2=random.randint(1,2)
    player2_score=player2_score+powerr2
    random_pokemon2=random[r2]
    powerr2=power[r2]
    label["image"]=random_pokemon2
    p1s["text"]="Player's 2 score is "+str(player2_score)
btn2=Button(root,image=img,command=player2)
btn2.place(relx=0.9,rely=0.6,anchor=CENTER)
root.mainloop()
