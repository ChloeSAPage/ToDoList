def get_todos(filepath="ToDoList.txt"):
     """Read the file and returns the list of ToDos """
     with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
        return todo_list_local

def write_todos(todo_list_arg, filepath="ToDoList.txt"):
    """Writes the ToDoList in the text file"""
    with open(filepath, "w") as file:
        file.writelines(todo_list_arg)

def show_todo(todo_list):
    """Shows the ToDoList from the file then numbers
       and capitalises each ToDo"""
    print("Here is the List of ToDos:")
    for index, item in enumerate(todo_list):
            item =  item.strip("\n")
            print(f"{(index)+1}. {item.capitalize()}")


def yes_no(action, number, todo_list):
    """Confirms if the user performed the right action"""
    print(f"do you wish to {action} {todo_list[number].strip()}?")
    yes_no_input = input()
    yes_no_input = yes_no_input.strip().lower()
    return yes_no_input

print("Hello")