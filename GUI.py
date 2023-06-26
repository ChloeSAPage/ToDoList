import Functions
import PySimpleGUI as sg

add_ = [[sg.Text("Type in a Todo")],
        sg.InputText(tooltip="Enter Todo", key = "new_todo"),
        sg.Button("Add")]

list_box = sg.Listbox(values=Functions.get_todos(), key = "todo_list", 
            enable_events=True,size = [44, 10])

edit_ = sg.Button("Edit")


window = sg.Window("My ToDo App",
                   layout=[add_,
                            [list_box, edit_]], font=("Helvetica", 12))

while True:
    button, user_input = window.read()
    print(button)
    print(user_input)
    match button:
        case "Add":
            todo_list = Functions.get_todos()
            new_todo = user_input["new_todo"] +"\n"
            todo_list.append(new_todo.capitalize())
            Functions.write_todos(todo_list)
            window["todo_list"].update(values=todo_list)
        case "Edit":
            todo_to_edit = user_input["todo_list"][0]
            new_todo = user_input["new_todo"] +"\n"
            todo_list = Functions.get_todos()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo.capitalize()
            Functions.write_todos(todo_list)
            window["todo_list"].update(values=todo_list)
        case "todo_list":
            window["new_todo"].update(value=user_input["todo_list"][0])
        case sg.WIN_CLOSED:
          break

window.close()