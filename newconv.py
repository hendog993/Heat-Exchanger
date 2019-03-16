import xlrd
import csv

input_file = input("Enter file name: \n")
# input_file = "leader_data.xls"  # Name this the file from the data analysis
output_file = "AveragedData.csv"
data = xlrd.open_workbook(input_file)
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
sheet3 = data.sheet_by_index(2)
sheet4 = data.sheet_by_index(3)
sheet5 = data.sheet_by_index(4)
sheets = [sheet1, sheet2, sheet3, sheet4, sheet5]


def list_average(sheet, column):
	average = round(sum(sheet.col_values(column, 2, 11)) / len(sheets[x].col_values(column, 2, 11)), 2)
	return average


for x in list(range(0, 5)):
	t1 = list_average(sheets[x], 2)
	t2 = list_average(sheets[x], 3)
	t3 = list_average(sheets[x], 4)
	t4 = list_average(sheets[x], 5)
	t5 = list_average(sheets[x], 6)
	t6 = list_average(sheets[x], 7)
	hot_flow = list_average(sheets[x], 13)
	cold_flow = list_average(sheets[x], 15)
	cph = list_average(sheets[x], 19)
	cpc = list_average(sheets[x], 20)
	hot_avg = list_average(sheets[x], 21)
	rho_hot = list_average(sheets[x], 22)
	cold_avg = list_average(sheets[x], 23)
	rho_cold = list_average(sheets[x], 24)
	dt_hot = list_average(sheets[x], 25)
	dt_cold = list_average(sheets[x], 26)
	mf_hot = list_average(sheets[x], 27)
	mf_cold = list_average(sheets[x], 28)

	with open(output_file, "a", newline="") as output:
		outputWriter = csv.writer(output)
		outputWriter.writerow([t1, t2, t3, t4, t5, t6, hot_flow, cold_flow, cph, cpc, hot_avg, rho_hot, cold_avg,
							   rho_cold, dt_hot, dt_cold, mf_hot, mf_cold])
	output.close()

print("CSV Successfully generated to ", output_file)
