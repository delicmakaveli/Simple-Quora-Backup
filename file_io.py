import os


# Creates a directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
    else:
        pass


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Within a directory, create a reading_list text file
def create_data_file(project_name, content):
    # Creates a path (reading_list)
    reading_list = project_name + '/reading_list.txt'
    if not os.path.isfile(reading_list):
        # If there is no file - write/create a file with the content in it
        write_file(reading_list, content)


# Within a directory, create an answers text file
def create_data_file1(project_name, content):
    # Creates a path (reading_list)
    my_answers = project_name + '/my_answers.txt'
    if not os.path.isfile(my_answers):
        # If there is no file - write/create a file with the content in it
        write_file(my_answers, content)
    else:
        delete_file_content(my_answers)


# Add data to an existing file
def append_to_file(path, data):
    # with ab and a - opens the file and as soon as I exit the block(execute everything in it) it automatically closes
    with open(path, 'ab') as file:
        file.write(data)

    with open(path, 'a') as f1:
        f1.write('\n' + '\n')


# Delete the contents of a file
def delete_file_content(path):
    with open(path, 'w'):
        # Does nothing/writes nothing, creates a new file with the same name/overwrites
        pass




