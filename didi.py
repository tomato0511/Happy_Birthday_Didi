from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.title("Happy Birthday 😎")
root.geometry("15200x620")

f1=Frame(root, bg="pink", borderwidth=10, relief=SUNKEN)
f1.pack(fill="x", side="top")

f5=Frame(f1, bg="yellow", borderwidth=10, relief=SUNKEN)
f5.pack(side="left", padx=20, pady=10)

level2=Label(f5, text='''🎉🎊🎈
🎁🎆''' , font=("arial",36) , fg="green", bg="indigo")
level2.pack()

f4=Frame(f1, bg="yellow", borderwidth=10, relief=SUNKEN)
f4.pack(side="right", padx=20, pady=10)

level1=Label(f4, text='''🎂 🍰 
🧁💖🌹''' , font=("arial",36)  , fg="gold",bg="hotpink")
level1.pack(side="top")

f3=Frame(f1, bg="yellow", borderwidth=10, relief=SUNKEN)
f3.pack(fill="y", padx=20, pady=10)

lavel=Label(f3, text="🌸 🌹 🌻 HAPPY BIRTHDAY 🌼 💐 🌹", font=("arial", 36, "bold"), fg="deeppink",bg="cyan")
lavel.pack(fill="y" , pady=10, padx=10)

f2=Frame(root, bg="yellow", borderwidth=10, relief=SUNKEN)
f2.pack(fill="both", padx=5, pady=5)

# my_pic=Image.open("cake_.png")

# resized=my_pic.resize((200,200), Image.Resampling.LANCZOS)

# new=ImageTk.PhotoImage(resized)

# f6=Frame(f2, borderwidth=10, relief=SUNKEN)
# f6.pack(side="left")





l2=Label(f2,text='''
আমার নিজের কোনো দিদি নেই ,
         but now I can say I have , 
       যে আমাকে Guide করে , 
       পড়া শোনাই help করে ,🎁  
      💖 ভুল করলে শাসন করে ,
       ভুল যাতে না করি-সেই জন্যে সাবধান করে ।💝
         ''', font=("arial",40,"bold"), fg="magenta", bg="lavender",justify="center")
l2.pack( fill="both",padx=10, pady=10, side="bottom")

# ch=Label(l2,image=new)
# ch.pack( side="left")

root.mainloop()