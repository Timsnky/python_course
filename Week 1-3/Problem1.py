balance=float(raw_input('Enter the Initial Amount Credited: '))
annualInterestRate=float(raw_input('Enter the Annual Interest Rate: '))
monthlyPaymentRate=float(raw_input('Enter the Monthly Payment Rate: '))
months=12
totalpaid=0.0
monthlyInterestrate=annualInterestRate/12
for i in range(months):
    minimummonthlypayment=balance*monthlyPaymentRate
    balance=((balance-minimummonthlypayment)*(1+monthlyInterestrate))
    months=months-1
    print('Month: '+str(12-months))
    print('Minimum monthly payment: '+str(round(minimummonthlypayment,2)))
    print('Remaining balance: '+str(round(balance,2)))
    totalpaid=totalpaid+minimummonthlypayment

print('Total paid: '+str(round(totalpaid,2)))
print('Remaining balance: '+str(round(balance,2)))
