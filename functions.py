#function def
def get_todos(filepath="todos.txt"):
    """ Reads a text file and return the List of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todos.txt"):
    """ Writes to-do items List in the
        text file
        """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)