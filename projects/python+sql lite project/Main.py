
from tkinter import*
from admin_prg import Admin
from user_prg import User
   
class MainWindow:        
          def __init__(self,window):
              
              self.window = window
              self. window.title("BasketBall Team Management System")
              self.window.geometry("900x500")
              self.window.config(bg="black")
              #MAIN FRAME
              frame1=Frame(window,bg="yellow2")
              frame1.pack()
              titleM = Label(frame1,text ="MAIN MENU", font="Arial 20 bold",fg="white",bg="red2").grid(row =0 ,column = 0,columnspan=2,pady=20)
              self.b1=Button(frame1,text="Admin",font="Arial 15",fg="white",bg="red2",width =30,command=self.admin).grid(row =2 ,column = 0,columnspan=2,pady=50)
              self.b2=Button(frame1,text="User",font="Arial 15",fg="white",bg="red2",width =30,command=self.User).grid(row =4 ,column = 0,columnspan=2,pady=15)
          def admin(self):
              self.top = Toplevel( self.window) 
              self.app = Admin(self.top)
          def User(self):
              self.top1 = Toplevel(self.window) 
              self.app =User(self.top1)
          def Exit(self):
              self.window.destroy()

window = Tk()
MainWindow(window)   
