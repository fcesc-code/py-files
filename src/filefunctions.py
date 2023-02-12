import os
import csv
import classes as t
import constants as c

cwd = os.getcwd()
csvDelimiter = ';'
input_file_name = 'rome_data.csv'
input_directory = 'py-files\\data\\confidential'
input_path = os.path.join(cwd, input_directory, input_file_name)
output_totals_file_name = 'rome_totals.csv'
output_totals_directory = 'py-files\\data\\results'
output_totals_path = os.path.join(cwd, output_totals_directory, output_totals_file_name)


class DataHandler():
  def __init__(self):
    self.data = []
    with open(input_path) as self.file_input:
      reader = csv.reader(self.file_input, delimiter=csvDelimiter)
      rows = list(reader)
      self.rawData = rows[slice(1, len(rows))]

  def load(self):
    for row in self.rawData:
      if (row[0] != ''):
        fallbackDate = row[0]
      self.data.append(t.Record(*row, fallbackDate))
    self.close()

  def close(self):
    self.file_input.close()
  
  def get_all(self):
    return self.data

class OutputHandler():
  # def __init__(self):
  #   if (!os.path.exists(output_totals_path)):

  def write(self, data):
    with open(output_totals_path, 'w', newline='') as self.file_output:
      field_names = c.names
      self.writer = csv.DictWriter(self.file_output, fieldnames=field_names)
      self.writer.writeheader()
      for row in data:
        self.writer.writerow(row.get())

      self.file_output.close()
