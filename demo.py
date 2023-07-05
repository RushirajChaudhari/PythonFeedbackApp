from tkinter import * 
from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, Scrollbar, Listbox, END
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import * 

# dw- delete window 
# uw - update window 
user = {}



def signup():
    email = signup_email_entry.get()
    password = signup_password_entry.get()

    if email in user:
        messagebox.showerror("Signup", "Email already registered.")
    else:
        user[email] = password
        messagebox.showinfo("Signup", "Signup successful. You can now log in.")


def login():
    username = login_email_entry.get()
    password = login_password_entry.get()

    if username in user and user[username] == password:
        messagebox.showinfo("Login", "Login successful.")
        mw.withdraw()
        aw.deiconify()
    else:
        messagebox.showerror("Login", "Invalid username or password.")



# def f1():
#     mw.withdraw()
#     aw.deiconify()
    
def f2():
    uw.withdraw()
    mw.deiconify()
    

def f3():
    mw.withdraw()
    vw.deiconify()
    vw_st_data.delete(1.0 , END)
    con = None
    try:
        con = connect("rushi.db")
        cursor = con.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info = info + " id: " + str(d[0]) + " Name: " + str(d[1]) + "\n"
        vw_st_data.insert(INSERT , info)
    except Exception as e:
        showerror("Issue" , str(e))
    finally:
        if con is not None:
            con.close()
            
            


def f4():
    vw.withdraw()
    mw.deiconify()
    
def f5():
    con = None
    try:
        con = connect("rushi.db")
        cursor = con.cursor()
        sql = "insert into student values('%d' , '%s')"
        
        try:
            rno = int(aw_ent_empid.get())
        except ValueError:
            showerror("Issue" , "empid should be integers only ")
            return 
        if rno< 1:
            showerror("Issue" , "empid should be min 1")
            return
        
        name = aw_ent_name.get()
        if not name.isalpha():
            showerror("Issue" , "name should contain alphabets only ")
            return
        
        if len(name) < 2:
            showerror("Issue" , "name should contain min 2 letters ")
            return

        cursor.execute(sql % (rno,name))
        con.commit()
        showinfo("Success " , "record created ")
    except Exception as e:
        showerror("Issue" , str(e))
        con.rollback()
    finally:
        if con is not None:
            con.close()
        aw_ent_empid.delete(0 , END)
        aw_ent_name.delete(0 , END)
        aw_ent_empid.focus()

def f8():
    dw.withdraw()
    mw.deiconify()
    
def f9():
    mw.withdraw()
    dw.deiconify()
    
def f6():
    mw.withdraw()
    dw.deiconify()
    con = None
try:
    con = connect("rushi.db")
    cursor = con.cursor()
    sql = "delete from student where rno = %d "
    rno = int(uw_ent_id.get()) 
    cursor.execute(sql % (rno))
    if cursor.rowcount == 1:
        con.commit()
        showinfo("record deleted successfully ")
    else:
        showinfo("record doesnot exists ")
except Exception as e:
    con.rollback()
    # showerror("issue" , e )
finally:
    if con is not None:
       con.close()
    #    showinfo("Success " , "record deleted")

        
    
def f7():
    mw.withdraw()
    uw.deiconify()


    
def f10():
    con = None
    mw.withdraw()
    uw.deiconify()
    try:
        con = connect("rushi.db")
        cursor = con.cursor()
        sql = "UPDATE student SET name = '%s' WHERE rno='%d'"
        try:
            empid = int(uw_ent_id.get())
        except ValueError:
            showerror("Issue" , "empid should be integers only ")
            return 
        if empid < 1:
            showerror("Issue" , "empid should be min 1")
            return
        
        name = uw_ent_name.get()
        if not name.isalpha():
            showerror("Issue" , "name should contain alphabets only ")
            return
        
        if len(name) < 2:
            showerror("Issue" , "name should contain min 2 letters ")
            return

        cursor.execute(sql % (empid,name))
        con.commit()
        showinfo("Success " , "record created ")
    except Exception as e:
        showerror("Issue" , str(e))
        con.rollback()
    finally:
        if con is not None:
            con.close()
        uw_lab_id.delete(0 , END)
        uw_lab_name.delete(0 , END)
        uw_lab_id.focus()

