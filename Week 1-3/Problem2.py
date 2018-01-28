balance=float(raw_input('Enter the Initial Amount Credited: '))
annualInterestRate=float(raw_input('Enter the Annual Interest Rate: '))
months=12
monthlyInterestrate=annualInterestRate/12
monthlypayment=10
while balance>0:
    newmonths=months
    newbalance=balance
    for newmonths in range(newmonths):
        newbalance=((newbalance-monthlypayment)*(1+monthlyInterestrate))
        newmonths=newmonths-1
    if newbalance>0:
        monthlypayment=monthlypayment+10
    else:
        break
print('Lowest Payment: '+str(monthlypayment))

