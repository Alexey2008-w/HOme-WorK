import os



def create_file_list(folder):
    file_list = os.listdir(folder)
    join_file_list = []
    for file in file_list:
        with open(folder + "/" + file) as _temp_file:
            join_file_list.append([file, 0, []])
            for line in _temp_file:
                join_file_list[-1][2].append(line.strip())
                join_file_list[-1][1] += 1

    return sorted(join_file_list, key=lambda x: x[1], reverse=False)



def create_join_file(folder, filename):
    with open(filename + '.txt', 'w+') as join_file:
        join_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            join_file.write(f'Назввание файла: {file[0]}\n')
            join_file.write(f'Количество строк: {file[1]}\n')
            for string in file[2]:
                join_file.write(string + '\n')
            join_file.write('\n')
    return print('Файл создан')


create_join_file('txt', 'join_file')