# def f10():
#     con = None
#     mw.withdraw()
#     uw.deiconify()
#     con = connect("rushi.db")
#     cursor = con.cursor()
#     sql = "UPDATE student SET name = '%s' WHERE rno='%d' "
#     empid = int(uw_ent_id.get())
#     name = uw_ent_name.get()
#     cursor.execute(sql % (name , rno))
#     con.commit()
#     showinfo("Success " , "Record created")
        

def f11():
    mw.withdraw()
    su.deiconify()

def f12():
    mw.withdraw()
    lu.deiconify()

def f13():
    mw.withdraw()
    al.deiconify()
    
def f14():
    su.withdraw()
    mw.deiconify()
    
def f15():
    lu.withdraw()
    mw.deiconify()
    
def f16():
    al.withdraw()
    mw.deiconify()
    
def f17():
    uw.withdraw()
    mw.deiconify()
    
def f18():
    aw.withdraw()
    mw.deiconify()

mw = Tk()
mw.title("Feedback By Rushi")
mw.geometry("1000x1200+100+100")
mw.configure(bg = "lightblue")
f = ("Times New Roman" , 20 , "bold")
f1 = ("Times New Roman" , 20)
f2 = ("Times New Roman" , 30 , "bold" , 'underline')

# # Add image file
# bg = PhotoImage(file = "background.png.png")
  
# # Show image using label
# label1 = Label( mw, image = bg)
# label1.place(x = 0, y = 0)

mw_lab_main = Label(mw , text= "Feeback App By Rushiraj Chaudhari" , font=f2 , bg = "lightblue" ,fg="black")
mw_btn_signup = Button(mw , text="SignUp as User" ,font=f1,  border=12 , width=13,fg="black" ,bg="lightgrey" , command=f11)
mw_btn_login = Button(mw , text="Login as User" ,font=f1,  border=12  , width=13,fg="black" ,bg="lightgrey",  command=f12)
mw_btn_admin = Button(mw , text="Login as Admin" ,  border=12 ,font=f1 , width=13,fg="black" ,bg="lightgrey", command=f13)
mw_btn_update = Button(mw , text="Update" ,  border=12  , width=13 , command=f10 ,fg="black" ,bg="lightgrey", font=f1)
mw_btn_delete = Button(mw , text="Delete" ,  border=12  , width=13 , command=f6,fg="black" ,bg="lightgrey", font=f1)

# # SIGNUP SECTION 
# signup_label = Label(mw, text="SignUp: ", font=f, fg="darkblue",width=35 , bg="grey")
# signup_label.pack()

# signup_email_label = Label(mw , text="SignUp", font=f1 )
# signup_email_label.pack(pady=3)

# signup_email_entry = Entry(mw , font=f1 )
# signup_email_entry.pack(pady=3)

# signup_password_label = Label(mw, text="Password:", font=f1)
# signup_password_label.pack(pady=3)

# signup_password_entry = Entry(mw, show="*", font=f1)
# signup_password_entry.pack(pady=3)

# signup_button = Button(mw, text="Signup" , command=signup, font=f1 ,width=10 , height=1)
# signup_button.pack(pady=8)

#                 # LOGIN SECTION
                
# login_label = Label(mw, text="Login:" , font=f, fg="darkblue",width=35 , bg="grey")
# login_label.pack()

# login_email_label = Label(mw, text="Username:" , font=f1)
# login_email_label.pack(pady=5)

# login_email_entry = Entry(mw , font=f1)
# login_email_entry.pack(pady=3)

# login_password_label = Label(mw, text="Password:", font=f1)
# login_password_label.pack(pady=3)

# login_password_entry = Entry(mw, show="*", font=f1)
# login_password_entry.pack(pady=4)

# login_button = Button(mw, text="Login" , command=login, font=f1,width=10 , height=1)
# login_button.pack(pady=8)


