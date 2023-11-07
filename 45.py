#https://www.youtube.com/watch?v=553lAJbfZMM&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=66
#TODOLISTMANAGEMENT
# add(what,when,importnaace low mid high),view(view all, view priority),remove,edit


todo = [["wassen","10:00","hoog"],["douchen","12:00","laag"]]

def prettyPrint():
    for item in todo:
        print("-".join(item))

def sortPrio():
    prio = input("laag, mid or hoog priority?").strip().lower()
    for item in todo:
        if item[2] == prio:
            print(", ".join(item))

    
    print()
   
def add():
    nog = ("yes").lower()
    while nog == "yes" or nog == "y":
        what = input("what?: ")
        when = input("When?: ")
        importance = input("Importance?: ").strip().lower()
        row = what , when, importance
        todo.append(row)
        print(todo)
        nog = input("Continue? Yes/No Y/N: ").strip().lower()

def view():
    print("")
    view = "all"
    view = input("""1. View all
2. Sort priority
: """)
    print()
    if view == "1":
        prettyPrint()
    elif view == "2":
        sortPrio()

def remove():
    remove = input("which task to remove?")
    for item in todo:
        if remove in item:
            todo.remove(item)
            print("item removed successfully")

def edit():
    edit_task = input("which task to edit?")
    for task in todo:
        if edit_task in task[0]:
            print(f"Editing task: {task}")
            edit_choice = input("What would you like to edit (task, hour, priority)? ")
            if edit_choice == "task":
                new_task = input("Enter the new task: ")
                task[0] = new_task
            elif edit_choice == "hour":
                new_hour = input("Enter the new hour: ")
                task[1] = new_hour
            elif edit_choice == "priority":
                new_priority = input("Enter the new priority: ")
                task[2] = new_priority
            else:
                print("task hour or prio")
            print("Task updated successfully.")
            print("")
            break
    else:
        print(f"Task '{edit_task}' not found in the to-do list.")
    

#mainloop

menu = "q".lower
while menu != "q": 
        print("---TODO LIST---")
        menu = input("""
1. add
2. view
3. remove
4. edit
5. quit

: """)

        menu = menu.strip().lower()

        if menu == "1" or menu == "add":
            add()
        elif menu == "2" or menu == "view":
            view()
        elif menu == "3" or menu == "remove":
            remove()
        elif menu == "4" or menu == "edit":
            edit()
        elif menu == "quit" or menu =="5":
            break
