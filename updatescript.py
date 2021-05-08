from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import MySQLdb


class UPDATEproduct():

    def resetpro(self):
        Q.set(0)
        t1.set('')
        t2.set('')
        t3.set('')
        t4.set('')
        t5.set('')
        t6 = []
        t7.set('')
        self.image = Image.open('Default/default.png')
        self.img = self.image.resize((200, 200))
        self.render = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.render)
         #canvas.create_image(0, 0, anchor=NW, image=self.render)
        return

    def idexistpro(self):
        self.abslist = []
        product_ID = Q.get()
        product_ID = int(product_ID)
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursorobj = db.cursor()
        sql = "select pid from product"
        cursorobj.execute(sql)
        data = cursorobj.fetchall()
        for (i,) in data:
            self.abslist.append(i)
        if product_ID not in self.abslist:
            messagebox.showwarning("Invalid input", "Enter valid product id")
            #messagebox.showwarning("Invalid input,Enter valid product id")
        else:
            self.getproduct()

    def browsePhoto(self):
        self.photo = Entry( textvariable=t7,state=NORMAL)
        filename1 = fd.askopenfilename()
        self.photo.insert(END, filename1)

    def UpdateData(self):
        self.pid=Q.get()
        self.name = t1.get()
        self.Category = t2.get()
        self.Price = t3.get()
        self.Quantity = t4.get()
        self.Discription = t5.get()
        self.photo = t7.get()

        if self.name == '' or self.Category == '' or self.Price == '' or self.Quantity == '' or self.Discription == '' :
            messagebox.showerror("Error", "Please enter all details first.....?")
        #sqlquery = "update cus set Name='" + self.name + "', Contact='" + self.contact + "',Email='" + self.email + "',Location='" + self.location + "' where Customer_ID='" + self.cid + "'"
        #cursor.execute(sqlquery)
        else:
            try:
                db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
                cursor = db.cursor()
                if self.photo=='':
                    sqlquery = "update product set name='" + self.name + "', category='" + self.Category + "',price='" + self.Price + "',quantity='" + self.Quantity + "',discription='" + self.Discription +  "' where pid='" + str(self.pid)+ "'"
                    cursor.execute(sqlquery ,)
                else:
                    binphoto = self.convertBinaryFun(self.photo)
                    sqlquery = "update product set name='" + self.name + "', category='" + self.Category + "',price='" + self.Price + "',quantity='" + self.Quantity + "',discription='" + self.Discription + "',prodimg=%s'" + "' where pid='" + str(
                        self.pid) + "'"
                    cursor.execute(sqlquery, (binphoto,))
                db.commit()
                messagebox.showinfo("Success", "Product details has been Updated succesfully.")
                rows = cursor.fetchall()
                self.resetpro()
                self.clear()
            except MySQLdb.Error as error:
                print('Failed to insert the record with image', error)

    def write_file(data, filename):
        with open(filename, "wb") as f:
            OrgData = f.write()
        return OrgData

    def convertBinaryFun(self, filename):
        # converting digital data into Binary format
        with open(filename, "rb") as f:
            binaryData = f.read()
        return binaryData

    def getproduct(self):
        pid = Q.get()
        print(pid)
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursorobj = db.cursor()
        sql = "select * from product  WHERE pid LIKE '%" + str(pid) + "%' "
        cursorobj.execute(sql)
        data = cursorobj.fetchone()
        productid = (data[0])
        t1.set(data[1])
        t2.set(data[2])
        t3.set(data[3])
        t4.set(data[4])
        t5.set(data[5])

        binpic = (data[6])
        StoreFilepath = "imgOut/img{0}.jpg".format(str(t1))
        with open(StoreFilepath, "wb") as f:
            f.write(binpic)
        self.image = Image.open('imgOut/imgPY_VAR0.jpg')
        self.img = self.image.resize((200, 200))
        self.render = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.render)
        self.canvas.pack()

        '''if pid==0 :
            messagebox.showinfo("Enter valid product id")
        else:'''

        ''''''


    def clear(self):
        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select pid,name,category,price,quantity,discription from product  "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)

    def update(self, rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i)

    def __init__(self, win):

        self.lbl1 = Label(win, text="Update Product to Alpha Inventory System...!", font=('arial', 15, 'bold'))
        # self.lbl1.pack(side=TOP,fill="both",expand="yes",padx=5,pady=3)
        self.lbl1.grid(row=1, column=0, padx=10, pady=5)

        w1 = LabelFrame(window, text='Enter Product Details here !')
        w1.grid(row=2, column=0, padx=10, pady=5)
        # w1.pack(side=LEFT,fill="both",expand="yes",padx=20,pady=10)

        w2 = LabelFrame(window, text='Product list', height="15")
        w2.grid(row=2, column=1, padx=5, pady=3)

        w3 = LabelFrame(window, text='search product using id', height="15")
        w3.grid(row=1, column=1, padx=5, pady=3)

        w4 = LabelFrame(window, text='', height="15")
        w4.grid(row=3, column=0, padx=15, pady=3)

        self.lbl2 = Label(w3, text="Enter Product id", font=('arial', 15))
        self.lbl2.grid(row=2, column=0, padx=10, pady=5)

        self.productid = Entry(w3, textvariable=Q)
        self.productid.grid(row=2, column=1, padx=10, pady=5)
        self.searchbtn = Button(w3, text="Search", command=self.idexistpro)
        self.searchbtn.grid(row=2, column=2, padx=10, pady=5)

        self.lname = Label(w1, text='Product_Name', font=('arial', 10))
        self.lname.grid(row=2, column=0, padx=10, pady=5)
        self.name = Entry(w1, textvariable=t1)
        self.name.grid(row=2, column=1, padx=10, pady=5)

        self.lCategory = Label(w1, text='Category', font=('arial', 10))
        self.lCategory.grid(row=4, column=0, padx=10, pady=5)
        self.Category = ttk.Combobox(w1, textvariable=t2, values=["Food", "Grocery", "Clothes"], font=('arial', 10))
        self.Category.grid(row=4, column=1, padx=10, pady=5)

        self.lPrice = Label(w1, text='Price', font=('arial', 10))
        self.lPrice.grid(row=6, column=0, padx=10, pady=5)
        self.Price = Entry(w1, textvariable=t3)
        self.Price.grid(row=6, column=1, padx=10, pady=5)

        self.lQuantity = Label(w1, text='Quantity', font=('arial', 10))
        self.lQuantity.grid(row=8, column=0, padx=10, pady=5)
        self.Quantity = Entry(w1, textvariable=t4)
        self.Quantity.grid(row=8, column=1, padx=10, pady=5)

        self.lDiscription = Label(w1, text='Discription', font=('arial', 10))
        self.lDiscription.grid(row=10, column=0, padx=10, pady=5)
        self.Discription = Entry(w1, textvariable=t5)
        self.Discription.grid(row=10, column=1, padx=10, pady=5)

        self.photo = Entry(w1, textvariable=t7,state=DISABLED)
        self.photo.grid(row=12, column=2, padx=10, pady=5)

        self.photobtn = Button(w1, text='Browse Image to Update',command=self.browsePhoto)
        self.photobtn.grid(row=12, column=1, padx=10, pady=5)

        self.submitbtn = Button(w4, text='Update Record', command=self.UpdateData)

        self.submitbtn.grid(row=14, column=1, padx=10, pady=5)
        self.resetbtn = Button(w4, text="Reset", command=self.resetpro)
        self.resetbtn.grid(row=14, column=2, padx=10, pady=5)

        w1a = LabelFrame(w1, text='Product Image!')
        w1a.grid(row=2, column=2, padx=10, pady=5, rowspan=10)
        self.canvas = tk.Canvas(w1a, bg="grey", width=200, height=200)
        self.image=Image.open('Default/default.png')
        self.resized=self.image.resize((200,200))
        self.render = ImageTk.PhotoImage(file='Default/default.png')
        self.canvas.create_image(0, 0, anchor=NW, image=self.render)
        self.canvas.pack()

        self.trv = ttk.Treeview(w2, columns=(1, 2, 3, 4, 5, 6), show="headings", height="15")

        self.trv.pack(side=LEFT, expand='yes', fill='both')

        self.trv.heading(1, text="Product ID")
        self.trv.heading(2, text="Product Name")
        self.trv.heading(3, text="Category")
        self.trv.heading(4, text="Price")
        self.trv.heading(5, text="Quantity")
        self.trv.heading(6, text="Discription")
        #self.trv.heading(7, text="product image")
        self.trv.pack(side=LEFT, expand='yes', fill='both')
        self.trv.column('#0', stretch=NO, minwidth=0, width=50)
        self.trv.column('#1', stretch=NO, minwidth=0, width=100)
        self.trv.column('#2', stretch=NO, minwidth=0, width=100)
        self.trv.column('#3', stretch=NO, minwidth=0, width=100)
        self.trv.column('#4', stretch=NO, minwidth=0, width=100)
        self.trv.column('#5', stretch=NO, minwidth=0, width=100)
        self.trv.column('#6', stretch=NO, minwidth=0, width=100)
        #self.trv.column('#7', stretch=NO, minwidth=0, width=100)

        db = MySQLdb.connect('localhost', 'root', '2904', 'alphadb')
        cursor = db.cursor()
        query = "select * from product "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.clear()
        #w2.pack(,fill="both",expand="yes")


window = Tk()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 =StringVar()
t7= StringVar()
Q = IntVar()
productid=2
obj=UPDATEproduct(window)
window.title('Update Product....!')
window.iconbitmap(bitmap='C:/newproduct.jfif')
window.configure(background='#856ff8')
window.geometry('1200x500+300+200')
window.mainloop()
