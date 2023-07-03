import functions
import PySimpleGUI as sg

add_ = [[sg.Text("Type in a Todo")],
        sg.InputText(tooltip="Enter Todo", key = "todo"),
        sg.Button("Add")]

list_box = sg.Listbox(values=functions.get_todos(), key = "todo_list", 
            enable_events=True,size = [44, 10])

edit_ = sg.Button("Edit")

complete_ = sg.Button("Complete")

exit_ = [sg.Button("Exit")]


window = sg.Window("My ToDo App",
                   layout=[add_,
                    [list_box, edit_ , complete_], exit_], 
                    font=("Comic Sans", 12))

while True:
    button, values = window.read()
    print(button)
    print(values)
    match button:
        case "Add":
            todo_list = functions.get_todos()
            new_todo = values["todo"] +"\n"
            todo_list.append(new_todo.capitalize())
            functions.write_todos(todo_list)
            window["todo_list"].update(values=todo_list)
        case "Edit":
            todo_to_edit = values["todo_list"][0]
            new_todo = values["todo"] +"\n"
            todo_list = functions.get_todos()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo.capitalize()
            functions.write_todos(todo_list)
            window["todo_list"].update(values=todo_list)
        case "Complete":
            todo_to_complete = values["todo_list"][0]
            todo_list = functions.get_todos()
            todo_list.remove(todo_to_complete)
            functions.write_todos(todo_list)
            window["todo_list"].update(values=todo_list)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todo_list":
            window["todo"].update(value=values["todo_list"][0])
        case sg.WIN_CLOSED:
          break

window.close()