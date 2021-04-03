import MySQLdb
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import*

#Database Connection
def connection():
    global conn, cursor
    conn = MySQLdb.connect(host = 'localhost', database = 'python_project', user = 'root', password = '1304')
    cursor = conn.cursor()

root = Tk()
root.geometry('900x400')
root.title('Contact Management System')

#Display Function for making the 4 frames and the contents of each frame.
def display_frames():

    global tree
    global search   
    global ID, First_Name, Last_Name, gender, email, contact_no
    search = StringVar()
    ID = StringVar()
    First_Name = StringVar()
    Last_Name = StringVar()
    gender = StringVar()
    email = StringVar()
    contact_no = StringVar()

    f1 = Frame(root, width = 600, height = 100, bg = '#4b1675')
    f1.pack(side = TOP, fil = X)

    f2 = Frame(root, width = 400, height = 350, bg = '#b866fa')
    f2.pack(side = LEFT, fil = Y)

    f3 = Frame(root, width = 500, height = 350, bg = '#7836ad')
    f3.pack(side = LEFT, fil = Y)

    f4 = Frame(root,width = 650, bg = 'yellow')
    f4.pack(side = RIGHT, fil = Y)


    #f1 content
    lbtitle = Label(f1, text = "CONTACT MANAGEMENT SYSTEM", font = ('Arial', 20, 'bold italic'), fg = 'white', bg = '#4b1675')
    lbtitle.pack(pady = 20)


    #f2 content
    lbfname = Label(f2, text = "FIRST NAME", font = ('Arial', 15,  'bold italic'), fg = 'black', bg = '#b866fa')
    lbfname.pack(padx = 125, pady = 15)
    efname = Entry(f2, width = 25, fg = 'black', bg = 'white', font = ('Arial', 15), textvariable = First_Name)
    efname.pack()

    lblname = Label(f2, text = "LAST NAME", font = ('Arial', 15,  'bold italic'), fg = 'black', bg = '#b866fa')
    lblname.pack(padx = 125, pady = 15)
    elname = Entry(f2, width = 25, fg = 'black', bg = 'white', font = ('Arial', 15), textvariable = Last_Name)
    elname.pack()

    lbemail = Label(f2, text = "E-MAIL", font = ('Arial', 15,  'bold italic'), fg = 'black', bg = '#b866fa')
    lbemail.pack(padx = 125, pady = 15)
    eemail = Entry(f2, width = 25, fg = 'black', bg = 'white', font = ('Arial', 15), textvariable = email)
    eemail.pack()

    lbgender = Label(f2, text = "GENDER", font = ('Arial', 15,  'bold italic'), fg = 'black', bg = '#b866fa')
    lbgender.pack(padx = 125, pady = 15)
    sgender = Spinbox(f2, values=('male', 'female', 'others'), fg='black', bg='white', width=20, font='Arial 17', textvariable=gender)
    sgender.pack()
    #egender = Entry(f2, width = 30, fg = 'black', bg = 'white', font = ('Arial', 15), textvariable = gender)
    #egender.pack()

    lbcontact = Label(f2, text = "CONTACT NO", font = ('Arial', 15,  'bold italic'), fg = 'black', bg = '#b866fa')
    lbcontact.pack(padx = 125, pady = 15)
    econtact = Entry(f2, width = 25, fg = 'black', bg = 'white', font = ('Arial', 15), textvariable = contact_no)
    econtact.pack()

    bsubmit = Button(f2, text = "SUBMIT", width = 12, fg = 'white', bg = '#1e7031', font = ('Arial', 20, 'bold'), command = add_details)
    bsubmit.pack(pady = 35)

    #f3 content
    lbsearch = Label(f3, text = "Enter First Name to Search ", font = ('Arial', 20,  'bold italic'), fg = 'black', bg = '#7836ad',)
    lbsearch.pack(padx = 25, pady = 15)
    esearch = Entry(f3, width = 30, fg = 'black', bg = 'white', font = ('Arial', 15), textvariable = search)
    esearch.pack(pady = 15)

    bsearch = Button(f3, text = "Search", width = 15, fg = 'black', bg = '#c98fff', font = ('Arial', 20, 'bold'), command = search_record)
    bsearch.pack(pady = 15)

    bview = Button(f3, text = "View All", width = 15, fg = 'black', bg = '#c98fff', font = ('Arial', 20, 'bold'), command = display_details)
    bview.pack(pady = 15)

    breset = Button(f3, text = "Reset", width = 15, fg = 'black', bg = '#c98fff', font = ('Arial', 20, 'bold'), command = reset)
    breset.pack(pady = 15)

    bdelete = Button(f3, text = "Delete", width = 15, fg = 'black', bg = '#c98fff', font = ('Arial', 20, 'bold'), command = delete)
    bdelete.pack(pady = 15)

    bupdate = Button(f3, text = "Update", width = 15, fg = 'blackcd', bg = '#c98fff', font = ('Arial', 20, 'bold'), command = update)
    bupdate.pack(pady = 15)

    #f4 contents
    scrollbarx = Scrollbar(f4, orient=HORIZONTAL)
    scrollbary = Scrollbar(f4, orient=VERTICAL)
    #Creating tree for table contents
    tree = ttk.Treeview(f4, columns=('contact_id','fname','lname','sex','mail','phone_no'),height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    #Column Headings & its positioning
    tree.heading('contact_id', text="ID", anchor=CENTER)
    tree.heading('fname', text="First Name", anchor=CENTER)
    tree.heading('lname', text="Last Name", anchor=CENTER)
    tree.heading('sex', text="Gender", anchor=CENTER)
    tree.heading('mail', text="Email", anchor=CENTER)
    tree.heading('phone_no', text="Contact No", anchor=CENTER)

    #Assigning the width per column
    tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree.column('#1', stretch=NO, minwidth=0, width=80, anchor=CENTER)
    tree.column('#2', stretch=NO, minwidth=0, width=120, anchor=CENTER)
    tree.column('#3', stretch=NO, minwidth=0, width=120, anchor=CENTER)
    tree.column('#4', stretch=NO, minwidth=0, width=100, anchor=CENTER)
    tree.column('#5', stretch=NO, minwidth=0, width=180, anchor=CENTER)
    tree.column('#6', stretch=NO, minwidth=0, width=150, anchor=CENTER)
    tree.pack()

def add_details():

    connection()
    #getting form data and saving into new variables(the one on left side)
    First_Name1 = First_Name.get()
    Last_Name1 = Last_Name.get()
    gender1 = gender.get()
    email1 = email.get()
    contact_no1 = contact_no.get()

    #to check if fields are left empty
    if (First_Name1=='' or Last_Name1==''or gender1=='' or email1==''or contact_no1==''):
        tkMessageBox.showinfo("Message","Please fill the required details.")
    else:
        #Executing the query
        str = "insert into contacts (First_Name, Last_Name, gender, email, contact_no) values('%s','%s','%s','%s','%s')"
        args = (First_Name1, Last_Name1,gender1,email1,contact_no1)
        cursor.execute(str % args)

    #refresh the table data after inserting new values
        conn.commit()
        tkMessageBox.showinfo("Message","Contact Stored successfully")

    display_details()
    conn.close()

def display_details():

    connection()
    tree.delete(*tree.get_children())           #clear current data      
    cursor.execute("Select * from contacts")
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()

def OnDoubleClick(self):

    current_Item = tree.focus()             #to get the selected item from treeview         
    contents = (tree.item(current_Item))    #to save the current_item in contents
    selectedItem = contents['values']       #to store the value of the contents in selected_item

    #for displaying the details according to their resp fields
    ID.set(selectedItem[0])
    First_Name.set(selectedItem[1])
    Last_Name.set(selectedItem[2])
    gender.set(selectedItem[3])
    email.set(selectedItem[4])
    contact_no.set(selectedItem[5])

def delete():

    connection()
    #if any conatct detail is not selected
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            current_Item = tree.focus()
            contents = (tree.item(current_Item))
            selectedItem = contents['values']
            tree.delete(current_Item)
            cursor.execute("Delete from contacts where ID = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()

def reset():

    #clear current data from table
    tree.delete(*tree.get_children())

    #refresh table data
    display_details()

    #clear search text
    search.set("")
    First_Name.set("")
    Last_Name.set("")
    gender.set("")
    email.set("")
    contact_no.set("")

def update():

    connection()

    #getting form data
    First_Name1 = First_Name.get()
    Last_Name1 = Last_Name.get()
    gender1 = gender.get()
    email1 = email.get()
    contact_no1 = contact_no.get()

    #applying empty validation
    if (First_Name1=='' or Last_Name1==''or gender1=='' or email1==''or contact_no1==''):
        tkMessageBox.showinfo("Message","Please fill the required details.")
    else:

        #getting selected data
        current_Item = tree.focus()
        contents = (tree.item(current_Item))
        selectedItem = contents['values']

        #update query
        str = "update contacts set First_Name = '%s', Last_Name = '%s', gender = '%s', email = '%s', contact_no = '%s'  where ID = '%d'"
        args = (First_Name1, Last_Name1,gender1,email1,contact_no1, selectedItem[0])
        cursor.execute(str % args)
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")

        #reset form
        reset()

        #refresh table data
        display_details()
        conn.close()

def search_record():

    connection()
    search1 = search.get()      #seach1 stores the value of the search field(val of First Name)

    #checking search text is empty or not
    if search1 != "":

        #clearing current display data because after searching, only that data will be displayed which has been searched for
        tree.delete(*tree.get_children())

        #select query for updation with where clause
        str = "select * from contacts where First_Name = '%s' "
        args = (search1)
        cursor.execute(str % args)
        
        #fetch all matching records
        fetch = cursor.fetchall()
        
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

display_frames()
root.mainloop()