# # -------------------------ADMIN LOGIN-------------------
# admin_label = Label(mw, text="Admin Login:", font=f , fg="darkblue" ,width=35 , bg="grey")
# admin_label.pack()

# login_admin_label = Label(mw, text="Username", font=f1)
# login_admin_label.pack(pady=5)

# login_admin_entry = Entry(mw , font=f1)
# login_admin_entry.pack(pady=3)

# admin_password_label = Label(mw, text="Password:", font=f1)
# admin_password_label.pack(pady=3)

# admin_password_entry = Entry(mw, show="*", font=f1)
# admin_password_entry.pack(pady=3)

# admin_login_button = Button(mw, text="Admin Login" , command=f3, font=f1)
# admin_login_button.pack(pady=8)





mw_lab_main.pack(pady=80)
mw_btn_signup.pack(pady=10)
mw_btn_login.pack(pady=10)
mw_btn_admin.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)

# Add Window Section 

aw = Toplevel(mw)
aw.title("Add Feedback")
aw.geometry("700x600+50+50")
# aw.configure(bg="lightblue")

aw_lab_empid = Label(aw , text="enter Id: " , font=f)
aw_ent_empid = Entry(aw , font=f)
aw_lab_name = Label(aw , text="Enter Feedback: " , font=f)
aw_ent_name = Entry(aw , font=f )
aw_btn_save = Button(aw ,  text="Save" , font=f , width=7  ,command=f5)
aw_btn_back = Button(aw , text="LogOut" , font=f , width=7  , command=f18)

aw_lab_empid.pack(pady=10)
aw_ent_empid.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()

# delete window section 
dw = Toplevel(mw)
dw.title("Delete Feedback")
dw.geometry("1000x900+50+50")
dw.configure(bg="lightblue")

dw_lab_id = Label(dw , text="Enter id" , font=f)
dw_ent_id = Entry(dw , font=f)
dw_btn_save = Button(dw , text="Save" , font=f , width=7 , command=f6 )
dw_btn_back = Button(dw , text="Back" , font=f , width=7 , command=f8 )

dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()
#   ----------------------xxxx---------------------

# Update Window
uw = Toplevel(mw)
uw.title("Update Feedback")
uw.geometry("1000x900+50+50")
uw.configure(bg="lightblue")

uw_lab_id = Label(uw , text="Enter id" , font=f)
uw_ent_id = Entry(uw , font=f)
uw_lab_name = Label(uw , text="Enter name: " , font=f )
uw_ent_name = Entry(uw , font=f)
uw_btn_save = Button(uw , text="Save" , font=f , width=7 , command=f10 )
uw_btn_back = Button(uw , text="Back" , font=f , width=7 , command=f17 )

uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
# uw_lab_salary.pack(pady=10)
# uw_ent_salary.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
uw.withdraw()


# SIGNUP AS USER 
# su->signup user 
su = Toplevel(mw)
su.title("SignUp as user")
su.geometry("500x600+50+50")
su.configure(bg="lightblue")


# su_lab_id = Label(su , text="Enter username: " , font=f)
# su_ent_id = Entry(su , font=f)
# su_lab_name = Label(su , text="Enter password: " , font=f )
# su_ent_name = Entry(su , font=f)
# su_btn_save = Button(su , text="SignUp" , font=f , width=7, command=signup)
# su_btn_back = Button(su , text="Back" , font=f , width=7 , command=f14)

# su_lab_id.pack(pady=10)
# su_ent_id.pack(pady=10)
# su_lab_name.pack(pady=10)
# su_ent_name.pack(pady=10)
# su_btn_save.pack(pady=10)
# su_btn_back.pack(pady=10)
# su.withdraw()

# SIGNUP SECTION 
# signup_label = Label(su, text="SignUp: ", font=f, fg="darkblue",width=35 , bg="grey")
# signup_label.pack()

signup_email_label = Label(su , text="SignUp", font=f1 )
signup_email_label.pack(pady=3)

signup_email_entry = Entry(su , font=f1 )
signup_email_entry.pack(pady=3)

signup_password_label = Label(su, text="Password:", font=f1)
signup_password_label.pack(pady=3)

