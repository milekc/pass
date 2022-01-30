from docxtpl import DocxTemplate


class Passport:
    def __init__(self):
        self.doc = DocxTemplate('temp.docx')
        self.context = {'name': 'Кантователь плит'}

    def run(self):
        self.doc.render(self.context)
        self.doc.save('pass.docx')


if __name__ == '__main__':

    pas = Passport()
    pas.run()
