import filefunctions as f
import datafunctions as d

# variables
result_totals = {}
result_averages = {}

# load data from file and close the file in the os
data_handler = f.DataHandler()
data_handler.load()
data = data_handler.get_all()

# calculate totals and averages
result = d.Results(data)
result_totals = result.get_totals()
result_averages = result.get_averages()

# creates a csv file with the results
output_handler = f.OutputHandler()
output_handler.write(result_totals)

