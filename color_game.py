from tkinter import *
from random import shuffle
def scr():
   global score
   if timeLeft>0:
    e.focus_set()
    res=e.get()
    if res.lower() == color[1].lower():
      score = score + 1
      l6.config(text=score)
    e.delete(0, END)
    result()

def count():
   global timeLeft
   if timeLeft>0:
      timeLeft=timeLeft-1
      l4.config(text=timeLeft)
      l4.after(1000,count)
def result():
   shuffle(color)
   l2.config(text=color[0],fg=color[1])

def start(event):
   if timeLeft==60:
      count()
   scr()

color=["pink","red","yellow","black","brown","grey","green","orange","purple","blue"]
timeLeft=60
score=0
root=Tk()
root.geometry("700x400")
root.title("color game")
l1=Label(root,text="type the color of given word not the word",fg="black",bg="yellow",font="lucida 20 bold")
l1.pack()
l2=Label(root,font="lucida 50 bold")
l2.pack()
l3=Label(root,text="Timeleft:",fg="black",bg="yellow",font="lucida 35 bold")
l3.pack(side=LEFT)
l4=Label(root,text=timeLeft,font="lucida 35 bold")
l4.pack(side=LEFT)
l6=Label(root,text=score,font="lucida 35 bold")
l6.pack(side=RIGHT)
l5=Label(root,text="score:",fg="black",bg="yellow",font="lucida 35 bold")
l5.pack(side=RIGHT)
e=Entry(root)
e.place(x=300,y=175)
l7=Label(root,text="press enter to start game ",font="lucida 20 bold")
l7.place(x=200,y=350)
root.bind("<Return>",start)
e.focus_set()
root.mainloop()