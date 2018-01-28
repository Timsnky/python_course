balance=float(raw_input('Enter the Initial Amount Credited: '))
annualInterestRate=float(raw_input('Enter the Annual Interest Rate: '))
months=12
approx=0.001
monthlyInterestrate=annualInterestRate/12
lowerbound=balance/12
upperbound=(balance*((1+monthlyInterestrate)**12))/12
monthlypayment=((lowerbound+upperbound)/2)
newbalance=balance
while abs(newbalance)>approx:
    newmonths=months
    newbalance=balance
    for newmonths in range(newmonths):
        newbalance=((newbalance-monthlypayment)*(1+monthlyInterestrate))
        newmonths=newmonths-1
    if newbalance<0:
        upperbound=monthlypayment
    else:
        lowerbound=monthlypayment
    monthlypayment=((lowerbound+upperbound)/2.0)
print(round(monthlypayment,2))

