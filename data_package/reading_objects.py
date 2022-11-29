import xlrd
from library.config import Config
# path = Config.Data_path

   #
   # def read_teat_data(self,sheetname):
   #      workbook = xlrd.open_workbook(Config.Data_path)
   #      worksheet = workbook.sheet_by_name(sheetname)
   #      columns = worksheet.ncols
   #      print(columns)
   #      rows = worksheet.get_rows()
   #      header = next(rows)
   #      data = []
   #
   #      for row in rows:
   #         values = ()
   #         for j in range(columns):
   #            values += (row[j].value,)
   #         data.append(values)
   #      return data

def read_locators():
    workbook = xlrd.open_workbook(Config.Data_path)
    worksheet = workbook.sheet_by_name("wishlist")
    rows = worksheet.nrows
    # print(rows)
    d = {}
    for i in range(1,rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1],row[2])
    return d

print(read_locators())