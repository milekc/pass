import sys

from docxtpl import DocxTemplate

from gui import Interface
from key import context


class Passport:
    def __init__(self):
        self.doc = DocxTemplate('temp.docx')
        self.context = context
        self.interface = Interface()



    def run(self):
        self.doc.render(self.context)
        self.doc.save('pass.docx')

    def run_interface(self):
        while True:
            self._check_event()
            self.values = self.interface.window.read()  # Смотрим по работе


    def _check_event(self):
        for event in self.interface.window.read():
            if event == 'Выход' or event == self.interface.win_closed:
                sys.exit()

            elif event == 'Заполнить':
                self.run()
                sys.exit()


if __name__ == '__main__':
    pas = Passport()
    pas.run_interface()
    sys.exit()
