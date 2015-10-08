#Credit Card Payments
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


balance = 4213           # Total balance on the account
annualInterestRate = .2                #APR on the card
monthlyPaymentRate = .04         # Minimum rate that we have to pay monthly
i = 1
mon_interest_rate = annualInterestRate / 12.0
total_paid = 0
while i <= 12:    
    min_mon_payment = monthlyPaymentRate * balance
    total_paid += min_mon_payment
    prev_balance = balance - min_mon_payment
    rem_balance =  prev_balance + (mon_interest_rate * prev_balance)
    print 'Month:',
    print  i
    print 'Minimum monthly payment:',
    print  float("{0:.2f}".format(min_mon_payment))
    print 'Remaining balance:',
    print  float("{0:.2f}".format(rem_balance)) 
    balance = rem_balance           
    i += 1
print 'Total paid:',
print float("{0:.2f}".format(total_paid))
print 'Remaining balance:',
print float("{0:.2f}".format(balance))

