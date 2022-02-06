from docxtpl import DocxTemplate

context_dict = {}
tpl=DocxTemplate('temp_stol.docx')
tpl.render(context_dict)
set_of_variables = tpl.get_undeclared_template_variables()

print(set_of_variables)