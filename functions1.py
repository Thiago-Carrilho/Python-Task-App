def get_todos(filepath='todos1.txt'):
    """
    Read the text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos1.txt'):
    """Write the to-do items inside the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)