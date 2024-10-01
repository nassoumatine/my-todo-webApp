FILEPATH = "./todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(
            todos_arg)  # no need to return anything since we have nothing to
        # capture because the function only writes something to yhe file


if __name__ == "__main__":
    print("hello")
    print(get_todos())
