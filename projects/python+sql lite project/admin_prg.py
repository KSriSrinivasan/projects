
from tkinter import*
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Combobox

conn=sqlite3.connect("sql1.db")
  
class Admin:
        
          def __init__(self,window):
              self.window = window
              self. window.title("Admin")
              self.window.geometry("1000x500")
              self.window.config(bg="black")
              #MAIN FRAME
              self.frame1=Frame(window,bg="yellow")
              self. frame1.pack()
              titleM = Label( self.frame1,text ="ADMIN MENU", font="Arial 25 bold",fg="white",bg="Red").grid(row =0 ,column = 0,columnspan=2,pady=20)
              self.b1=Button( self.frame1,text="Display All Players",font="Arial 15",fg="white",bg="Red",width =30,command=self.display).grid(row =2 ,column = 0,columnspan=2,pady=10)
              self.b2=Button (self.frame1,text="Delete Player",font="Arial 15",fg="white",bg="Red",width =30,command=self.delete).grid(row =4 ,column = 0,columnspan=2,pady=15)
              self.b3=Button (self.frame1,text="Update/Change Player",font="Arial 15",fg="white",bg="Red",width =30,command=self.updt).grid(row =6 ,column = 0,columnspan=2,pady=15)

          def display(self):
              self.top = Toplevel( self.window) 
              self.app = Disp(self.top)
          def delete(self):
              self.top1 = Toplevel(self.window) 
              self.app =Delete(self.top1)
          def updt(self):
              self.top2 = Toplevel(self.window) 
              self.app =Update(self.top2)
          def Exit(self):
              self.master.destroy()

class Disp:
     def __init__(self,window):
              self.window = window
              self. window.title("Display Team")
              self.window.geometry("900x500")
              self.window.config(bg="black")
              #MAIN FRAME
              self.frame1=Frame(window,bg="yellow")
              self.frame1.pack()
              self.lTitle = Label(self.frame1,text ="PLAYERS TABLE", font="Arial 20 bold",fg="white",bg="green").grid(row =0 ,column = 0,columnspan=2,pady=20)

              self.b1=Button(self.frame1,text="All Players",font="Arial 15",fg="white",bg="green",width =30,command=self.show).grid(row =2 ,column = 0,columnspan=2,pady=50)
     def show(self):
          conn = sqlite3.connect('sql1.db')
          r_set=conn.execute('SELECT * from Players ORDER BY teamNo');
          #self.lShow = Label(self.frame1,text ="TEAMNO NAME JERSEYNO POSITION AGE", font="Arial 10 bold",fg="white",bg="green").grid(row =4 ,column = 1,columnspan=12,pady=20)
          i=6 # row value inside the loop 
          for player in r_set: 
             for j in range(len(player)):
                e = Entry(self.frame1, width=20, fg="white",bg="green") 
                e.grid(row=i, column=j) 
                e.insert(END, player[j])
             i=i+1
class Delete:
     def __init__(self,window):
              self.window = window
              self. window.title("Delete")
              self.window.geometry("900x500")
              self.window.config(bg="black")
              #MAIN FRAME
              self.frame2=Frame(window,bg="yellow")
              self.frame2.pack()
              self.lShow = Label(self.frame2,text ="PLAYER DELETION", font="Arial 20 bold",fg="white",bg="green").grid(row =0 ,column = 0,columnspan=2,pady=20)

              self.deleteJno=IntVar()
              self.l1 = Label(self.frame2,text ="Enter Jersey Number: ", font="Arial 10 bold",fg="white",bg="green").grid(row =2 ,column = 0,columnspan=10,pady=20)
              self.l2 = Entry(self.frame2,font="Aerial 15 bold",bd=2,textvariable= self.deleteJno).grid(row=4,column=0,columnspan=10,pady=20)

              self.b1=Button(self.frame2,text="Delete",font="Arial 15",fg="white",bg="green",width =30,command=self.Del).grid(row =6,column = 0,columnspan=2,pady=50)
     def Del(self):
              conn = sqlite3.connect('sql1.db')
              p=list(conn.execute("SELECT * FROM Players WHERE jerseyNumber="+str(self.deleteJno.get())))
              if len(p) != 0:
                   p=list(conn.execute("DELETE FROM Players WHERE jerseyNumber="+str(self.deleteJno.get())))
                   messagebox.showinfo("Player Deletion", "Player Removed")
                   conn.commit()
              else:
                    messagebox.showinfo("Player Deletion", "Player Not In Database")
                    conn.commit()
              conn.commit()
              conn.close()
     def Exit(self):
              self.window.destroy()     
    
