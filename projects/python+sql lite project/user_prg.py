
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3
conn=sqlite3.connect("sql1.db")
'''
conn.execute('CREATE TABLE Players(teamNo INTEGER,name TEXT NOT NULL, jerseyNumber INTEGER NOT NULL UNIQUE, position TEXT NOT NULL, age INTEGER NOT NULL)')
'''
print("DATABASE CONNECTION SUCCESSFUL")
class User:
        
          def __init__(self,window):
              self.window = window
              self. window.title("User")
              self.window.geometry("900x500")
              self.window.config(bg="black")
            #MAIN FRAME
              self.frame1=Frame(window,bg="green")
              self.frame1.pack()
            #datafeilds
              self. teamNo=IntVar()
              self. name=StringVar()
              self. jn=IntVar()
              self. position=StringVar()
              self.age=IntVar()
              self.confirm=IntVar()
            #TITLE
              self.userTitle = Label(self.frame1,text = "PLAYER REGISTRATION FORM", font="Aerial 20 bold",bg="green")
              self.userTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
            #labels
              self.l1 = Label(self.frame1,text="Team Number",font="Aerial 15 bold",bg="green",bd=22).grid(row=2,column=0)
              self.spin =Spinbox(self.frame1,from_=1,to=12,width=30,bd=2,textvariable= self.teamNo).grid(row=2,column=1)

              self.l2 = Label(self.frame1,text="Player Name",font="Aerial 15 bold",bg="green",bd=22).grid(row=4,column=0)
              self.l2 = Entry(self.frame1,text="Enter Player Name",font="Aerial 15 bold",bd=2,textvariable= self.name).grid(row=4,column=1)

              self.l3 = Label(self.frame1,text="Jersey Number",font="Aerial 15 bold",bg="green",bd=22).grid(row=6,column=0)
              self.l3 = Entry(self.frame1,text="Enter Player JN",font="Aerial 15 bold",bd=2,textvariable= self.jn).grid(row=6,column=1)

              
              self.l4 = Label(self.frame1,text="Position",font="Aerial 15 bold",bg="green",bd=22).grid(row=8,column=0)
              self.combo=Combobox(self.frame1,width=15,background ='blue', foreground ="red",font = ("Times New Roman", 15),textvariable=self.position)
              self.combo['values']=("Point-Guard", "Shoot-Guard","Power-Forward","Small-Forward","Center")
              self.combo.grid(row=8,column=1)
              self.combo.current(0)

              self.l5 = Label(self.frame1,text="Age",font="Aerial 15 bold",bg="green",bd=22).grid(row=10,column=0)
              self.spin1 =Spinbox(self.frame1,from_=18,to=22,width=30,bd=2,textvariable= self.age).grid(row=10,column=1)
              self.button2 = Button(self.frame1, text="SUBMIT",width =10,font="Aerial 15 bold",bg="white",command = self.insert).grid(row=12,column=1)
              
             # def click():
                  #  self.mb=messageBox.showinfo("yeahh","yeeab")
              #self.l6=Checkbutton(self.frame1,text="I have checked the above conditions and i agree",selectcolor="blue",variable=self.confirm,width=30,height=30,command=click).grid(row=12,column=0)
            
          def insert(self):
               conn = sqlite3.connect('sql1.db')
               self.insertion=( self. teamNo.get(),self.name.get(),self.jn.get(),self.position.get(),self.age.get())
               conn.execute('INSERT INTO Players VALUES (?,?,?,?,?)',self.insertion)
               messagebox.showinfo("BASKETBALL PLAYERS MANAGEMENT SYSTEM SYSTEM","PLAYER ENROLLED")
               conn.commit()
               conn.close()
          def Exit(self):
               self.window.destroy()


              
