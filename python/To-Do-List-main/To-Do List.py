from tkinter import *
from tkinter import messagebox
import sqlite3 as sq

buttons="#f6edf6"
white="#ffffff"
operamauve="#b784a7"
languidlavender="#d6cadd"
antique="#915c83"
make="#856088"



def addTask():
    word = txt_input.get()
    if len(word) == 0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        cur.execute('insert into tasks values (?)', (word,))
        listUpdate()
        txt_input.delete(0, 'end')


def listUpdate():
    clearList()
    for i in task:
        lb_tasks.insert('end', i)


def delOne():
    try:
        val = lb_tasks.get(lb_tasks.curselection())
        if val in task:
            task.remove(val)
            listUpdate()
            cur.execute('delete from tasks where title = ?', (val,))
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')


def deleteAll():
    mb = messagebox.askyesno('Delete All', 'Are you sure?')
    if mb == True:
        while(len(task) != 0):
            task.pop()
        cur.execute('delete from tasks')
        listUpdate()


def clearList():
    lb_tasks.delete(0, 'end')


def retrieveDB():
    while(len(task) != 0):
        task.pop()
    for row in cur.execute('select title from tasks'):
        task.append(row[0])


# Driver Code
if __name__ == "__main__":
    # Create root window
    root = Tk()
    # Change the title
    root.title('To-Do List App')
    # Change the window size
    root.geometry("300x500")
    # no resize for both directions
    root.resizable(False, False)
    # create background display
    root.configure(bg=buttons)

    

    # Change icon
    photo = PhotoImage(file="icon.png")
    root.iconphoto(False, photo)

    # Establish connection with database
    conn = sq.connect('todo.db')
    cur = conn.cursor()

    # Create table if not already exists
    cur.execute('create table if not exists tasks (title text)')

    # Create an empty list
    task = []

    # set gui widgets
    lbl_title = Label(root, text='To-Do List', font=('Helvetica', 18,'bold'),bg=buttons ,fg=antique)
    lbl_task_show = Label(root, text='Enter Task Below :',
                          font=('Helvetica', 10),bg=buttons,fg=make)
    txt_input = Entry(root, width=30, bd="2", font="16",bg=languidlavender)
    lb_tasks = Listbox(root, width=28, height=12,
                       selectmode='SINGLE', relief=RIDGE, bd="4", font="14",bg=languidlavender)
    btn_add_task = Button(root, text='Add task', width=20,
                          command=addTask, relief=RIDGE,bg=operamauve,fg=white)
    btn_del_one = Button(root, text='Delete', width=20,
                         relief=RIDGE, command=delOne,bg= operamauve,fg=white)
    btn_del_all = Button(root, text='Delete all', width=20,
                         relief=RIDGE, command=deleteAll,bg=operamauve,fg=white)
    btn_exit = Button(root, text='Exit', width=20, relief=RIDGE, command=exit,bg=operamauve,fg=white)

    # function call
    retrieveDB()
    listUpdate()

    # Place geometry
    lbl_title.place(x=79, y=5)
    lbl_task_show.place(x=94, y=45)
    txt_input.place(x=10, y=80)
    btn_add_task.place(x=73, y=115)
    btn_del_one.place(x=73, y=145)
    btn_del_all.place(x=73, y=175)
    btn_exit.place(x=73, y=205)
    lb_tasks.place(x=17, y=240)

    # start mainloop
    root.mainloop()

    # Commit change
    conn.commit()
    # close connection
    cur.close()
