#	      Test Case 1:
#	      balance = 320000
#	      annualInterestRate = 0.2
#
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 29157.09


#	      Test Case 2:
#	      balance = 999999
#	      annualInterestRate = 0.18
#	      
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 90325.03
	      
balance = init = 999999
annualInterestRate = 0.18

minval = balance/12 ; maxval = balance * ((1 + (annualInterestRate / 12.0))**12)/12
while abs(balance) >= 0.01:
    balance = init; payment = (minval + maxval)/2.0
    for i in range(12):
        monthlyinterest = annualInterestRate / 12.0
        balance  = balance - payment
        balance += balance * monthlyinterest
    if balance > 0:
        minval = payment
    elif balance < 0:
        maxval = payment
    else:
        break
print "Lowest Payment: " + str(round(payment,2))
