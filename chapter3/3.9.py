name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked: "))
payRate = eval(input("Enter the hourly pay rate: "))
fedWithholdRate = eval(input('Enter federal tax withholding rate: '))
stateWithholdRate = eval(input('Enter state tax withholding rate: '))

print("Employee name:", name, '\n'
	"Hours Worked:", hours, '\n'
	"Pay Rate: $",payRate, "\n"
	"Gross Pay: $",hours * payRate, "\n"
	'Deductions:\n'
	"\t Federal Withholding (20.0%): $",(fedWithholdRate) * (hours * payRate), '\n'
	"\t State Withholding (9.0%): $", stateWithholdRate * (hours * payRate), '\n'
	"\t Total Deduction: $",((fedWithholdRate) * (hours * payRate)) + (stateWithholdRate * (hours * payRate)), '\n'
	"Net pay: $",(hours * payRate) - (((fedWithholdRate) * (hours * payRate)) + (stateWithholdRate * (hours * payRate))))