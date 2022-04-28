class atm (object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    
    def checkBalance(self):
        print('your balance is 5000000')

    def withdrawn(self,amount):
        newamount=5000000-amount
        print('amount remaining ')
        print(str (newamount))

cardnumber=input('Enter your card number')
pinnumber=input('Enter your pin number ')

user=atm(cardnumber,pinnumber)
user.checkBalance()
user.withdrawn(1000)
      
