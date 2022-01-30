from docxtpl import DocxTemplate
from key import context


class Passport:
    def __init__(self):
        self.doc = DocxTemplate('temp.docx')
        self.context = context

    def run(self):
        self.doc.render(self.context)
        self.doc.save('pass.docx')


if __name__ == '__main__':

    pas = Passport()
    pas.run()
