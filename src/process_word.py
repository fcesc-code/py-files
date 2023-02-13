import openpyxl
import docx
import os

# constants 
cwd = os.getcwd()
input_directory = 'py-files\\data\\testdc'
input_file_name = 'testdc.xlsx'
input_path = os.path.join(cwd, input_directory, input_file_name)
output_directory = 'py-files\\data\\resultsdc'
output_file_name = 'results.docx'
output_path = os.path.join(cwd, output_directory, output_file_name)

# constants

input_tab = 'HOJA1'
col_code = 1
col_previous = 2
col_new = 3
col_comment = 4
max_rows = 0
max_cols = 0
i = 0
j = 0

wb = openpyxl.load_workbook(input_path)
ws = wb[input_tab]

max_rows = ws.max_row
max_cols = ws.max_column

# while (i < max_rows):
#   ws.rows[i]
#   i += 1

# constants 2
letters = [ 'A', 'B', 'C', 'D', 'E', 'F']
doc = docx.Document(output_path)
table = doc.add_table(rows=0, cols=2)

for i in range(1, max_rows + 1):
  print('Iteration', i)
  cells = table.add_row().cells
  position_code = 'A' + str(i)
  position_text = 'C' + str(i)
  code = str(ws[position_code].value)
  text = str(ws[position_text].value)
  print('   >> insert: ', code, text)
  cells[0].text = code
  cells[1].text = text
  i += 1

table.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
#end
doc.save(output_path)
