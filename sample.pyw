from os import walk
from shutil import copyfile

import PySimpleGUI as sg


def open_file():

    """открываем файл и готовим список файлов для проверки"""
    with open(file_way, 'r') as file:
        for line in file:
            list_file.append(line[:-1])

        error = list_file

        return list_file, error


def otbor_file():
    """получаем список фалов"""
    sp_tr = walk(first_dir)
    for i in sp_tr:
        for j in i[1:]:
            for k in j:
                s1 = (i[0] + '\\' + k)
                if k[:k.find(' ')] in list_file and s1[-3:] == 'DXF':
                    '''Отбор фалов по номеру и расширению'''

                    '''Далее составление списка, и ввывод сообщения, что файл скопирован, составляется список не 
                    скопированных '''
                    list_spisok.append(s1)

                    copyfile(s1, final_dir + '\\' + k)
                    '''Процесс копирования'''
                    list_error.remove(k[:k.find(' ')])


list_file, list_error, list_spisok = [], [], []

sg.theme('DarkGrey1')
text_set = {"size": (20, 1), 'font': ("Arial", 12)}
but_set = {"size": (15, 2)}
column_to_be_centered = [
    [sg.OK('Выполнить', **but_set, button_color='green'), sg.Cancel('Выход', **but_set, button_color='red')]]

layout = [
    [sg.Text('Выбери список файлов', **text_set),
     sg.In(size=(25, 1), enable_events=True, key='-IN_FILE-'),
     sg.FileBrowse('Выбрать', **but_set, button_color='#4d4b49')],

    [sg.Text('Выбери папку для поиска', **text_set),
     sg.In(size=(25, 1), enable_events=True, key='-S_FOLDER-'),
     sg.FolderBrowse('Выбрать', **but_set, button_color='#4d4b49')],

    [sg.Text('Выбери папку для копий', **text_set),
     sg.In(size=(25, 1), enable_events=True, key='-COPY_FOLDER-'),
     sg.FolderBrowse('Выбрать', **but_set, button_color='#4d4b49')],

    [sg.Column(column_to_be_centered, justification='center')],
    [sg.Multiline(size=(70, 5), key='-OUT_PRINT-')]
]

window = sg.Window("Подбор файлов", layout)

while True:
    event, values = window.read()
    if event == 'Выход' or event == sg.WIN_CLOSED:

        break
    elif event == 'Выполнить':
        list_file, list_error = open_file()
        otbor_file()
        window.Element('-OUT_PRINT-').Update(
            f'Скопировано {len(list_spisok)} файлов. Этих файлов нет: {" ,".join(list_error)}')

    elif event == '-IN_FILE-':
        file_way = values['-IN_FILE-']

    elif event == '-S_FOLDER-':
        first_dir = values['-S_FOLDER-']

    elif event == '-COPY_FOLDER-':
        final_dir = values['-COPY_FOLDER-']

window.close()
