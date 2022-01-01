class Atm:
    def __init__ (self,CashWithdrawl,BalanceEnquiry):
        self.BalanceEnquiry=BalanceEnquiry
        self.CashWithdrawl=CashWithdrawl
        
    def infoOfCar(self):
        print("CashWithdrawl  "+self.CashWithdrawl)
        print("BalanceEnquirie "+self.BalanceEnquiry)       

s1808=Atm(1965895,150,)
n394223=Atm(69944,150,)

def getInfo():
    car=input("enter your card number and pin numder")
    if(Atm=="s1808"):
        s1808.infoOfCar()
    elif(Atm=="n394223"):
        n394223.infoOfCar()
    else:
        print("you have enter incorrect card number")

getInfo()

#CashWithdrawl, BalanceEnquiry