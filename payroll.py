# Project: Payroll calculator
# Joel Broos 

name = input("Enter employee's name: ")
hoursWorked = float(input('Enter number of hours worked in a week: '))
hourlyRate = float(input('Enter hourly pay rate: '))
atoRate = float(input('Enter ATO tax withholding rate: '))
medicareRate = float(input('Enter Medicare Levy rate: '))

# Gross pay calculation
grossPay = hoursWorked * hourlyRate
# Tax total calculation
taxTotal = atoRate * grossPay
# Medicare levy calculation
medicareLevy = medicareRate * grossPay
# Total deductions calculation
totalDeduct = taxTotal + medicareLevy
# Net pay calculation
NetPay = grossPay - totalDeduct

# Print the user's payroll
print(f'\nEmployee Name: {name}')
print(f'Hours Worked: {hoursWorked}')
print(f'Pay Rate: ${hourlyRate}')
print(f'Gross Pay: ${grossPay}')
print('Deductions:')
print(f'\tATO tax({atoRate:.0%}): ${taxTotal:.2f}')
print(f'\tMedicare Levy({medicareRate:.0%}): ${medicareLevy:.2f}')
print(f'\tTotal Deduction: ${totalDeduct:.2f}')
print(f'\nNet Pay: ${NetPay:.2f}')