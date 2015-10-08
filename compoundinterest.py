#Credit card payments to payoff debt
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#Compound interest for principal: P(1+r/n)^nt

balance = 3926
annualInterestRate = 0.2  
    
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance,2)
print 'Lowest Payment:',
print monthlyPayment

    