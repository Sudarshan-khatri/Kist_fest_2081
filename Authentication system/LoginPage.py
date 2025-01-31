from tkinter import *
from PIL import ImageTk, Image  # pip install pillow 
import mysql.connector
import bcrypt


class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x710")
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # =================Background image==================#
        self.bg_frame = Image.open("D:/kist_fair_1/Authentication system/backgd.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # =========Login Form==========#
        self.lgn_frame = Frame(self.window, bg='#FFFF00', width=956, height=660)
        self.lgn_frame.place(x=200, y=70)
        self.txt = 'Welcome'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Arial', 25, 'bold'),bg='yellow', fg='#000080')
        self.heading.place(x=30, y=30, width=200, height=100)

        # ====Left side Image======#
        self.side_img = Image.open("D:/kist_fair_1/Authentication system/key.png")
        photo = ImageTk.PhotoImage(self.side_img)
        self.side_img_label = Label(self.lgn_frame, image=photo, bg='#FFFF00')
        self.side_img_label.image = photo  # Retain reference to avoid garbage collection
        self.side_img_label.place(x=2, y=100)

        

    #=====sign up form=======#
        self.sign_up_img = Image.open("D:/kist_fair_1/Authentication system/add-friend.png")
        photo = ImageTk.PhotoImage(self.sign_up_img )
        self.sign_up_img_label = Label(self.lgn_frame, image=photo, bg='#FFFF00')
        self.sign_up_img_label.image = photo  # Retain reference to avoid garbage collection
        self.sign_up_img_label.place(x=550, y=110)
        self.sign_in_label=Label(self.lgn_frame,text='Sign In',bg='yellow',fg='#000080',font=('Arial',13,'bold'))
        self.sign_in_label.place(x=650,y=380)


    #========user_Name ================#
        self.UserName_label=Label(self.lgn_frame,text='Username',bg='yellow',fg='#000080',font=('Arial',13,'bold'))
        self.UserName_label.place(x=550,y=410)

        self.UserName_entry=Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='yellow',fg='#000080')
        self.UserName_entry.place(x=570,y=430,width=200)

        self.UserName_line=Canvas(self.lgn_frame,width=300, height=2.0,bg='#2E7D32',highlightthickness=0)
        self.UserName_line.place(x=550,y=450)


    #========username icon===============#

        self.user_icon= Image.open("D:/kist_fair_1/Authentication system/user.png")
        photo = ImageTk.PhotoImage(self.user_icon)
        self.user_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFF00')
        self.user_icon_label.image= photo  # Retain reference to avoid garbage collection
        self.user_icon_label.place(x=550,y=430)

    #===========password =================#
    
        self.password_label=Label(self.lgn_frame,text='Password',bg='yellow',fg='#000080',font=('Arial',13,'bold'))
        self.password_label.place(x=550,y=480)

        self.password_entry=Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='yellow',fg='#000080')
        self.password_entry.place(x=570,y=505,width=200)

        self.password_line=Canvas(self.lgn_frame,width=300, height=2.0,bg='#2E7D32',highlightthickness=0)
        self.password_line.place(x=550,y=520)

    #========password icon===============#

        self.password_icon= Image.open("D:/kist_fair_1/Authentication system/user.png")
        photo = ImageTk.PhotoImage(self.user_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFF00')
        self.password_icon_label.image= photo  # Retain reference to avoid garbage collection
        self.password_icon_label.place(x=550,y=500)

        
    #=========Login Button================#
        self.login=Button(self.lgn_frame, text='Login',font=('Arial',13,'bold'),width=25,bd=1,cursor='hand2',bg='#3047ff',activebackground='#3047ff',fg='white')
        self.login.place(x=610,y=535,width=150)
    #=========Forget password=========#
        self.forget_button=Button(self.lgn_frame,text='Forget password ?',font=('Arial',11,'bold'),width=50,bd=1,bg='#3047ff',fg='white')
        self.forget_button.place(x=750,y=580,width=200)

    #============sign up=====================#
        self.sign_label=Button(self.lgn_frame,text='Sign_up',font=('Arial',11,'bold'),width=50,bd=1,bg='#3047ff',fg='white')   
        self.sign_label.place(x=500,y=580,width=200)

    #============show/hide password=============#    
        self.show_img= Image.open("D:/kist_fair_1/Authentication system/show.png")
        photo = ImageTk.PhotoImage(self.show_img)
        self.show_img= Button(self.lgn_frame, image=photo, bg='white',activebackground='white',cursor='hand2',bd=0,command=self.show)
        self.show_img.image= photo
        self.show_img.place(x=830,y=500)


        self.hide_img= Image.open("D:/kist_fair_1/Authentication system/show.png")
        self.photo = ImageTk.PhotoImage(self.hide_img)
        

    def show(self):
        self.hide_img= Button(self.lgn_frame, image=self.photo, bg='white',activebackground='white',cursor='hand2',bd=0)
        self.hide_img.image=self.photo
        self.hide_img.place(x=830,y=500)
        self.password_entry.config(show='*')




def page():
    window = Tk()
    window.title("TwinPlay Adventures")
    LoginForm(window)
    window.mainloop()


if __name__ == "__main__":
    page()