signup_password_entry = Entry(su, show="*", font=f1)
signup_password_entry.pack(pady=3)

signup_button = Button(su, text="Signup" , command=signup, font=f1 ,width=10 , height=1)
signup_button.pack(pady=8)
signup_button = Button(su , text="Back" , font=f , width=7 , command=f14)
signup_button.pack()
su.withdraw()

# LOGIN AS USER 
# lu->login user 
lu = Toplevel(mw)
lu.title("Login as user")
lu.geometry("500x600+50+50")
lu.configure(bg="lightblue")


# lu_lab_id = Label(lu , text="Enter username: " , font=f)
# lu_ent_id = Entry(lu , font=f)
# lu_lab_name = Label(lu , text="Enter password: " , font=f )
# lu_ent_name = Entry(lu , font=f)
# lu_btn_save = Button(lu , text="Login" , font=f , width=7 , command=login)
# lu_btn_back = Button(lu , text="Back" , font=f , width=7 , command=f15)

# lu_lab_id.pack(pady=10)
# lu_ent_id.pack(pady=10)
# lu_lab_name.pack(pady=10)
# lu_ent_name.pack(pady=10)
# lu_btn_save.pack(pady=10)
# lu_btn_back.pack(pady=10)
# lu.withdraw()


#                 # LOGIN SECTION
                
# login_label = Label(lu, text="Login:" , font=f, fg="darkblue",width=35 , bg="grey")
# login_label.pack()

login_email_label = Label(lu, text="email:" , font=f1)
login_email_label.pack(pady=5)

login_email_entry = Entry(lu , font=f1)
login_email_entry.pack(pady=3)

login_password_label = Label(lu, text="Password:", font=f1)
login_password_label.pack(pady=3)

login_password_entry = Entry(lu, show="*", font=f1)
login_password_entry.pack(pady=4)

login_button = Button(lu, text="Login" , command=login, font=f1,width=10 , height=1)
login_button.pack(pady=8)
lu_btn_back = Button(lu , text="Back" , font=f , width=7 , command=f15)
lu_btn_back.pack()
lu.withdraw()



# LOGIN AS Admin 
# al->admin login  
al = Toplevel(mw)
al.title("Login as Admin")
al.geometry("500x600+50+50")
al.configure(bg="lightblue")


# al_lab_id = Label(al , text="Enter username: " , font=f)
# al_ent_id = Entry(al , font=f)
# al_lab_name = Label(al , text="Enter password: " , font=f )
# al_ent_name = Entry(al , font=f)
# al_btn_save = Button(al , text="Admin Login" , font=f ,command=f3)
# al_btn_back = Button(al , text="Back" , font=f ,command=f2)

# al_lab_id.pack(pady=10)
# al_ent_id.pack(pady=10)
# al_lab_name.pack(pady=10)
# al_ent_name.pack(pady=10)
# al_btn_save.pack(pady=10)
# al_btn_back.pack(pady=10)
# al.withdraw()


# -------------------------ADMIN LOGIN-------------------
# admin_label = Label(mw, text="Admin Login:", font=f , fg="darkblue" ,width=35 , bg="grey")
# admin_label.pack()

login_admin_label = Label(al, text="email", font=f1)
login_admin_label.pack(pady=5)

login_admin_entry = Entry(al , font=f1)
login_admin_entry.pack(pady=3)

admin_password_label = Label(al, text="Password:", font=f1)
admin_password_label.pack(pady=3)

admin_password_entry = Entry(al, show="*", font=f1)
admin_password_entry.pack(pady=3)

admin_login_button = Button(al, text="Admin Login" , command=f3, font=f1)
admin_login_button.pack(pady=8)
al_btn_back = Button(al , text="Back" , font=f , width=7 , command=f16)
al_btn_back.pack()
al.withdraw()


# View Window Section 
vw = Toplevel(mw)
vw.title("view Student")
vw.geometry("700x600+50+50")
vw.configure(bg = "lightblue")

vw_st_data = ScrolledText(vw , font=f , width=30 , height=8)
vw_btn_back = Button(vw , text="Back" , font=f , command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

mw.mainloop()



