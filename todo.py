# a simple to do app from the CLI
todo_list = []
def main():
    f = open("todo.txt", "x")
    print("What would you like to do? " +
          "Press 1 to view list" + 
          "Press 2 to add to list" +
          "Press 3 to delete from list")
    response = int(input())
    if response == 1:
        view_list()
    elif response == 2:
        add_task()
    elif response == 3:
        delete_task()
    else:
        print("Please enter a valid response")
        #main()

def view_list():
    print(todo_list)

def add_task():
    print("Please add a task: ")
    task = input()
    todo_list.append(task)
    print("Task added. Please view To-Do list below:")
    print(todo_list)

def delete_task():
    print(view_list)
    print("The List has tasks starting from 0.\n" +
           "Please enter the integer of the task you wish to delete: ")
    delete = input()
    todo_list.remove(delete)

main()