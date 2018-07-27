import xlrd
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

# Specify which file we want to load
def parse_file(datafile):
  workbook = xlrd.open_workbook(datafile)
  sheet = workbook.sheet_by_index(0)
  
  data = 
