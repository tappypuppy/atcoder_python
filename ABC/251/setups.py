import os

cwd = os.getcwd()

levels = ['A','B','C','D','E','F']


for folder_name in levels:
    folder_path = os.path.join(cwd,folder_name)
    os.makedirs(folder_path, exist_ok = True)

    f_list = [folder_name + '.py', 'command.txt', 'input.txt', 'knowledge.txt']

    for file_name in f_list:
        file_path = os.path.join(folder_path, file_name)

        f = open(file_path, 'w')
        
        if file_name == 'command.txt':
            text = 'python ' + folder_name + '.py < input.txt'
            f.write(text)
        else:
            f.write('')
        
        f.close()

