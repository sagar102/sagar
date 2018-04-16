import tkinter
from tkinter import *
from main import *
def display_all():
	root = Tk()
	t=Text(root)
	root.title("CALCULATION TABLE")
	t.insert(END,"***********************************************************************************")
	t.insert(END,"CALCULATIOIN FOR WEEKDAYS FREE TABEL")
	t.pack()
	mainloop()
if __name__ == "__main__":
	Tk = tkinter.Tk
	root = Tk()
	entry1 = {}
	entry2 = {}
	root.title("ATM SIMULATION ")
	root.geometry("1370x800")
	v = StringVar()
	lb=Label(root,text="ENTER THE NO OF CUSTOMERs:",height=1)
	lb.config(font=('times', 13))
	lb.place(x=10,y=10)
	entry=Entry(root,textvariable=v,width=10)
	entry.place(x=300,y=10)
	entry.insert(0,"10")
	button = Button(root, text='OK', command=display_all)
	button.place(x=400,y=70)
	root.mainloop()
	
