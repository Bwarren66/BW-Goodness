from tkinter import*

#-------------instance/window size/color/name-------------------------------------------

root=Tk()
root.geometry("1200x500")
root.configure(bg="red")
root.title("B.W. Goodness")

#-------------frames-------------------------------------------------------

Tops=Frame(root,bd=10,relief=RIDGE, bg='red')
Tops.pack(side=TOP)

menu_frame = Frame(root,bd=10, relief=RIDGE, bg='red')
menu_frame.pack(side=LEFT)

info_frame=Frame(root, bd=10, relief=RIDGE, bg='red')
info_frame.pack(side=LEFT)

#-----------------Restaurant Name------------------------------------------

name = Label(Tops, font=('arial' ,25, 'bold'),text="B.W. Goodness", fg='white', bg='red',bd=9,anchor='center', width=20)
name.grid(row=0,column=0)


#-----------calculate total/ validation code/ thank you message------------------------

def calculate():
    try: Cheeseburger=int(Cheeseburger_entry.get())
    except: Cheeseburger=0
    try: Pizzaslice=int(Pizzaslice_entry.get())
    except: Pizzaslice=0
    try: Hotdog=int(Hotdog_entry.get())
    except: Hotdog=0
    try: Fries=int(Fries_entry.get())
    except: Fries=0
    try: Soda=int(Soda_entry.get())
    except: Soda=0
    try: Water=int(Water_entry.get())
    except: Water=0

    total=(int(Cheeseburger)*5)+(int(Pizzaslice)*4)+(int((Hotdog)*4)+(int(Fries)*3)+(int(Soda)*2)+(int(Water)*1))
    totalorderlbl=Label(info_frame, font=('arial' , 18, 'bold'), bg='yellow', text="Total amount of order is $"+str(total)+ " Thank you for your order!", anchor="center")
    totalorderlbl.grid(row=0, column=0)

Thanklbl=Label(info_frame, font=('arial' , 18, 'bold'), bg='yellow', text=("We appreciate your business!"), bd=8, anchor='center')
Thanklbl.grid(row=1, column=0)

#--------exit command--------------------------------------------------------------    

def iExit():
    root.destroy()

#------------reset command---------------------------------------------------------

def reset():
    Cheeseburger.set("")
    Pizzaslice.set("")
    Hotdog.set("")
    Fries.set("")
    Soda.set("")
    Water.set("")
    Total.set("")
    
#-------------------------------variables and strings----------------------

Cheeseburger = IntVar()
Pizzaslice = IntVar()
Hotdog = IntVar()
Fries = IntVar()
Soda = IntVar()
Water = IntVar()
Total = IntVar()

Cheeseburger=StringVar()
Pizzaslice=StringVar()
Hotdog=StringVar()
Fries=StringVar()
Soda=StringVar()
Water=StringVar()
Total=StringVar()

Cheeseburger.set("")
Pizzaslice.set("")
Hotdog.set("")
Fries.set("")
Soda.set("")
Water.set("")
Total.set("")

#-------------------menu list and entry form--------------------------------------------

Menulbl=Label(menu_frame, font=('arial' , 15, 'bold'), bg='red', text="MENU",  bd=8, anchor='w')
Menulbl.grid(row=0, column=0)

Qty=Label(menu_frame, font=('arial' , 15, 'bold'), bg='red', text="QUANTITY",  bd=8, anchor='w')
Qty.grid(row=0, column=1)

Cheeseburger_menu = Label(menu_frame,font=('arial' , 15, 'bold'), fg='white',bg='red', text="Cheeseburger",  bd=8, anchor='w')
Cheeseburger_menu.grid(row=1, column=0)

Cheeseburger_entry = Entry(menu_frame,font=('arial' , 15, 'bold'), textvariable=Cheeseburger, bd=6, width=6, bg="white", justify='center')
Cheeseburger_entry.grid(row=1, column=1)

Pizzaslice_menu = Label(menu_frame,font=('arial' , 15, 'bold'), fg='white', bg='red', text="Pizza Slice", bd=8, anchor='w')
Pizzaslice_menu.grid(row=2, column=0)

Pizzaslice_entry = Entry(menu_frame,font=('arial' , 15, 'bold'), textvariable=Pizzaslice, bd=6, width=6, bg="white", justify='center')
Pizzaslice_entry.grid(row=2, column=1)

Hotdog_menu = Label(menu_frame, font=('arial' , 15, 'bold'), fg='white', bg='red', text="Hot Dog",bd=8, anchor='w')
Hotdog_menu.grid(row=3, column=0)

Hotdog_entry = Entry(menu_frame, font=('arial' , 15, 'bold'), textvariable=Hotdog, bd=6, width=6, bg="white", justify='center')
Hotdog_entry.grid(row=3, column=1)

Fries_menu = Label(menu_frame, font=('arial' , 15, 'bold'), fg='white', bg='red', text="Fries",  bd=8, anchor='w')
Fries_menu.grid(row=4, column=0)

Fries_entry = Entry(menu_frame, font=('arial' , 15, 'bold'), textvariable=Fries,  bd=6, width=6, bg="white", justify='center')
Fries_entry.grid(row=4, column=1)

Soda_menu = Label(menu_frame, font=('arial' , 15, 'bold'), fg='white', bg='red', text="Soda",  bd=8, anchor='w')
Soda_menu.grid(row=5, column=0)

