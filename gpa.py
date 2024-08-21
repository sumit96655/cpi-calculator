import tkinter as tk
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

from tkinter import messagebox

grade1 = []
grade1point = []
credit1 = []


class cgpa:

    def __init__(self):
        # Basic GUI window for Calculator
        self.window = tk.Tk()
        self.window.geometry('850x600+350+80')
        self.window.configure(bg="cornsilk")
        self.window.title("CGPA CALCULATOR")

        # methods
        self.Title()
        self.CreateLabel1()
        self.CreateFrame2()
        self.CreateFrame3()
        self.CalculateButton()
        self.ClearButton()
        self.SaveButton()
        self.DataButton()
        self.update_button()

    def Title(self):
        title = tk.Label(self.window, text='CGPA CALCULATOR', font=('times new roman', 20, "normal"), bg='white',
                         fg='maroon', bd=10, relief=tk.GROOVE)
        title.place(x=0, y=5, height=50, width=850)

    def CreateLabel1(self):
        self.lb_name = tk.Label(self.window, text="Name: ", font=('times new roman', 13, "bold"), fg='black',
                                bg='cornsilk')
        self.lb_name.place(x=50, y=80)
        self.regno = tk.Label(self.window, text="Registration Number: ", font=('times new roman', 13, "bold"),
                                 fg='black', bg='cornsilk')
        self.regno.place(x=500, y=80)

        Name = tk.StringVar()
        Registration = tk.StringVar()

        self.name = tk.Entry(self.window, textvariable=Name, width=30, font=('times new roman', 13, "normal"), bd='2')
        self.name.place(x=120, y=80)
        self.regno = tk.Entry(self.window, textvariable=Registration, width=15, font=('times new roman', 13, "normal"), bd='2')
        self.regno.place(x=690, y=80)

    def CreateFrame2(self):
        self.lb_sem = tk.LabelFrame(self.window,font=('times new roman', 10, "normal"), fg='black',
                                    bg='cornsilk3', height=500, width=800)
        self.lb_sem.place(x=30, y=130)
        txt_labels = tk.Label(self.lb_sem,
                              text='                Course Title                                                                 Course Code                                                 Credit                                       Grade Obtained         ',
                              font=('times new roman', 10, "normal"), bg='burlywood4', fg='black')
        txt_labels.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
        self.sub1 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=30)
        self.sub1.grid(row=2, column=0, pady=5)
        self.code1 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=20)
        self.code1.grid(row=2, column=1, pady=5)
        self.credit1 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.credit1.grid(row=2, column=2, pady=5)
        self.grade1 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.grade1.grid(row=2, column=3, pady=5)
        self.sub2 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=30)
        self.sub2.grid(row=4, column=0, pady=5, rowspan=2)
        self.code2 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=20)
        self.code2.grid(row=4, column=1, pady=5, rowspan=2)
        self.credit2 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.credit2.grid(row=4, column=2, pady=5, rowspan=2)
        self.grade2 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.grade2.grid(row=4, column=3, pady=5, rowspan=2)
        self.sub3 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=30)
        self.sub3.grid(row=6, column=0, pady=5, rowspan=2)
        self.code3 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=20)
        self.code3.grid(row=6, column=1, pady=5, rowspan=2)
        self.credit3 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.credit3.grid(row=6, column=2, pady=5, rowspan=2)
        self.grade3 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.grade3.grid(row=6, column=3, pady=5, rowspan=2)
        self.sub4 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=30)
        self.sub4.grid(row=8, column=0, pady=5, rowspan=2)
        self.code4 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=20)
        self.code4.grid(row=8, column=1, pady=5, rowspan=2)
        self.credit4 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.credit4.grid(row=8, column=2, pady=5, rowspan=2)
        self.grade4 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.grade4.grid(row=8, column=3, pady=5, rowspan=2)
        self.sub5 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=30)
        self.sub5.grid(row=10, column=0, pady=5, rowspan=2)
        self.code5 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=20)
        self.code5.grid(row=10, column=1, pady=5, rowspan=2)
        self.credit5 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.credit5.grid(row=10, column=2, pady=5, rowspan=2)
        self.grade5 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.grade5.grid(row=10, column=3, pady=5, rowspan=2)
        self.sub6 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=30)
        self.sub6.grid(row=12, column=0, pady=5, rowspan=2)
        self.code6 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=20)
        self.code6.grid(row=12, column=1, pady=5, rowspan=2)
        self.credit6 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.credit6.grid(row=12, column=2, pady=5, rowspan=2)
        self.grade6 = tk.Entry(self.lb_sem, font=('times new roman', 10, "normal"), bg='white', fg='black', width=10)
        self.grade6.grid(row=12, column=3, pady=5, rowspan=2)
        
    def clear_lists(self):
        grade1.clear()
        grade1point.clear()
        credit1.clear()
    
    def CreateFrame3(self):
        lb_cgpa = tk.Label(self.window, font=('times new roman', 20, "normal"), fg='black', bg='cornflowerblue', padx=65, pady=25,
                           text='Your GPA is: ')
        lb_cgpa.place(x=30, y=380)
        self.gpavalue = tk.Label(self.window, font=('times new roman', 40, "normal"), fg='maroon', bg='cornflowerblue', padx=108,
                            pady=10, text=0.00)
        self.gpavalue.place(x=30, y=460)

    def CalculateButton(self):
        self.lb_calculate = tk.Button(self.window, font=('times new roman', 16, "normal"), fg='black', bg='aquamarine4',
                                      height=3, width=34, text='Calculate CGPA', command= self.calculate_command)
        self.lb_calculate.place(x=380, y=380)

    def ClearButton(self):
        self.lb_clear = tk.Button(self.window, font=('times new roman', 10, "bold"), fg='black', bg='grey', height=2,
                                  width=15, text='CLEAR', command=self.clear_command)
        self.lb_clear.place(x=380, y=480)

    def SaveButton(self):
        self.lb_save = tk.Button(self.window, font=('times new roman', 10, "bold"), fg='black', bg='grey', height=2,
                                 width=15, text='SAVE', command=self.save_command)
        self.lb_save.place(x=530, y=480)

    def DataButton(self):
        self.lb_next = tk.Button(self.window, font=('times new roman', 10, "bold"), fg='black', bg='grey', height=2,
                                 width=15, text='DATA', command=self.Data_command)
        self.lb_next.place(x=680, y=480)
    
    def update_button(self):
        self.lb_update = tk.Button(self.window, font=('times new roman', 10, "bold"), fg='black', bg='grey', height=2,
                                 width=15, text='UPDATE', command=self.update_command)
        self.lb_update.place(x=530, y=540)



    def calculate_command(self):
        try:
            print("Calculate GPA Button Pressed.")
            list = ['AA', 'aa', 'AB', 'ab', 'BB', 'bb', 'BC', 'bc', 'CC', 'cc', 'CD', 'cd', 'DD', 'dd', 'FF', 'ff']
            num = [1, 2, 3, 4, 0]
            if (self.grade1.get() in list) and (self.grade2.get() in list) and (
                    self.grade3.get() in list) and \
                    (self.grade4.get() in list) and (
                    self.grade5.get() in list) and \
                    (self.grade6.get() in list) and (int(self.credit1.get()) in num) and (
                    int(self.credit2.get()) in num) and \
                    (int(self.credit3.get()) in num) and (int(self.credit4.get()) in num) and (
                    int(self.credit5.get()) in num) and (int(self.credit6.get()) in num):

                c1, c2, c3, c4, c5, c6 = self.credit1.get(), self.credit2.get(), self.credit3.get(), self.credit4.get(), self.credit5.get(), self.credit6.get()
                credit1.append(int(c1))
                credit1.append(int(c2))
                credit1.append(int(c3))
                credit1.append(int(c4))
                credit1.append(int(c5))
                credit1.append(int(c6))
                print(credit1)
                g1, g2, g3, g4, g5, g6 = self.grade1.get(), self.grade2.get(), self.grade3.get(), self.grade4.get(), self.grade5.get(), self.grade6.get()
                g1 = g1.upper()
                grade1.append(g1)
                g2 = g2.upper()
                grade1.append(g2)
                g3 = g3.upper()
                grade1.append(g3)
                g4 = g4.upper()
                grade1.append(g4)
                g5 = g5.upper()
                grade1.append(g5)
                g6 = g6.upper()
                grade1.append(g6)
                print(grade1)
                y = 0
                while (y < 6):
                    if (grade1[y] == "AA"):
                        number = 10
                        grade1point.append(number)
                    elif (grade1[y] == "AB"):
                        number = 9
                        grade1point.append(number)
                    elif (grade1[y] == "BB"):
                        number = 8
                        grade1point.append(number)
                    elif (grade1[y] == "BC"):
                        number = 7
                        grade1point.append(number)
                    elif (grade1[y] == "CC"):
                        number = 6
                        grade1point.append(number)
                    elif (grade1[y] == "CD"):
                        number = 5
                        grade1point.append(number)
                    elif (grade1[y] == "DD"):
                        number = 4
                        grade1point.append(number)
                    elif (grade1[y] == "FF"):
                        number = 0
                        grade1point.append(number)
                    y = y + 1
                print(grade1point)
                i = 0
                self.tgpa, first_part1, second_part1 = 0.00, 0, 0
                while (i < 6):
                    first_part1 += credit1[i] * grade1point[i]
                    second_part1 += credit1[i]
                    i = i + 1
                self.tgpa = first_part1 / second_part1
                self.tgpa = "{:.2f}".format(self.tgpa)
                print(self.tgpa)
                self.gpavalue["text"] = self.tgpa
            else:
                messagebox.showinfo("Information",
                                    "Please choose credit and grades from following values only.\n\n Grades = [ 'AA', "
                                    "'aa', 'AB', 'ab', 'BB', 'bb', 'BC', 'bc', 'CC', 'cc', 'CD', 'cd', 'DD', 'dd', "
                                    "'FF', 'ff' ]\n\nCredits = [ 1, 2, 3, 4, 0 ]")
                
            self.clear_lists()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
        
        pass

     
    def clear_command(self):
        self.name.delete(0, tk.END)
        self.regno.delete(0, tk.END)
        self.sub1.delete(0, tk.END)
        self.sub2.delete(0, tk.END)
        self.sub3.delete(0, tk.END)
        self.sub4.delete(0, tk.END)
        self.sub5.delete(0, tk.END)
        self.sub6.delete(0, tk.END)
        self.code1.delete(0, tk.END)
        self.code2.delete(0, tk.END)
        self.code3.delete(0, tk.END)
        self.code4.delete(0, tk.END)
        self.code5.delete(0, tk.END)
        self.code6.delete(0, tk.END)
        self.credit1.delete(0, tk.END)
        self.credit2.delete(0, tk.END)
        self.credit3.delete(0, tk.END)
        self.credit4.delete(0, tk.END)
        self.credit5.delete(0, tk.END)
        self.credit6.delete(0, tk.END)
        self.grade1.delete(0, tk.END)
        self.grade2.delete(0, tk.END)
        self.grade3.delete(0, tk.END)
        self.grade4.delete(0, tk.END)
        self.grade5.delete(0, tk.END)
        self.grade6.delete(0, tk.END)


    

    def save_command(self):
        try:
            print("Save button Pressed.")
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            list = []
            if self.name.get() == "" or self.regno.get() == "" or self.gpavalue.cget('text') == "" or self.sub1.get()=="" or self.sub2.get()=="" or self.sub3.get()=="" or self.sub4.get()=="" or self.sub5.get() or self.sub6.get()=="" or self.code1.get()=="" or self.code2.get()=="" or self.code3.get()=="" or self.code4.get()=="" or self.code5.get()=="" or self.code6.get()=="" :
                print("Enter data before saving.")
                messagebox.showerror("Error..!!", "Enter all required data before saving..!!!")
            else:
                cur.execute("""SELECT * from studentdetails;""")
                while True:
                    value = cur.fetchone()
                    if value == None:
                        break
                    if self.regno.get() == str(value[1]):
                        list.append(str(value[1]))
                print("list=", list)
                if self.regno.get() in list:
                    print("Data already present.")
                    messagebox.showerror("Error", "SORRY..!!\nData already present.\n")
                else:
                    cur.execute('SELECT * FROM studentdetails')
                    print(self.name.get() + self.regno.get() + str(self.gpavalue.cget('text')))
                    cur.execute('INSERT INTO studentdetails VALUES(?,?,?)', (str(self.name.get()), (str(self.regno.get())), (str(self.gpavalue.cget('text')))))
                    print("Data Saved Successfully.")
                    messagebox.showinfo("Saved", "Data Saved Successfully..!!!")
                    con.commit()
                    print(cur.fetchall())
                    con.close()
        except:
            messagebox.showerror("Error", "Something went wrong..!!!\n")
        pass

    def askClearConfirmation(self):
        isTrue = tk.messagebox.askyesno("Seeking Confimation","Do you really want to clear series data?\nOnce cleared it cannot be restored")
        if (isTrue):
            self.clear_entries()

    def clear_entries(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT COUNT (*) FROM studentdetails')
        count = cur.fetchone()[0]
        cur.execute('DELETE FROM studentdetails;',)
        con.commit()
        for i in range(0, count):
            self.name1.configure(text="")
            self.reg.configure(text="")
            self.gpa.configure(text="")
            
            
    def update_command(self):
        list = []
        print('update button pressed')
        con = sqlite3.connect('database.db')    
        cur= con.cursor()
        cur.execute('SELECT * FROM studentdetails')
        r = cur.fetchall
        while True:
            value = cur.fetchone()
            if value == None:
                break
            if self.regno.get() == str(value[1]):
                list.append(str(value[1]))
                
        print("list=", list)
        if self.regno.get() in list:
            print("Data present.")
            list.append(str(self.gpavalue.cget('text')))
            cur.execute('INSERT INTO studentdetails VALUES(?,?,?)', (str(self.name.get()), (str(self.regno.get())), (str(self.gpavalue.cget('text')))))
            
            messagebox.showinfo("Success", "CGPA updated successfully")
        else:
            cur.execute('SELECT * FROM studentdetails')
            print(self.name.get() + self.regno.get() + str(self.gpavalue.cget('text')))
            cur.execute('INSERT INTO studentdetails VALUES(?,?,?)', (str(self.name.get()), (str(self.regno.get())), (str(self.gpavalue.cget('text')))))
            print("Data Saved Successfully.")
        messagebox.showinfo("Saved", "Data Saved Successfully..!!!")
        con.commit()
        print(cur.fetchall())
        con.close()
        
    def Data_command(self):
        nx = tk.Tk()
        nx.geometry("500x650")
        nx.title("Data")

        p1 = tk.Label(nx, text="Name", font="time 15 bold")
        p1.grid(row=1, column=0, padx=10, pady=10)
        p2 = tk.Label(nx, text="Reg no.", font="time 15 bold")
        p2.grid(row=1, column=1, padx=10, pady=10)
        p3 = tk.Label(nx, text="CGPA", font="time 15 bold")
        p3.grid(row=1, column=2, padx=10, pady=10)

        clear = tk.Button(nx, text="Clear ALL data", command=self.askClearConfirmation)
        clear.grid(row=0, column=0, padx=10, pady=10)

        graph = tk.Button(nx, text="Show Graph", command=self.Bar_Graph)
        graph.grid(row=0, column=1, padx=10, pady=10)

        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM studentdetails')
        num = 2
        r = cur.fetchall()
        for i in r:
            self.name1 = tk.Label(nx, text=i[0], font=("time 12 bold"), fg="maroon")
            self.name1.grid(row=num, column=0, padx=10, pady=10)
            self.reg = tk.Label(nx, text=i[1], font=("time 12 bold"), fg="maroon")
            self.reg.grid(row=num, column=1, padx=10, pady=10)
            self.gpa = tk.Label(nx, text=i[2], font=("time 12 bold"), fg="maroon")
            self.gpa.grid(row=num, column=2, padx=10, pady=10)
            num = num + 1


        con.commit()
        con.close()

    def Bar_Graph(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT name, gpavalue from studentdetails')
        r = cur.fetchall()
        names = []
        gpas = []

        for i in r:
            names.append(i[0])
            gpas.append(i[1])

        print("Names of Students = ", names)
        print("Marks of Students = ", gpas)

        plt.bar(names, gpas)
        plt.ylim(0, 10)

        plt.xlabel("Names of Students")
        plt.ylabel("CGPA of Students")
        plt.title("Student's Comparitive CGPA")

        plt.show()
        con.commit()
        con.close()



    # to start/run the machinery
    def run(self):
        self.window.mainloop()


# main function to run gpa where cal is an object of class Cgpa
if __name__ == "__main__":
    cal = cgpa()
    cal.run()
