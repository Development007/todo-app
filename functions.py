def get_todos(filepath="items.txt"):
    """Read text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="items.txt"):
    """Overwrite the text file and write in line
    according to data"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None


if __name__ == "__main__":
    print("Hello")
    print(get_todos())