import PySimpleGUI as sg
from docxtpl import DocxTemplate

def ts():
    g = float(values['-load_capacity-'].replace(' ', '')) / 1000
    h = (float(values['-height-'].replace(' ', '')) - float(values['-height_down-'].replace(' ', '')))/1000
    l = float(values['-length-'].replace(' ', ''))/1000
    w = float(values['-width-'].replace(' ', ''))/1000
    dh = float(values['-height_down-'].replace(' ', ''))/1000
    return (f'{g}-{h}-{l}-{w}-{dh}')

doc = DocxTemplate('temp_stol.docx')
# Интерфейс
sg.theme('DarkGrey5')
size = (480, 420)
layout = [[sg.Text('Паспорт на стол подъема', size=(400, 1), justification='center', )],  # relief=sg.RELIEF_RAISED,
          [sg.Text('Ввести номер заявки', size=(15, 1), ), sg.InputText('№ Заявки', key='-order-')],
          [sg.Text('Номер акта - счета', size=(15, 1), ),
           sg.InputText('Акт №', size=(14, 1), key='-payment-'),
           sg.Text('Дата готовности', size=(12, 1)), sg.InputText('', size=(13, 1), key='-date-')],

          [sg.Text('_' * 80)],
          [sg.Text('Грузоподъемность', size=(15, 1)), sg.InputText('1 000', key='-load_capacity-')],
          [sg.Text('Тип платформы', size=(15, 1)), sg.InputText('плоская', key='-type_pl-')],
          [sg.Text('Размер платформы')],
          [sg.InputText('Длина, мм', size=(20, 1), key='-length-'),
           sg.InputText('Ширина, мм', size=(20, 1), key='-width-')],
          [sg.Text('Высота стола')],
          [sg.InputText('Высота подъема, мм', size=(20, 1), key='-height-'),
           sg.InputText('Высота в сложенном виде, мм', size=(20, 1), key='-height_down-')],
          [sg.Text('Мощность', size=(12, 1)), sg.InputText('кВт', size=(14, 1), key='-power-'),
           ],
          [sg.Text('_' * 80)],
          [sg.OK('Заполнить', size=(20, 2), button_color='green', pad=(40, 0)),
           sg.Cancel("Выход", size=(20, 2), button_color='red', pad=(5, 0))]]
window = sg.Window("Паспорт для стола подъемного", layout, size=size)

# работа приложения и отработка кнопок
while True:


    event, values = window.read()
    type_s = ts()
    if event == 'Выход' or event == sg.WIN_CLOSED:
        break
    elif event == 'Заполнить' or event == sg.OK:
        context = {'load_capacity': values['-load_capacity-'],
                   'height': values['-height-'],
                   'width': values['-width-'],
                   'payment': values['-payment-'],
                   'type': type_s,
                   'order': values['-order-'],
                   'height_down': values['-height_down-'],
                   'length': values['-length-'],
                   'power': values['-power-'],
                   'data': values['-date-'],
                   'type_pl': values['-type_pl-']}
        file_name = context['order'] + ' Стол подъема'
        doc.render(context)
        doc.save(f'{file_name}.docx')
        break

window.close()
