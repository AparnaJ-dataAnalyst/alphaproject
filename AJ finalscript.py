# Python-AlpphaInventorySoft
import MySQLdb
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter.ttk as ttk
import os
import sys
import os

#import MySQLdb
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

class AlphaSystem:

    def exit(self):
        result = tkMessageBox.askquestion('Alpha Inventory System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            window.destroy()
            exit()

    def addcustomeritem(self):
        self.win2 = Tk()

        frame = LabelFrame(self.win2, text="Add New customer Record")
        frame.grid(row=0, column=1)

        Label(frame, text='Firstname').grid(row=1, column=1)
        self.firstname = Entry(frame, bd=4)
        self.firstname.grid(row=1, column=2)

        Label(frame, text='Lasttname').grid(row=2, column=1)
        self.lastname = Entry(frame, bd=4)
        self.lastname.grid(row=2, column=2)

        Label(frame, text='Username').grid(row=3, column=1)
        self.username = Entry(frame, bd=4)
        self.username.grid(row=3, column=2)

        Label(frame, text='Email').grid(row=4, column=1)
        self.email = Entry(frame, bd=4)
        self.email.grid(row=4, column=2)

        ttk.Button(frame, text='Add Record', command=self.addcustomer).grid(row=5, column=2)
        self.message = Label(text='', fg='red')
        self.message.grid(row=6, column=1)
        self.win2.title("Customer Registration...!")
        self.win2.configure(background='#856ff8')
        self.win2.geometry('530x460+300+200')
        self.win2.mainloop()

    def addcustomer(self, w1):
        self.fname = self.firstname.get()
        self.lname = self.lastname.get()
        self.uname = self.username.get()
        self.email = self.email.get()

        if self.fname == '':
            messagebox.showerror("Error", "Please enter firstname first.....?")
        elif self.lname == '':
            messagebox.showerror("Error", "Please enter lasttname first.....?")
        elif self.uname == '':
            messagebox.showerror("Error", "Please enter username first.....?")
        elif self.email == '':
            messagebox.showerror("Error", "Please enter email first.....?")
        else:
            db = MySQLdb.connect("localhost", "root", "2904", "alphadb")
            cursor = db.cursor()
            sqlquery = "insert into customer(firstname,lastname,username,email) values(%s,%s,%s,%s)"
            try:
                cursor.execute(sqlquery, (self.fname, self.lname, self.uname, self.email))
                db.commit()
            except:
                db.rollback()
            db.close()
            messagebox.showinfo("Success", "customer added successfully....!")

    def resetaddpro(self):
        self.pname.delete(0, END)
        self.pCategory.delete(0, END)
        self.pPrice.delete(0, END)
        self.pQuantity.delete(0, END)
        self.pDiscription.delete(0, END)
        self.pphoto.delete(0, END)
        # self.Q.set(0)

    def addproductitem(self):

        self.win3 = Tk()

        self.lbl1 = Label(self.win3, text="Add Product to Alpha Inventory System...!", font=('arial', 15, 'bold'))
        self.lbl1.grid(row=1, column=0, padx=10, pady=5)
        # self.lbl1.pack(side=TOP,fill="both",expand="yes",padx=5,pady=3)

        self.w1 = LabelFrame(self.win3, text='Enter Product Details here !')
        self.w1.grid(row=2, column=0, padx=10, pady=5)
        # w1.pack(side=LEFT,fill="both",expand="yes",padx=20,pady=10)

        self.w2 = LabelFrame(self.win3, text='Product list', height="15")
        self.w2.grid(row=2, column=1, padx=5, pady=3)
        # w2.pack(side=LEFT,fill="both",expand="yes",padx=20,pady=20)

        self.lname = Label(self.w1, text='Product_Name', font=('arial', 10))

        self.lname.grid(row=2, column=0, padx=10, pady=5)
        self.pname = Entry(self.w1)
        self.pname.grid(row=2, column=1, padx=10, pady=5)

        self.lCategory = Label(self.w1, text='Category', font=('arial', 10))
        self.lCategory.grid(row=4, column=0, padx=10, pady=5)
        self.pCategory = ttk.Combobox(self.w1, values=["Food", "Grocery", "Clothes"], font=('arial', 10))
        self.pCategory.grid(row=4, column=1, padx=10, pady=5)

        self.lPrice = Label(self.w1, text='Price', font=('arial', 10))
        self.lPrice.grid(row=6, column=0, padx=10, pady=5)
        self.pPrice = Entry(self.w1)
        self.pPrice.grid(row=6, column=1, padx=10, pady=5)

        self.lQuantity = Label(self.w1, text='Quantity', font=('arial', 10))
        self.lQuantity.grid(row=8, column=0, padx=10, pady=5)
        self.pQuantity = Entry(self.w1)
        self.pQuantity.grid(row=8, column=1, padx=10, pady=5)

        self.lDiscription = Label(self.w1, text='Discription', font=('arial', 10))
        self.lDiscription.grid(row=10, column=0, padx=10, pady=5)
        self.pDiscription = Entry(self.w1)
        self.pDiscription.grid(row=10, column=1, padx=10, pady=5)

        self.lProduct_Image = Label(self.w1, text='Product_Image', font=('arial', 10))
        self.lProduct_Image.grid(row=12, column=0, padx=10, pady=3)
        self.pphoto = Entry(self.w1)
        self.pphoto.grid(row=12, column=1, padx=10, pady=5)
        self.photobtn = Button(self.w1, text='Browse Image', command=self.browsePhoto)
        self.photobtn.grid(row=12, column=2, padx=10, pady=5)

        self.submitbtn = Button(self.w1, text='Add Record', command=self.insertData)
        self.submitbtn.grid(row=14, column=1, padx=10, pady=5)
        self.resetbtn = Button(self.w1, text="Reset", command=self.resetaddpro)
        self.resetbtn.grid(row=14, column=2, padx=10, pady=5)

        self.trv = ttk.Treeview(self.w2, columns=(1, 2, 3, 4, 5, 6), show="headings", height="15")
        self.trv.pack(side=LEFT, expand='yes', fill='both')
        self.trv.column('#0', stretch=NO, minwidth=0, width=50)
        self.trv.column('#1', stretch=NO, minwidth=0, width=100)
        self.trv.column('#2', stretch=NO, minwidth=0, width=100)
        self.trv.column('#3', stretch=NO, minwidth=0, width=50)
        self.trv.column('#4', stretch=NO, minwidth=0, width=50)
        self.trv.column('#5', stretch=NO, minwidth=0, width=50)
        self.trv.column('#6', stretch=NO, minwidth=0, width=100)

        self.trv.heading(1, text="Product ID")
        self.trv.heading(2, text="Product Name")
        self.trv.heading(3, text="Category")
        self.trv.heading(4, text="Quantity")
        self.trv.heading(5, text="Price")
        self.trv.heading(6, text="Discription")

        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select pid,name,category,price,quantity,discription from product "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.clear()

        frame = LabelFrame(self.win3, text="Add New Product Record")
        frame.grid(row=0, column=2)

        self.win3.title("PRODUCT ADDITION..!")
        self.win3.configure(background='#856ff8')
        self.win3.geometry('1050x500')
        self.win3.mainloop()


    def convertBinaryFun(self, filename):
        # converting digital data into Binary format
        with open(filename, "rb") as f:
            binaryData = f.read()
        return binaryData

    def browsePhoto(self):
        filename1 = fd.askopenfilename()
        self.pphoto.insert(END, filename1)

    def insertData(self):
        self.name = self.pname.get()
        self.Category = self.pCategory.get()
        self.Price = self.pPrice.get()
        self.Quantity = self.pQuantity.get()
        self.Discription = self.pDiscription.get()
        self.photo = self.pphoto.get()

        if self.name == '' or self.Category == '' or self.Price == '' or self.Quantity == '' or self.Discription == '' or self.photo == '':
            messagebox.showerror("Error", "Please enter all details first.....?")

        else:
            try:
                db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
                cursor = db.cursor()
                sqlquery = "insert into product(name,category,price,quantity,discription,prodimg) values(%s,%s,%s,%s,%s,%s)"
                binphoto = self.convertBinaryFun(self.photo)
                res = cursor.execute(sqlquery,
                                     (self.name, self.Category, self.Price, self.Quantity, self.Discription, binphoto))
                db.commit()
                messagebox.showinfo("Success", "Product has been saved succesfully.")
                rows = cursor.fetchall()
                self.clear()
            except MySQLdb.Error as error:
                print('Failed to insert the record with image', error)

    def clear(self):
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        # self.Q.set(0)
        cursor = db.cursor()
        query = "select pid,name,category,price,quantity,discription from product  "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)

    def update(self, rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i)

    def updateproductitem(self):
        os.system('python updatescript.py')
        '''self.win10= Tk()
        self.obj=UPDATEproduct.__init__(self.win10)
        self.win10.mainloop()'''
    def Filterbyid(self):
        # self.pid=Q.get()
        self.pid = self.productid.get()
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select * from product where pid=  " + str(self.pid)
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)

    def Filterbyname(self):
        self.pname = self.productname.get()
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        # query = "select * from product WHERE name="+ str(self.pname)
        query = "select * from product WHERE  name LIKE '%" + str(self.pname) + "%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)

    def Filterbycat(self):
        self.pcatgory = self.productcategory.get()
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        # query =  " select * from product where category='" + self.pcatgory + "'"
        query = "select * from product WHERE  category LIKE '%" + str(self.pcatgory) + "%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)

    def Viewproductitem(self):
        self.win5 = Tk()
        self.lbl1 = Label(self.win5, text="View or Search Product", font=('arial', 15, 'bold'))
        # self.lbl1.pack(side=TOP,fill="both",expand="yes",padx=5,pady=3)
        self.lbl1.grid(row=1, column=0, padx=25, pady=5)

        self.w1 = LabelFrame(self.win5, text='filter')
        self.w1.grid(row=2, column=0, padx=10, pady=5)

        self.w1a = LabelFrame(self.w1, text='')
        self.w1a.grid(row=2, column=0, padx=10, pady=5, rowspan=10)

        self.lbl1 = Label(self.w1a, text="Product Id", font=('arial', 10, 'bold'))
        self.lbl1.pack(side=LEFT, expand='no', fill='both')

        self.productid = tk.Entry(self.w1a)  # ,textvariable=t1
        self.productid.pack(side=LEFT, expand='no', fill='both')

        self.SEARCHbtn = Button(self.w1a, text="SEARCH", command=self.Filterbyid)
        self.SEARCHbtn.pack(side=BOTTOM, expand='no', fill='both')

        self.w1b = LabelFrame(self.w1, text='')
        self.w1b.grid(row=2, column=1, padx=10, pady=5, rowspan=10)

        self.lbl1 = Label(self.w1b, text="Product name", font=('arial', 10, 'bold'))
        self.lbl1.pack(side=LEFT, expand='no', fill='both')

        self.productname = tk.Entry(self.w1b)
        # ,textvariable=t1
        self.productname.pack(side=LEFT, expand='no', fill='both')

        self.SEARCHbtn = Button(self.w1b, text="SEARCH", command=self.Filterbyname)
        self.SEARCHbtn.pack(side=BOTTOM, expand='no', fill='both')

        self.w1c = LabelFrame(self.w1, text='')
        self.w1c.grid(row=2, column=2, padx=10, pady=5, rowspan=10)

        self.lbl1 = Label(self.w1c, text="Product Category", font=('arial', 10, 'bold'))
        self.lbl1.pack(side=LEFT, expand='no', fill='both')

        # self.productcategory = Entry(w1c, textvariable=t2)  #
        self.productcategory = ttk.Combobox(self.w1c, values=["Food", "Grocery", "Clothes"], font=('arial', 10))
        self.productcategory.pack(side=LEFT, expand='no', fill='both')

        self.SEARCHbtn = Button(self.w1c, text="SEARCH", command=self.Filterbycat)
        self.SEARCHbtn.pack(side=BOTTOM, expand='no', fill='both')

        self.w2 = LabelFrame(self.win5, text='table')
        self.w2.grid(row=4, column=0, padx=10, pady=5)
        self.trv = ttk.Treeview(self.w2, columns=(1, 2, 3, 4, 5, 6), show="headings", height="15")

        self.trv.pack(side=LEFT, expand='yes', fill='both')

        self.trv.heading(1, text="Product ID")
        self.trv.heading(2, text="Product Name")
        self.trv.heading(3, text="Category")
        self.trv.heading(4, text="Quantity")
        self.trv.heading(5, text="Price")
        self.trv.heading(6, text="Discription")
        #self.trv.heading(7, text="Product image")
        self.trv.pack(expand='yes', fill='both')

        '''self._img = tk.PhotoImage(file="imagename.gif") #change to your file path
        self.tree.insert('', 'end', text="#0's text", image=self._img,
                         value=("A's value", "B's value"))'''

        self.trv.column('#0', stretch=NO, minwidth=0, width=100)
        self.trv.column('#1', stretch=NO, minwidth=0, width=100)
        self.trv.column('#2', stretch=NO, minwidth=0, width=200)
        self.trv.column('#3', stretch=NO, minwidth=0, width=150)
        self.trv.column('#4', stretch=NO, minwidth=0, width=100)
        self.trv.column('#5', stretch=NO, minwidth=0, width=100)
        self.trv.column('#6', stretch=NO, minwidth=0, width=150)
        #self.trv.column('#7', stretch=NO, minwidth=0, width=100)
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select * from product "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.clear()


        self.win5.configure(background='#856ff8')
        # window.configure(background='#856ff8')
        self.win5.geometry('950x573+300+200')
        self.win5.mainloop()

    def Deleteproductitem(self):
        self.win4 = Tk()

        self.lbl1 = Label(self.win4, text="Delete Product to Alpha Inventory System...!", font=('arial', 15, 'bold'))
        # self.lbl1.pack(side=TOP,fill="both",expand="yes",padx=5,pady=3)
        self.lbl1.grid(row=1, column=1, padx=10, pady=5)

        self.w2 = LabelFrame(self.win4, text='Product list', height="15")
        self.w2.grid(row=5, column=1, padx=5, pady=3)
        # w2.pack(side=LEFT,fill="both",expand="yes",padx=20,pady=20)

        self.w3 = LabelFrame(self.win4, text='search product using id', height="15")
        self.w3.grid(row=3, column=1, padx=5, pady=3)

        self.lbl2 = Label(self.w3, text="Enter Product id", font=('arial', 15))
        self.lbl2.grid(row=2, column=0, padx=10, pady=5)

        self.pidQ = Entry(self.w3)
        self.pidQ.grid(row=2, column=1, padx=10, pady=5)
        self.DELETEbtn = Button(self.w3, text="DELETE", command=self.idexist)
        self.DELETEbtn.grid(row=2, column=2, padx=10, pady=5)
        self.RESETbtn = Button(self.w3, text="RESET", command=self.resetdelpro)
        self.RESETbtn.grid(row=2, column=3, padx=10, pady=5)

        self.trv = ttk.Treeview(self.w2, columns=(1, 2, 3, 4, 5, 6), show="headings", height="15")

        self.trv.pack(expand='yes', fill='both')

        self.trv.heading(1, text="Product ID")
        self.trv.heading(2, text="Product Name")
        self.trv.heading(3, text="Category")
        self.trv.heading(4, text="Quantity")
        self.trv.heading(5, text="Price")
        self.trv.heading(6, text="Discription")
        self.trv.pack(side=LEFT, expand='yes', fill='both')
        self.trv.column('#0', stretch=NO, minwidth=0, width=100)
        self.trv.column('#1', stretch=NO, minwidth=0, width=100)
        self.trv.column('#2', stretch=NO, minwidth=0, width=100)
        self.trv.column('#3', stretch=NO, minwidth=0, width=100)
        self.trv.column('#4', stretch=NO, minwidth=0, width=100)
        self.trv.column('#5', stretch=NO, minwidth=0, width=100)
        self.trv.column('#6', stretch=NO, minwidth=0, width=100)

        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select pid,name,category,price,quantity,discription from product "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.clear()
        self.win4.title("PRODUCT deletion..!")
        self.win4.configure(background='#856ff8')
        self.win4.geometry('800x460+300+200')
        self.win4.mainloop()

    def resetdelpro(self):
        self.pidQ.delete(0, END)
        self.clear()

    def search(self):
        product_ID = self.pidQ.get()
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select * from product WHERE  pid LIKE '%" + str(product_ID) + "%' "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)
        print(self.pidQ)

    def idexist(self):
        product_ID = self.pidQ.get()
        product_ID = int(product_ID)
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursorobj = db.cursor()
        sql = "select pid from product"
        cursorobj.execute(sql)
        data = cursorobj.fetchall()
        abslist = []
        for (i,) in data:
            abslist.append(i)
        if product_ID not in abslist:
            messagebox.showerror("Error", "invalid product id")
        else:
            self.deleteproduct()

    def deleteproduct(self):
        product_ID = self.pidQ.get()
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this record?"):
            query = "DELETE FROM product WHERE pid =" + str(product_ID)
            cursor.execute(query)
            db.commit()
            self.clear()
        else:
            return True
        self.pidQ.delete(0, END)

    def __init__(self, win):
        AlphaSystem.win = win

        self.img = ImageTk.PhotoImage(Image.open("image/inventory1.jpg"))
        self.lbl1 = Label(win, image=self.img)
        self.lbl1.place(x=0, y=0, relwidth=1, relheight=1)
        self.lbl1 = Label(win, text="Welcome to Alpha Inventory System...!", font=('algerian', 22, 'bold'))
        self.lbl1.place(x=400, y=30)

        # ------------Menubar-------------------------
        chooser = Menu()

        itemone = Menu(tearoff=0)
        itemone.add_command(label='Add Product', command=self.addproductitem)
        itemone.add_command(label='Update Product', command=self.updateproductitem)
        itemone.add_command(label='Delete Product', command=self.Deleteproductitem)
        itemone.add_separator()
        itemone.add_command(label='View\Search', command=self.Viewproductitem)

        item2 = Menu(tearoff=1)
        item2.add_command(label='Add Customer', command=self.addcustomeritem)
        item2.add_command(label='Edit Customer')
        item2.add_command(label='Delete Customer')
        item2.add_separator()
        item2.add_command(label='Help')

        chooser.add_cascade(label='User Profile')
        chooser.add_cascade(label='Admin Master')
        chooser.add_cascade(label='Customer Master', menu=item2)
        chooser.add_cascade(label='Product Master', menu=itemone)
        chooser.add_cascade(label='Order Master')
        chooser.add_cascade(label='Reports')
        chooser.add_cascade(label='Help')

        chooser.add_cascade(label='Exit', command=self.exit)

        win.config(menu=chooser)


if __name__ == '__main__':
    window = Tk()

    alpha = AlphaSystem(window)
    window.title("Alpha Inventory System...!!!")
    window.geometry('1487x954')
    window.iconbitmap( bitmap='image/inventoryicon.png')
    window.configure(background='white')
    window.mainloop()
