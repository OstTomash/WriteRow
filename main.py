import os


def add_content_to_file(file_name, content):
    abs_path = os.getcwd();
    file_path = os.path.join(abs_path, 'files', file_name)
    result = ''

    try:
        f = open(file_path, 'a+')
    except FileNotFoundError:
        return 'File Not Found'
    else:
        f.write(f'{content}\n')
        f.close()

    return result


custom_input = input("Enter any phrase: ")
add_content_to_file('example.txt', custom_input)