Soda_entry = Entry(menu_frame,font=('arial' , 15, 'bold'), textvariable=Soda, bd=6, width=6, bg="white", justify='center')
Soda_entry.grid(row=5, column=1)

Water_menu = Label(menu_frame, font=('arial' , 15, 'bold'), fg='white', bg='red', text="Water",  bd=8, anchor='w')
Water_menu.grid(row=6, column=0)

Water_entry = Entry(menu_frame,font=('arial' , 15, 'bold'), textvariable=Water, bd=6, width=6, bg="white", justify='center')
Water_entry.grid(row=6, column=1)

#-----------------------------------------view menu picture------------------------------------------

#View_Cheeseburger=Label(menu_frame, fg="white", bg="green", font=("arial", 13, "bold"), text="View", bd=8)
#View_Cheeseburger.grid(row=1, column=2)

#View_Pizzaslice=Label(menu_frame,fg="white", bg="green", font=("arial", 13, "bold"), text="View", bd=8)
#View_Pizzaslice.grid(row=2, column=2)

#View_Hotdog=Label(menu_frame,fg="white", bg="green", font=("arial", 13, "bold"), text="View", bd=8)
#View_Hotdog.grid(row=3, column=2)

#View_Fries=Label(menu_frame,fg="white", bg="green", font=("arial", 13, "bold"), text="View", bd=8)
#View_Fries.grid(row=4, column=2)

#View_Soda=Label(menu_frame,fg="white", bg="green", font=("arial", 13, "bold"), text="View", bd=8)
#View_Soda.grid(row=5, column=2)

#View_Water=Label(menu_frame,fg="white", bg="green", font=("arial", 13, "bold"), text="View", bd=8)
#View_Water.grid(row=6, column=2)


#-----------total/reset/exit buttons-------------------------------

Total_button=Button(menu_frame,padx=16,pady=8, bd=5 ,fg="white",font=('arial' ,10,'bold'),width=5, text="ORDER", bg="green",command=calculate)
Total_button.grid(row=8, column=1)

Reset_button=Button(menu_frame,padx=16,pady=8, bd=5 ,fg="white",font=('arial' ,10,'bold'),width=5, text="RESET", bg="green",command=reset)
Reset_button.grid(row=8, column=3)

Exit_button=Button(menu_frame,padx=16,pady=8, bd=5 ,fg="white",font=('arial' ,10,'bold'),width=5, text="EXIT", bg="green",command=iExit)
Exit_button.grid(row=8, column=4)

#-------------------------view menu prices in new window and view menu prices button--------------------

def price():
    root = Tk()
    root.geometry("550x300")
    root.title("Price List")
    root.configure(bg="red")
    button1=Button(root,padx=16,pady=8, bd=5 ,fg="white",font=('arial' ,10,'bold'),width=5, bg="green",text="EXIT", command=root.destroy)
    button1.grid(row=10, column=2)

    Menu_label = Label(root, text="Menu List", font=('arial', 20, 'bold'), bg="red", fg="black", bd=5)
    Menu_label.grid(row=3, column=0)
    Menu_price = Label(root, font=('arial', 20, 'bold'), text="Price",bg="red", fg="black", anchor=W)
    Menu_price.grid(row=3, column=3)
    Menu_label1 = Label(root, font=('arial', 14,'bold'), text="_____________",  bg="red", fg="red", anchor=W)
    Menu_label1.grid(row=3, column=2)
    Cheeseburger_label = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="Cheeseburger", anchor=W)
    Cheeseburger_label.grid(row=4, column=0)
    Cheeseburger_Cost = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="$5", anchor=W)
    Cheeseburger_Cost.grid(row=4, column=3)
    Pizzaslice_label = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="Pizza Slice", anchor=W)
    Pizzaslice_label.grid(row=5, column=0)
    Pizzaslice_Cost = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="$4", anchor=W)
    Pizzaslice_Cost.grid(row=5, column=3)
    Hotdog_label = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="Hot Dog", anchor=W)
    Hotdog_label.grid(row=6, column=0)
    Hotdog_Cost = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="$4", anchor=W)
    Hotdog_Cost.grid(row=6, column=3)
    Fries_label = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="Fries", anchor=W)
    Fries_label.grid(row=7, column=0)
    Fries_Cost = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="$3", anchor=W)
    Fries_Cost.grid(row=7, column=3)
    Soda_label = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="Soda", anchor=W)
    Soda_label.grid(row=8, column=0)
    Soda_Cost = Label(root, font=('arial', 18, 'bold'), fg="white", bg="red", text="$2", anchor=W)
    Soda_Cost.grid(row=8, column=3)
    Water_label = Label(root, font=('arial', 18, 'bold'),fg="white",  bg="red", text="Water",  anchor=W)
    Water_label.grid(row=9, column=0)
    Water_Cost = Label(root, font=('arial', 18, 'bold'), fg="white",  bg="red", text="$1",  anchor=W)
    Water_Cost.grid(row=9, column=3)

Price_button=Button(menu_frame,padx=16,pady=8, bd=5 ,fg="white",font=('arial' ,10,'bold'),width=11, text="VIEW MENU PRICE", bg="green",command=price)
Price_button.grid(row=8, column=0)

#----------------root.mainloop() ending----------------------------------------------------------

root.mainloop()



