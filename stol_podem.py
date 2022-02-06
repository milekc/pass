import PySimpleGUI as sg
from docxtpl import DocxTemplate

doc = DocxTemplate('temp_stol.doc')
# Интерфейс
sg.theme('DarkGrey5')
size = (480, 300)
layout = [[sg.Text('Паспорт на стол подъема', size=(400, 1), justification='center', )],  # relief=sg.RELIEF_RAISED,
          [sg.Text('Ввести номер заявки', size=(15, 1), ), sg.InputText('№ Заявки', key='-order-')],
          [sg.Text('Ввести Наименование', size=(15, 1)),
           sg.InputText('Кантователь катушек', enable_events=True, key='-name-')],
          [sg.Text('Ввести тип и г/п', size=(15, 1)), sg.InputText('Кнт -2,5т', key='-type-')],
          [sg.Text('_' * 80)], [sg.Text('Размер груза')],
          [sg.InputText('Длина, мм', size=(20, 1), key='-length-'),
           sg.InputText('Ширина/Диаметр, мм', size=(20, 1), key='-height-'),
           sg.InputText('Высота, мм', size=(20, 1), key='-width-')],
          [sg.Text('Мощность', size=(12, 1)), sg.InputText('кВт', size=(14, 1), key='-power-'),
           sg.Text('Дата готовности', size=(12, 1)), sg.InputText('', size=(14, 1), key='-date-')],
          [sg.Text('_' * 80)],
          [sg.OK('Заполнить', size=(20, 2), button_color='green', pad=(40, 0)),
           sg.Cancel("Выход", size=(20, 2), button_color='red', pad=(5, 0))]]
window = sg.Window("Паспорт для стола подъемного", layout, size=size)

# работа приложения и отработка кнопок
while True:
    event, values = window.read()
    year = values['-date-'].split('.')
    if event == 'Выход' or event == sg.WIN_CLOSED:
        break
    elif event == 'Заполнить' or event == sg.OK:
        context = {'name': values['-name-'],
                   'length': values['-length-'],
                   'height': values['-height-'],
                   'year': year[-1],
                   'width': values['-width-'],
                   'date': values['-date-'],
                   'order': values['-order-'],
                   'tip': values['-type-'],
                   'power': values['-power-']}
        file_name = context['order'] + ' ' + context['name']
        doc.render(context)
        doc.save(f'{file_name}.docx')
        break

window.close()
