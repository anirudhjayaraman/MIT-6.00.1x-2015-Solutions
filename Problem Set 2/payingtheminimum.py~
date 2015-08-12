# Test Case 1:
#	      balance = 4213
#	      annualInterestRate = 0.2
#	      monthlyPaymentRate = 0.04
#	      
#	      Result Your Code Should Generate:
#	      -------------------
#	      Month: 1
#	      Minimum monthly payment: 168.52
#	      Remaining balance: 4111.89
#	      Month: 2
#	      Minimum monthly payment: 164.48
#	      Remaining balance: 4013.2
#	      Month: 3
#	      Minimum monthly payment: 160.53
#	      Remaining balance: 3916.89          
#	      Month: 4
#	      Minimum monthly payment: 156.68
#	      Remaining balance: 3822.88          
#	      Month: 5
#	      Minimum monthly payment: 152.92     
#	      Remaining balance: 3731.13
#	      Month: 6
#	      Minimum monthly payment: 149.25
#	      Remaining balance: 3641.58
#	      Month: 7
#	      Minimum monthly payment: 145.66
#	      Remaining balance: 3554.19
#	      Month: 8
#	      Minimum monthly payment: 142.17
#	      Remaining balance: 3468.89
#	      Month: 9
#	      Minimum monthly payment: 138.76
#	      Remaining balance: 3385.63
#	      Month: 10
#	      Minimum monthly payment: 135.43
#	      Remaining balance: 3304.38
#	      Month: 11
#	      Minimum monthly payment: 132.18
#	      Remaining balance: 3225.07
#	      Month: 12
#	      Minimum monthly payment: 129.0
#	      Remaining balance: 3147.67
#	      Total paid: 1775.55
#	      Remaining balance: 3147.67

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0	      
for i in range(12):
    month = i + 1
    minPayment = monthlyPaymentRate * balance; balance -= minPayment; balance += balance * (annualInterestRate/12); totalPaid += minPayment
    print "Month: " + str(month) + "\n" + "Minimum monthly payment: " + str(round(minPayment, 2)) + "\n" + "Remaining balance: " + str(round(balance, 2))
    if i == 11:
        print "Total paid: " + str(round(totalPaid, 2)) + "\n" + "Remaining balance: " + str(round(balance, 2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
