import functions
# Used instead of tkinter because PySimpleGUI is better
import PySimpleGUI as sg
import time

sg.theme('DarkPurple4')
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=(50,50), image_source='add.png', mouseover_colors='LightBlue2',
                       tooltip='Add Todo', key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(size=2, image_source='edit.png', mouseover_colors='LightBlue2',
                        tooltip='Select to edit Todos', key="Edit")
complete_button = sg.Button(size=2, image_source='complete.png', mouseover_colors='LightBLue2',tooltip='Select Completed Item', key="Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do-App',
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup_error("Select a value to Edit", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup_error("Select an Completed item", font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
