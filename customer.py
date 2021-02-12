import random
from tkinter import*
from tkinter import messagebox
import sqlite3

#con = sqlite3.connect("database.db")

"""
print("opened the database")
try:
    con.execute('''create table customer (ID int PRIMARY KEY NOT NULL, NAME TEXT , USERNAME TEXT, PASSWORD TEXT , ITEM TEXT,ITEM_PRICE INT)''')
except:
    pass
try:
    con.execute("insert into customer(ID,NAME,USERNAME,PASSWORD,ITEM,ITEM_PRICE) values(1,'Vaibhav','vai','vai','bag',800)")
except:
    pass
print("Entered successfuelly")
con.commit()

data = con.execute("select *from customer")
"""



e1=None;e2=None;e3=None;e4=None;e5=None;e6=None;
ee1=None;
def fun4():
    global e1,e2,e3,e4,e5,e6
    print(type(e1.get()),type(e2.get()))
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    try:
        sql  = "insert into customer(ID,NAME,USERNAME,PASSWORD,ITEM,ITEM_PRICE) values(?,?,?,?,?,?)"
        val = (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())
        cur.execute(sql,val)
        con.commit()
        messagebox.showinfo("Data inserted")

    except:
        messagebox.showinfo("Error:")

    con.close()


def fun1():
    m1 = Tk()
    m1.geometry("400x220")
    l1 = Label(m1,text ="Customer Id")
    l1.place(x=40,y=10)

    l2 = Label(m1,text ="Name")
    l2.place(x=40,y =40)

    l3 = Label(m1,text ="Username")
    l3.place(x=40,y =70)

    l4 = Label(m1,text ="Password")
    l4.place(x=40,y =100)

    l5 = Label(m1,text ="Item")
    l5.place(x=40,y=130)

    l6 = Label(m1,text ="Item Price")
    l6.place(x=40,y =160)

    global e1,e2,e3,e4,e5,e6
    e1 = Entry(m1)
    e1.place(x=120,y=10)

    e2 = Entry(m1)
    e2.place(x=120,y =40)

    e3 = Entry(m1)
    e3.place(x=120,y =70)

    e4 = Entry(m1)
    e4.place(x=120,y =100)

    e5 = Entry(m1)
    e5.place(x=120,y=130)

    e6 = Entry(m1)
    e6.place(x=120,y =160)

    b1= Button(m1,text="insert",command = fun4)
    b1.place(x = 120,y = 190)

    m1.mainloop()


def search():
    m3 = Tk()
    m3.geometry("400x220")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "select NAME,USERNAME,PASSWORD,ITEM,ITEM_PRICE from customer where ID = ? "
    val = ee1.get()
    tmp = cur.execute(sql,val)
    data = tmp.fetchall()
    data0 = data[0]
    Label(m3,text="Search Result").pack()
    ls=["Name","UserName","Password","Item","Item Price"]
    for i in range(len(data0)):
        Label(m3,text =ls[i]+str(" : ")+ str(data0[i]) ).pack()

    con.close()
    m3.mainloop()


def fun2():
    m2 = Tk()
    m2.geometry("400x220")

    ll1 = Label(m2,text ="Customer Id")
    ll1.pack()
    global ee1
    ee1 = Entry(m2)
    ee1.pack()

    bb1= Button(m2,text="Search",command = search)
    bb1.pack()

    m2.mainloop()

def fun3():
    if var.get()==1:
        fun1()
    else:
        fun2()


if __name__=="__main__":
    m = Tk()
    m.geometry("260x260")
    l= Label(m,text="Select Option :")
    l.pack()
    var = IntVar()
    var.set(1)
    r1 = Radiobutton(m,text ='Insert',variable = var,value=1)
    r2 = Radiobutton(m,text ='Query',variable = var,value=2)
    r1.pack()
    r2.pack()



    b = Button(m,text = "Next",command = fun3)
    b.pack()


    m.mainloop()



