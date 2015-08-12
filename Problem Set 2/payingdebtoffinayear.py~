#         Test Case 1:
#	      balance = 3329
#	      annualInterestRate = 0.2
#
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 310
#	      
#  	      Test Case 2:
#	      balance = 4773
#	      annualInterestRate = 0.2
#	      
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 440

balance = init = 3329
annualInterestRate = 0.2
payment = 0
while balance > 0:
    balance = init
    for i in range(12):
        monthlyinterest = annualInterestRate / 12.0
        balance  = balance - payment
        balance += balance * monthlyinterest
    payment += 10
print "Lowest Payment: " + str(payment - 10)       
