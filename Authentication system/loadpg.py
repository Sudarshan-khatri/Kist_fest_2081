from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import LoginPage
import sys


root=Tk()
root.title('Loading page')
root.geometry("600x400+300+200")
root.resizable(0, 0)

height=600
width=400
# x=(root.winfo_screenwidth()//2)-(width//2)
# y=(root.winfo_screenheight()//2)-(width//2)
# root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
root.wm_attributes('-topmost',True)

root.overrideredirect(1)
root.config(background='yellow')



#======================Load the image==============#
image_path= Image.open("D:/kist_fair_1/Authentication system/load.jpg")
photo = ImageTk.PhotoImage(image_path )
bg_label = Label(root, image=photo, bg='yellow')
bg_label.place(x=-10, y=-10)

#==============Exit_button======#######
exit_btn=Button(root,text='x',command=lambda:exit_button(),font=('arial',13,'bold'),fg='blue',bg='yellow',activebackground='yellow')
exit_btn.place(x=580,y=0)

#==================Welcoome label============#
welcome_label=Label(root,text='WELCOME TO MY APP',font=('arial',28,'bold'),bg='yellow')
welcome_label.place(x=50,y=10)

#==============progress bar========================#
progress_label=Label(root,text='Please Wait......',font=('arial',13,'bold'),bg='yellow')
progress_label.place(x=150,y=300)

progress=Progressbar(root,orient='horizontal',length=500,mode='determinate')
progress.place(x=50,y=350)


def exit_button():
    sys.exit(root.destroy())

def top():
    win=Toplevel()
    LoginPage.LoginForm(win)
    root.withdraw()
    win.deiconify()
     

i=0
def load():
    global i
    if i <= 100:
        txt = 'Please wait....... ' + str(i) + '%'
        progress_label.config(text=txt)
        progress['value'] = i
        i += 10
        progress_label.after(1000, load)
    else:
        top()
load()

root.mainloop()