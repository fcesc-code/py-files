import openpyxl
import docx
import os

# constants 
cwd = os.getcwd()
input_directory = 'py-files\\data\\testdc'
input_file_name = 'fulltestdc.xlsx'
input_path = os.path.join(cwd, input_directory, input_file_name)
output_directory = 'py-files\\data\\resultsdc'
output_file_name = 'results.docx'
output_path = os.path.join(cwd, output_directory, output_file_name)


wb = openpyxl.load_workbook(input_path)
print('-> Excel source file opened successfully')
tabs = wb.sheetnames

letters = [ 'A', 'B', 'C', 'D', 'E', 'F']
doc = docx.Document(output_path)
print('-> Word target file opened successfully')
styles = doc.styles
i = 0

for tab in tabs:
  print(' > transfering worksheet ', tab)
  # doc.add_heading(tab, level=2)
  ws = wb[tab]
  max_rows = ws.max_row

  heading = doc.add_paragraph(tab.upper())
  heading.style = styles['Normal']
  table = doc.add_table(rows=0, cols=3)
  table.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
  previous_code = ''
  previous_title = ''

  for i in range(2, max_rows + 1):
    position_code = 'A' + str(i)
    code = str(ws[position_code].value).strip()
    if (code == 'None'): continue
    position_title = 'B' + str(i)
    title = str(ws[position_title].value).strip()
    position_text = 'F' + str(i)
    text = str(ws[position_text].value).strip()
    if (previous_code != code and code != 'None'): 
      previous_code = code
      code_changed = True
    else:
      code = previous_code
      code_changed = False
    if (previous_title != title and title != 'None'): 
      previous_title = title
    else:
      title = ''
    if (title != 'None' and text != 'None'):
      cells = table.add_row().cells
      if (code != 'None' and code_changed): 
        cells[0].text = code
      if (title != 'None'): 
        cells[1].text = title
      if (text != 'None'): 
        cells[2].text = text
      else:
        cells[2].text = ''
    i += 1

  par = doc.add_paragraph()
  run = par.add_run()
  run.add_break(docx.enum.text.WD_BREAK.PAGE)

#end
doc.save(output_path)
print('-> Word target file saved successfully')
print('-> Transfer completed')