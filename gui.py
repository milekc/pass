import PySimpleGUI as sg


class Interface:
    def __init__(self):
        self.theme = sg.theme('DarkGrey5')
        self.size = (480, 300)
        self.layout = [[sg.Text('Паспорт на кантователь', font='Monotype', size=(400, 1), justification='center',  )],#relief=sg.RELIEF_RAISED,
          [sg.Text('Ввести номер заявки', size=(15, 1)), sg.InputText('№ Заявки'), ],
            [sg.Text('Ввести Наименование', size=(15, 1)), sg.InputText('Кантователь катушек')],
          [sg.Text('Ввести тип и г/п', size=(15, 1)), sg.InputText('Кнт -2,5т')],
                       [sg.Text('_' * 80)],[sg.Text('Размер груза')],
                       [sg.InputText('Длина, мм', size=(20, 1)), sg.InputText('Ширина/Диаметр, мм', size=(20, 1)),
                        sg.InputText('Высота, мм', size=(20, 1))],
                       [sg.Text('Мощность', size=(12, 1)), sg.InputText('кВт', size=(14, 1)), sg.Text('Дата готовности', size=(12, 1)), sg.InputText('',size=(14, 1))],
          [sg.Text('_'  * 80)],
          [sg.Submit("Заполнить", size=(20,2), button_color='green', pad=(40,0)), sg.Submit("Выход", size=(20,2), button_color='red', pad=(5,0))]]
        self.window = sg.Window("Паспорт кантователя", self.layout, size = self.size)
        self.win_closed = sg.WIN_CLOSED


    # def run_interface(self):
    #     while True:
    #         self._check_event()
    #         self.values = self.window.read() # Смотрим по работе
    #
    # def _check_event(self):
    #     for event in self.window.read():
    #         if event == 'Выход' or event == sg.WIN_CLOSED:
    #             sys.exit()


# if __name__ == '__main__':
#     gui = Interface()
#     gui.run_interface()
#     sys.exit()





