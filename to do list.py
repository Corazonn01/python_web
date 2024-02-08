# python_web
from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title('To Do list')
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open('tasks.txt', 'a') as file:
            file.write(f'\n{task}')
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasks.txt', 'w') as fil:
            for task in task_list:
                fil.write(task+'\n')

        listbox.delete(ANCHOR)





def openTaskFile():
    try:
        global task_list
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('tasks.txt', 'w')
        file.close()


# icon for a list
image_icon = PhotoImage(file='task.png')
root.iconphoto(False, image_icon)

TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

dock_image = PhotoImage(file='dock.png')
Label(root, image=dock_image, bg='#32405b').place(x=30, y=25)

note_img = PhotoImage('task.png')
Label(root, image=note_img, bg='#32405b').place(x=340, y=25)

heading = Label(root, text="All tasks", font='Times 20 bold', fg='white', bg='#32405b')
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font='Times 20', bd=0)
task_entry.place(x=10, y=7)  # that is for typing some text
task_entry.focus()

button = Button(frame, text="Add task", font='Times 20', width=6, bg='#5a85ff', fg='#fff', bd=0, command=addTask)
button.place(x=300, y=-1)

# crating list box
frame1 = Frame(root, bd=3, width=700, height=280, bg='#32405b')
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('Times', 12), width=40, height=16, bg='#32405b', fg='white', cursor='hand2',
                  selectbackground='#5a95ff')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
# deletion
delete_icon = PhotoImage(file='delete.png')
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
