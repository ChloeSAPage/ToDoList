import Functions
import PySimpleGUI as sg

label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

window = sg.Window("My ToDo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()