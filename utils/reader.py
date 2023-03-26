import os

def get_file_contents(file_name):
    file_contents = []

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "files", file_name)

    with open(file_path, "r") as file_reader:
        file_content = file_reader.read()

        for line in file_content.split("\n")[1:-1]:
            column = line.split(",")
            file_contents.append(column)

        file_reader.close()

    return file_contents
