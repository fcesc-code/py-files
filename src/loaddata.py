from datetime import datetime
logd = datetime.now()
import os
import csv

# constants
file = 'rome_data.csv'
directory = 'py-files\\data\\confidential'
csvDelimiter = ';'
cwd = os.getcwd()
path = os.path.join(cwd, directory, file)
names = ['date', 'time', 'boilers', 'chillers', 'heating WH', 'cooling WH', 'ventilation WH', 'heating OW', 'cooling OW', 'ventilation OW', 'lighting', 'MHE']
units = ['int', 'hh:mm', 'kW', 'kW', 'kW', 'kW', 'kW', 'kW', 'kW', 'kW', 'kW', 'kW']

# classes
class Count:
  days = 0
  hours = 0
class Record:
  def __init__(self, date, hour, boilers, chillers, heatingWh, coolingWh, ventilationWh, heatingOw, coolingOw, ventilationOw, lighting, mhe, fallbackDate):
    if(date == ''):
      self.date = fallbackDate
    else:
      self.date = date
    self.hour = hour
    self.boilers = float(boilers)
    self.chillers = float(chillers)
    self.heatingWh = float(heatingWh)
    self.coolingWh = float(coolingWh)
    self.ventilationWh = float(ventilationWh)
    self.heatingOw = float(heatingOw)
    self.coolingOw = float(coolingOw)
    self.ventilationOw = float(ventilationOw)
    self.lighting = float(lighting)
    self.mhe = float(mhe)
  def __str__(self):
    return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.date, self.hour, self.boilers, self.chillers, self.heatingWh, self.coolingWh, self.ventilationWh, self.heatingOw, self.coolingOw, self.ventilationOw, self.lighting, self.mhe)

# variables
descriptions = []
data = []
fallbackDate = ''
count = Count()
totals = Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# load data from file
with open(path) as file_input:
  reader = csv.reader(file_input, delimiter=csvDelimiter)
  rows = list(reader)
  rawData = rows[slice(1, len(rows))]

for row in rawData:
  if (row[0] != ''):
    fallbackDate = row[0]
  data.append(Record(*row, fallbackDate))
  count.hours += 1

print('Headers row', descriptions)
print('First data row', data[0])
print('Second data row', data[1])
print('El contador és', count.hours, 'hores', end='.\n')

for record in data:
  totals.boilers += record.boilers
  totals.chillers += record.chillers
  totals.heatingWh += record.heatingWh
  totals.coolingWh += record.coolingWh
  totals.ventilationWh += record.ventilationWh
  totals.heatingOw += record.heatingOw
  totals.coolingOw += record.coolingOw
  totals.ventilationOw += record.ventilationOw
  totals.lighting += record.lighting
  totals.mhe += record.mhe

print('Totals:', totals)

# create file for data output
# # fo = open('data/rome_analysis.csv', 'w')

# # capture first row as headers
# descriptions = fi.readline()
# # Since the first row are headers, count is not increased on the first line.
# while True:
#     linei = fi.readline()
#     #longitud 0 de línia indica EOF
#     if len(linei) == 0:
#         break
#     data[count] = Record()
#     count.hours += 1
# print('El contador és', count.hours, 'hores', end='.\n')



#tanquem el diccionari
# fo.write('}\n')

# tanquem els arxius
file_input.close()
# fo.close()
