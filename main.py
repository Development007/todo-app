# todos = []
import functions
import time

now_time = time.strftime("%b %d, %Y %H:%M:%S")
print(now_time)
while True:
    # Get input from the user for todos and strip space chars from it
    user_action = input("Type add, show, complete, or exit: ")
    user_action = user_action.strip()

    # Check if user action input meet the following prefixed syntax
    if user_action.startswith("add"):
        todo = user_action[4: ]
        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(filepath="items.txt", todos_arg=todos)

    elif user_action.startswith("show"):
        # using with function because it don't need to close the file
        todos = functions.get_todos()
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter new todo:  ")
            todos[number] = new_todo + '\n'

            functions.write_todos(filepath="items.txt",todos_arg= todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(filepath="items.txt", todos_arg=todos)

            message = f"Todo {todo_to_remove} was removed"
            print(message)
        except IndexError:
            print("Not valid index")
            continue
        except ValueError:
            print("Digits Only")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        # - can be used instead of a word. I will better
        print("Value does not match")


print("Bye!")