class Update:
    def __init__(self,window):
              self.window = window
              self. window.title("Update")
              self.window.geometry("900x500")
              self.window.config(bg="black")
            #MAIN FRAME
            #datafeilds

              self. name=StringVar()
              self. position=StringVar()
              self.age=IntVar()
              self.confirm=IntVar()
              self.deleteJno=IntVar()
              self.frame1=Frame(window,bg="yellow")
              self.frame1.pack()
              self.lTitle= Label(self.frame1,text ="UPDATE/CHANGE PLAYER FORM", font="Arial 20 bold",fg="white",bg="green").grid(row =0 ,column = 0,columnspan=2,pady=20)
                 
              self.lz1 = Label(self.frame1,text ="Enter Jersey Number: ", font="Arial 10 bold",fg="white",bg="green").grid(row=2,column=0,columnspan=10,pady=20)
              self.lz2 = Entry(self.frame1,font="Aerial 15 bold",bd=2,textvariable= self.deleteJno).grid(row=3,column=0)
              self.b1=Button(self.frame1,text="Update",font="Arial 15",fg="white",bg="green",width =30,command=self.input).grid(row =6 ,column = 0,columnspan=2,pady=50)
    def input(self):
              

              self.l2 = Label(self.frame1,text="Player Name",font="Aerial 15 bold",bg="yellow",bd=22).grid(row=8,column=0)
              self.l2 = Entry(self.frame1,text="Enter Player Name",font="Aerial 15 bold",bd=2,textvariable= self.name).grid(row=8,column=1)
  
              self.l4 = Label(self.frame1,text="Position",font="Aerial 15 bold",bg="yellow",bd=22).grid(row=10,column=0)
              self.combo=Combobox(self.frame1,width=15,background ='blue', foreground ="red",font = ("Times New Roman", 15),textvariable=self.position)
              self.combo['values']=("Point-Guard", "Shoot-Guard","Power-Forward","Small-Forward","Center")
              self.combo.grid(row=10,column=1)
              self.combo.current(0)

              self.l5 = Label(self.frame1,text="Age",font="Aerial 15 bold",bd=22,bg="yellow").grid(row=12,column=0)
              self.spin1 =Spinbox(self.frame1,from_=18,to=22,width=30,bd=2,textvariable= self.age).grid(row=12,column=1)
              self.bt2 = Button(self.frame1, text="Update/Change",width =20,font="Aerial 15 bold",bg="green",fg="white",command = self.update1).grid(row=14,column=0,columnspan=2,pady=50)

             # def click():
                  #  self.mb=messageBox.showinfo("yeahh","yeeab")
              #self.l6=Checkbutton(self.frame1,text="I have checked the above conditions and i agree",selectcolor="blue",variable=self.confirm,width=30,height=30,command=click).grid(row=12,column=0)
            
    def update1(self):
               conn = sqlite3.connect('sql1.db')
               self.insertion=( self.name.get(),self.position.get(),self.age.get(),self.deleteJno.get(),)
               p = list(conn.execute("Select * from Players where jerseyNumber=?", (self.deleteJno.get(),)))
               if len(p) != 0:
                    conn.execute('UPDATE Players SET name=?,position=?,age=? WHERE jerseyNumber=?',self.insertion)
                    messagebox.showinfo("Player Change", "Player Change Updated")
                    conn.commit()
               else:
                    messagebox.showinfo("Player Change", "Player Not In Database")
                    
               conn.close()
    def Exit(self):
               self.window.destroy()

