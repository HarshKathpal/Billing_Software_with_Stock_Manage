from tkinter import*
from tkinter import ttk
import math,random,os
from tkinter import messagebox
import datetime
import time
import calendar
import pandas as pd
import datahandle
import ast    # "[]" ===>>>[]

class Bill_app:
    def __init__(self,root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.title("BHARAT ELECTRICALS")
        bg_color = "#074463"
        title = Label(self.root,text="BHARAT ELECTRICALS",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill = X)

        #==================Read file====================================================
        data = pd.read_excel("main_data.xlsx",usecols=["com_item","com_combo","com_stock"])
        data = data[~data['com_item'].isna()]
        d = len(data['com_item'])

        data1 = pd.DataFrame()
        data1 = data[0:int(d/2)]
        self.d1 = len(data1.com_item)

        data2 = pd.DataFrame()
        data2 = data[int(d/2):]
        data2 = data2.reset_index(drop=True)
        self.d2 = len(data2.com_item)
        
        #===========quantity_variable=========================
        self.wire_quantity_variable= [] # create an empty list
        for i in range(0,self.d1):
            self.wire_quantity_variable.append(IntVar())
            
        #==============rs_variable===============================
        self.wire_rs_variable = [] # create an empty list
        for i in range(0,self.d1):
            self.wire_rs_variable.append(IntVar())

        #==============value_variable===========================
        self.wire_value_variable = [] # create an empty list
        for i in range(0,self.d1):
            self.wire_value_variable.append(StringVar())

        #==============stock_variable===========================

        self.wire_stock_variable = [] # create an empty list(temp list only for show)
        for i in range(0,self.d1):
            self.wire_stock_variable.append(IntVar())

        #===============combobox_variable========================
        self.wrc = [] 
        for i in range(0,self.d1):
            self.wrc.append(StringVar())

        #==============fan=====================================
        #==============value_variable===========================
        self.fan_value_variable = [] # create an empty list
        for i in range(0,self.d2):
            self.fan_value_variable.append(StringVar())
        #===========fan_quantity_variable======
        self.fan_quantity_variable= [] # create an empty list
        for i in range(0,self.d2):
            self.fan_quantity_variable.append(IntVar())

        #===========fan_rs_variable=============
        self.fan_rs_variable= [] # create an empty list
        for i in range(0,self.d2):
            self.fan_rs_variable.append(IntVar())

        #============stock_variable==============
        sto1 = list(data2.com_stock)
        self.stock1=[]
        for i in sto1:
            res = ast.literal_eval(i)
            self.stock1.append(res)
        self.fan_stock_variable = [] # create an empty list
        for i in range(0,self.d2):
            self.fan_stock_variable.append(IntVar())

        #============fan_combobox_variable==========
        self.frc = [] # create an empty list
        for i in range(0,self.d2):
            self.frc.append(StringVar())
            
        #=============================total_variable=======================================================
        self.total_price = StringVar()
        self.total_quantity = IntVar()

        #==================customers_detail=====================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.c_add=StringVar()
        self.c_email=StringVar()
        
        self.bill_no=StringVar()
        bill_num = [1000]
        for i in os.listdir("customer_bills/"):
            bill_num.append(int(i.split(".")[0]))
        x = max(bill_num)+1 
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        # _____________________________customer detail frame___________________________________________________________
        
        
        F1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)
        cname_txt = Entry(F1,width=13,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cadd_lbl = Label(F1,text="Customer Add.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=10)
        cadd_txt = Entry(F1,width=13,textvariable=self.c_add,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

        cphn_lbl = Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=10,pady=10)
        cphn_txt = Entry(F1,width=13,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=10)

        cemail_lbl = Label(F1,text="Customer Email id",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=6,padx=10,pady=10)
        cemail_txt = Entry(F1,width=13,textvariable=self.c_email,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=7,padx=10,pady=10)

        #________________________________________________________new detail label_____________________

        F2 = LabelFrame(self.root,text="Wire",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=490,height=400)

        canvas2 = Canvas(F2)
        canvas2.pack(side="left",fill="both")
        canvas2.configure(width=490,height=100)
        
        yscrollbar2 = Scrollbar(F2,orient="vertical",command=canvas2.yview)
        yscrollbar2.pack(side = RIGHT,fill = "y")

        canvas2.configure(yscrollcommand=yscrollbar2.set)
        canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox('all')))
        

        my_frame2 = Frame(canvas2,width=490,height=400,bg=bg_color)
        canvas2.create_window((0,0), window=my_frame2)
        
        bath_lbl = Label(canvas2,text="""           Items                      Entry            Rs.        Quantity       Stock   """,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=4,relief=GROOVE).grid(row=0,column=0)
        space_lbl = Label(my_frame2,text="                ",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")
        
        self.text_wire = data1['com_item']  # item from data.xlsx
        #===========combobox_item=================================
        combobox = list(data1.com_combo) 
        self.combi = []
        for i in combobox:
            res = ast.literal_eval(i)
            self.combi.append(res)
        #===========stock set=====================================
        sto = list(data1.com_stock)
        self.stock=[]
        for i in sto:
            res = ast.literal_eval(i)
            self.stock.append(res)

        for i in range(len(self.text_wire)):
            text = Label(my_frame2,text=self.text_wire[i],font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=i+1,column=0,padx=10,pady=10,sticky="w")
            txt_combo = ttk.Combobox(my_frame2,value=self.combi[i],textvariable=self.wire_value_variable[i],width=4,state="readonly",font=("times new roman",15,"bold")).grid(row=i+1,column=1,padx=2,pady=5)
            txt_entry = Entry(my_frame2,width=5,textvariable=self.wire_rs_variable[i],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=i+1,column=2,padx=5,pady=5)
            txt_entry = Entry(my_frame2,width=5,textvariable=self.wire_quantity_variable[i],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=i+1,column=3,padx=(5,4),pady=5)
            m3_txt = Entry(my_frame2,width=5,textvariable=self.wire_stock_variable[i],state=DISABLED,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=i+1,column=4,padx=(5,4),pady=5)



        #==================================================f3===================================================

        F3 = LabelFrame(self.root,text="Fan",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=500,y=180,width=490,height=400)
        canvas3 = Canvas(F3)
        canvas3.pack(side="left",fill="both")
        canvas3.configure(width=450,height=100)
        
        yscrollbar3 = Scrollbar(F3,orient="vertical",command=canvas3.yview)
        yscrollbar3.pack(side = RIGHT,fill = "y")

        canvas3.configure(yscrollcommand=yscrollbar3.set)
        canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox('all')))
        my_frame3 = Frame(canvas3,width=500,height=400,bg=bg_color)
        canvas3.create_window((0,0), window=my_frame3)

        bath_lbl = Label(canvas3,text="           Items                      Entry            Rs.        Quantity       Stock   ",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=4,relief=GROOVE).grid(row=0,column=0,sticky="w")
        space_lbl = Label(my_frame3,text="                ",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")
        
        self.text_fan = data2['com_item']  # item from data.xlsx
        # #===========combobox_item=================================
        combobox1 = list(data2.com_combo) 
        self.combi1 = []
        for i in combobox1:
            res = ast.literal_eval(i)
            self.combi1.append(res)

        for i in range(len(self.text_fan)):
            text = Label(my_frame3,text=self.text_fan[i],font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=i+1,column=0,padx=10,pady=10,sticky="w")
            txt_combo = ttk.Combobox(my_frame3,value=self.combi1[i],textvariable=self.fan_value_variable[i],width=5,state="readonly",font=("times new roman",15,"bold")).grid(row=i+1,column=1,padx=2,pady=5)
            txt_entry = Entry(my_frame3,width=5,textvariable=self.fan_rs_variable[i],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=i+1,column=2,padx=5,pady=5)
            txt_entry = Entry(my_frame3,width=5,textvariable=self.fan_quantity_variable[i],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=i+1,column=3,padx=(5,4),pady=5)
            m4_txt = Entry(my_frame3,width=5,textvariable=self.fan_stock_variable[i],state=DISABLED,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=i+1,column=4,padx=(5,4),pady=5)

        #==========================================================bill area=========================================
        F6 = Frame(self.root,bd=10,relief=GROOVE)
        F6.place(x=995,y=180,width=365,height=306)
        bill_title=Label(F6,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea = Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=================search bill===============================================================================
        F7 = LabelFrame(self.root,text="Search Bill",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F7.place(x=995,y=486)

        c_bill_lbl = Label(F7,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=2)
        c_bill_txt = Entry(F7,width=10,font="arial 15",bd=5,textvariable=self.search_bill,relief=SUNKEN).grid(row=0,column=1,padx=15,pady=2)

        bill_btn = Button(F7,text="Search",command=self.find_bill,width=9,bd=5,font="arial 12 bold").grid(row=0,column=2,pady=2,padx=5)

        #=============================f8===============================================================================
        F8 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F8.place(x=0,y=570,relwidth=1,height=140)
        
        stock_btn=Button(F8,text="Stock",command=self.stocks,width=16,height=1,bd=6,font="arial 33 bold").grid(row=0,column=0,padx=6,pady=5)
        
        
        # btn
        btn_F=Frame(F8,bd=7,relief=GROOVE,bg=bg_color)
        btn_F.place(x=465,width=875,height=105)
        
        m2_lbl = Label(btn_F,text="Total Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")
        m2_txt = Entry(btn_F,width=18,textvariable=self.total_price,state=DISABLED,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        m3_lbl = Label(btn_F,text="Total Quantity",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=10,pady=1,sticky="w")
        m3_txt = Entry(btn_F,width=18,textvariable=self.total_quantity,state=DISABLED,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=6,pady=2)
        GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=6,pady=2)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=1,column=0,padx=6,pady=2)
        Exit_btn=Button(btn_F,command=self.exit_app,text="Exit",bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=1,column=1,padx=6,pady=2)
        self.welcome_bill()
    #============================total===========================================================================
    def total(self):
        self.stocks()
        total_wire_qua = 0
        total_wire_rs = 0
        total_fan_qua = 0
        total_fan_rs =0
        
        for i in range(len(self.text_wire)):
            total_wire_rs = total_wire_rs + (self.wire_rs_variable[i].get() * self.wire_quantity_variable[i].get())
            total_wire_qua = total_wire_qua + self.wire_quantity_variable[i].get()

        for i in range(len(self.text_fan)):
            total_fan_rs = total_fan_rs + (self.fan_rs_variable[i].get() * self.fan_quantity_variable[i].get())
            total_fan_qua = total_fan_qua + self.fan_quantity_variable[i].get()

        if (total_wire_qua + total_fan_qua)!=0:
            self.total_price.set(str(total_wire_rs +total_fan_rs)+" Rs." )
            self.total_quantity.set( total_wire_qua + total_fan_qua)
        else:
            messagebox.showerror("Error","You did not select any Item.")
    
    #===================================welcome_bill=================================================================
    def welcome_bill(self,time=None):
        t4,t2 = Bill_app.clock()
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tBharat Electicals\n")
        self.txtarea.insert(END,f"Data : {t4}\t\t\tTime : {time}\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n Customer Add : {self.c_add.get()}")
        self.txtarea.insert(END,f"\n Email id : {self.c_email.get()}")
        self.txtarea.insert(END,f"\n========================================")
        self.txtarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n========================================") 




    def bill_area(self):
        self.stocks()
        if self.c_name.get()=="" and self.c_phon.get()=="":
            messagebox.showerror("Error","Please Enter Customer Details...")
        elif self.c_name.get().isalpha() != True:
            messagebox.showerror("Error","Please Enter Valid Customer Name...")
        elif (self.c_phon.get().isdigit() != True) or (len(self.c_phon.get()) != 10) :
            messagebox.showerror("Error","Mobile Number must be integers and having 10 digits")
        else:
            t4,t2 = Bill_app.clock()
            self.welcome_bill(t2)
            self.total()
            for i in range(len(self.text_wire)):
                if self.wire_quantity_variable[i].get() != 0:
                    if self.wire_quantity_variable[i].get()<=self.wire_stock_variable[i].get():
                        self.txtarea.insert(END,f"\n {self.text_wire[i]} {self.wire_value_variable[i].get()}\t\t{self.wire_quantity_variable[i].get()}\t\t{self.wire_rs_variable[i].get()}")
                        self.wire_stock_variable[i].set(self.wire_stock_variable[i].get()-self.wire_quantity_variable[i].get())
                        combo_var = self.wire_value_variable[i].get()
                        ind = self.combi[i].index(combo_var)
                        self.stock[i][ind] = self.wire_stock_variable[i].get()
                    else:
                        messagebox.showerror("Error",f"please check stock for {self.text_wire[i]}...")
                        return

            for i in range(len(self.text_fan)):
                if self.fan_quantity_variable[i].get() != 0:
                    if self.fan_quantity_variable[i].get()<=self.fan_stock_variable[i].get():
                        self.txtarea.insert(END,f"\n {self.text_fan[i]} {self.fan_value_variable[i].get()}\t\t{self.fan_quantity_variable[i].get()}\t\t{self.fan_rs_variable[i].get()}")
                        self.fan_stock_variable[i].set(self.fan_stock_variable[i].get()-self.fan_quantity_variable[i].get())
                        combo_var = self.fan_value_variable[i].get()
                        ind = self.combi1[i].index(combo_var)
                        self.stock1[i][ind] = self.fan_stock_variable[i].get()
                    else:
                        messagebox.showerror("Error",f"please check stock for {self.text_fan[i]}...")
                        return


            if self.total_quantity.get() != 0:
                self.txtarea.insert(END,f"\n----------------------------------------")
                self.txtarea.insert(END,f"\n Total : {self.total_price.get()}")
                self.txtarea.insert(END,f"\n Total Quantity : {self.total_quantity.get()}")
                self.txtarea.insert(END,f"\n----------------------------------------")
                self.save_bill() 
    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data = self.txtarea.get("1.0",END)
            f1 = open("customer_bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
            self.clear_data()
        else:
            return
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("customer_bills/"):
            if i.split(".")[0] == self.search_bill.get():
                present= "yes"
                f1 = open(f"customer_bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
        
    
    def clear_data(self):
        op = messagebox.askyesno("Clear","Do you really want to Clear the data?")
        if op>0:
            for i in range(0,self.d1):
                self.wire_quantity_variable[i].set(0)

            for i in range(0,self.d2):
                self.fan_quantity_variable[i].set(0)

            self.total_price.set("")
            self.total_quantity.set(0)

        #==================customers_detail=====================
            self.c_name.set("")
            self.c_phon.set("")
            self.c_add.set("")
            self.c_email.set("")

            self.bill_no.set("")
            bill_num = [1000]
            for i in os.listdir("customer_bills/"):
                bill_num.append(int(i.split(".")[0]))
            x = max(bill_num)+1 
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
        

    def stocks(self):
        # print("in stock")
        for i in range(len(self.text_wire)):
            try:
                # print("in stock loop")
                combo_var = self.wire_value_variable[i].get()
                # print(combo_var)
                ind = self.combi[i].index(combo_var)
                self.wire_stock_variable[i].set(self.stock[i][ind])
            except:
                pass
        for i in range(len(self.text_fan)):
            try:
                # print("in stock loop")
                combo_var = self.fan_value_variable[i].get()
                # print(combo_var)
                ind = self.combi1[i].index(combo_var)
                self.fan_stock_variable[i].set(self.stock1[i][ind])
            except:
                pass
        
        
    #=======================================================EXIT=====================================================
    def exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.delete()
            datahandle.datahandle_last()
            self.root.destroy()
    
    #==========================data in main file===========================================

    def delete(self):
        com_item = list(self.text_wire) + list(self.text_fan)
        com_combo = self.combi +self.combi1
        com_stock = self.stock +self.stock1
        x_dataframe = pd.DataFrame()
        x_dataframe['com_item'] = com_item
        x_dataframe['com_combo'] = com_combo
        x_dataframe['com_stock'] = com_stock
        
        x_dataframe.to_excel("main_data.xlsx")

        
#=============================clock=============================================================================
    @staticmethod
    def clock():   
        # bg_color = "#074463"
        # F9 = LabelFrame(root,bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        # F9.place(x=0,y=710,relwidth=1,height=60) 
        t2 = time.strftime("%H:%M:%S %p")
        # t3 = Label(F9,text=t2,font=("ds digital",20,"bold"),fg="light green",bg=bg_color)
        # t3.after(200,Bill_app.clock)
        # t3.grid(row=0,column=0)
        t4 = datetime.date.today()
        born = datetime.datetime.today().weekday()
        # day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        # t5 = Label(F9,text=day_name[born],font=("ds digital",20,"bold"),fg="light green",bg=bg_color).grid(row=0,column=1,padx=(450,0))
        # t5 = Label(F9,text=t4,font=("ds digital",20,"bold"),fg="light green",bg=bg_color).grid(row=0,column=2,padx=(460,0))
        return t4,t2

    

datahandle.datahandle_first()
root = Tk()
Bill_app.clock()
obj = Bill_app(root)
root.mainloop()