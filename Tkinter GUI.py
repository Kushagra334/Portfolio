from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as c


def Insert():
    id = id_entry.get()
    name = name_entry.get()
    salary = salary_entry.get()
    city = city_entry.get()
    phone = phone_entry.get()

    if (id == "" or name == "" or salary == "" or city == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please enter all fields")

    try:
        if any(ch.isalpha() for ch in id) or len(id) > 4:
            MessageBox.showerror("ERROR", "Invalid ID!!")
        elif any(ch.isnumeric() for ch in name):
            MessageBox.showerror("ERROR", "Invalid Name!!")
        elif any(ch.isalpha() for ch in salary) or not salary.isnumeric():
            MessageBox.showerror("ERROR", "Invalid Salary!!")
        elif any(ch.isnumeric() for ch in city):
            MessageBox.showerror("ERROR", "Invalid City!!")
        elif any(ch.isalpha() for ch in phone) or not phone.isnumeric() or len(phone) != 10:
            MessageBox.showerror("ERROR", "Invalid Phone!!")
        else:
            con = c.connect(host="localhost", user="root",password="kushagra123#", database="project")
            cursor = con.cursor()
            cursor.execute("insert into employee values({},'{}',{},'{}','{}')".format(id, name, salary, city, phone))
            cursor.execute("commit")
            MessageBox.showinfo("STATUS", "Successfully Inserted")
            con.close()
    except Exception as ep: 
        MessageBox.showerror("ERROR",ep)

def Update():
    id=id_entry.get()
    name = name_entry.get()
    salary = salary_entry.get()
    city = city_entry.get()
    phone = phone_entry.get()

    if (name == "" or salary == "" or city == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please enter fields you want to update!")
    
    try:
        if any(ch.isalpha() for ch in id) or len(id) > 4:
            MessageBox.showerror("ERROR", "Invalid ID!!")
        elif any(ch.isnumeric() for ch in name):
            MessageBox.showerror("ERROR", "Invalid Name!!")
        elif any(ch.isalpha() for ch in salary) or not salary.isnumeric():
            MessageBox.showerror("ERROR", "Invalid Salary!!")
        elif any(ch.isnumeric() for ch in city):
            MessageBox.showerror("ERROR", "Invalid City!!")
        elif any(ch.isalpha() for ch in phone) or not phone.isnumeric() or len(phone) != 10:
            MessageBox.showerror("ERROR", "Invalid Phone!!")
        else:
            con = c.connect(host="localhost", user="root",password="kushagra123#", database="project")
            cursor = con.cursor()
            cursor.execute("update employee set name = '{}', salary={}, city='{}', phone='{}' where id ={}".format(name, salary, city, phone, id))
            cursor.execute("commit")
            MessageBox.showinfo("STATUS", "Successfully Updated")
            con.close()
    except Exception as ep: 
        MessageBox.showerror("ERROR",ep)

def Del():

    if (id_entry.get() == ""):
        MessageBox.showinfo("ALERT", "Please enter ID to delete row")
    else:
        con = c.connect(host="localhost", user="root",
                        password="kushagra123#", database="project")
        cursor = con.cursor()
        cursor.execute("delete from employee where id='" +
                       id_entry.get() + "'")
        cursor.execute("commit")

        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        salary_entry.delete(0, 'end')
        city_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

        MessageBox.showinfo("Status", "Successfully Deleted")
        con.close()


def Select():

    if (id_entry.get() == ""):
        MessageBox.showinfo("ALERT", "ID is required to select row!")
    else:
        con = c.connect(host="localhost", user="root", password="kushagra123#", database="project")
        cursor = con.cursor()
        cursor.execute("select * from employee where id= '" +id_entry.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            name_entry.insert(0, row[1])
            salary_entry.insert(0, row[2])
            city_entry.insert(0, row[3])
            phone_entry.insert(0, row[4])

        con.close()


GUI = Tk()
GUI.geometry("500x500")
GUI.title("Employee Registration Portal")

id = Label(GUI, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=30)
id_entry = Entry(GUI, font=("verdana 15"))
id_entry.place(x=180, y=30)

name = Label(GUI, text="Name:", font=("verdana 15"))
name.place(x=50, y=80)
name_entry = Entry(GUI, font=("verdana 15"))
name_entry.place(x=180, y=80)

salary = Label(GUI, text="Salary:", font=("verdana 15"))
salary.place(x=50, y=130)
salary_entry = Entry(GUI, font=("verdana 15"))
salary_entry.place(x=180, y=130)

city = Label(GUI, text="City:", font=("verdana 15"))
city.place(x=50, y=180)
city_entry = Entry(GUI, font=("verdana 15"))
city_entry.place(x=180, y=180)

phone = Label(GUI, text="Phone:", font=("verdana 15"))
phone.place(x=50, y=230)
phone_entry = Entry(GUI, font=("verdana 15"))
phone_entry.place(x=180, y=230)

btnInsert = Button(GUI, text="Insert", command=Insert,font=("verdana 15")).place(x=100, y=300)
btnDelete = Button(GUI, text="Delete", command=Del,font=("verdana 15")).place(x=200, y=300)
btnUpdate = Button(GUI, text="Update", command=Update,font=("verdana 15")).place(x=300, y=300)
btnSelect = Button(GUI, text="Select", command=Select,font=("verdana 15")).place(x=200, y=350)

GUI.mainloop()
