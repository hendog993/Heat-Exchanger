import xlrd
import xlwt

workbook = "leader_data.xls"
data = xlrd.open_workbook(workbook)
write_sheet = 1

sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)

# Take averages for each reading

# for x in list(range(0,5)):

t1 = round(sum(sheet1.col_values(2, 2, 11))/len(sheet1.col_values(2, 2, 11)), 2)
t2 = round(sum(sheet1.col_values(3, 2, 11))/len(sheet1.col_values(3, 2, 11)), 2)
t3 = round(sum(sheet1.col_values(4, 2, 11))/len(sheet1.col_values(4, 2, 11)), 2)
t4 = round(sum(sheet1.col_values(5, 2, 11))/len(sheet1.col_values(5, 2, 11)), 2)
t5 = round(sum(sheet1.col_values(6, 2, 11))/len(sheet1.col_values(6, 2, 11)), 2)
t6 = round(sum(sheet1.col_values(7, 2, 11))/len(sheet1.col_values(7, 2, 11)), 2)
hot_flow = round(sum(sheet1.col_values(13, 2, 11))/len(sheet1.col_values(13, 2, 11)), 2)
cold_flow = round(sum(sheet1.col_values(15, 2, 11))/len(sheet1.col_values(15, 2, 11)), 2)
cph = round(sum(sheet1.col_values(19, 2, 11))/len(sheet1.col_values(19, 2, 11)), 2)
cpc = round(sum(sheet1.col_values(20, 2, 11))/len(sheet1.col_values(20, 2, 11)), 2)
hot_avg = round(sum(sheet1.col_values(21, 2, 11))/len(sheet1.col_values(21, 2, 11)), 2)
rho_hot = round(sum(sheet1.col_values(22, 2, 11))/len(sheet1.col_values(22, 2, 11)), 2)
cold_avg = round(sum(sheet1.col_values(23, 2, 11))/len(sheet1.col_values(23, 2, 11)), 2)
rho_cold = round(sum(sheet1.col_values(24, 2, 11))/len(sheet1.col_values(24, 2, 11)), 2)
dt_hot = round(sum(sheet1.col_values(25, 2, 11))/len(sheet1.col_values(25, 2, 11)), 2)
dt_cold = round(sum(sheet1.col_values(26, 2, 11))/len(sheet1.col_values(26, 2, 11)), 2)
mf_hot = round(sum(sheet1.col_values(27, 2, 11))/len(sheet1.col_values(27, 2, 11)), 2)
mf_cold = round(sum(sheet1.col_values(28, 2, 11))/len(sheet1.col_values(28, 2, 11)), 2)

print(dir(xlwt))