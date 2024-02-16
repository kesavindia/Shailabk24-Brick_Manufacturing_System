class Bank:
    bankName = 'AxisBank'
    custCount = 0

    @classmethod
    def bankStatus(cls):
        if cls.custCount > 10:
            bank = "Premium"
        else:
            bank = "local"
        return bank
    def __init__(self,AccNo,branch,course,loanAmount,AccType):
        self.AccNo = AccNo
        self.branch = branch
        self.course = course
        self.loanamount = loanAmount
        self.Acctype = AccType
        Bank.custCount += 1

    def CalcInterest(self):
        interest = self.loanamount*10/100
        print(interest)
        print(help(type(self)))

Satish = Bank(123,'melur','BE',10000,'SB')
Suresh = Bank(124,'Belur','BE',20000,'SB')
Ramesh = Bank(125,'Sulur','BE',30000,'SB')
Ramesh1 = Bank(126,'Sulur','BE',30000,'SB')
Ramesh2 = Bank(127,'Sulur','BE',30000,'SB')
Ramesh3 = Bank(128,'Sulur','BE',30000,'SB')
Ramesh4 = Bank(129,'Sulur','BE',30000,'SB')
Ramesh5 = Bank(130,'Sulur','BE',30000,'SB')
Ramesh6 = Bank(131,'Sulur','BE',30000,'SB')
Ramesh7 = Bank(132,'Sulur','BE',30000,'SB')
Ramesh8 = Bank(132,'Sulur','BE',30000,'SB')
Satish.CalcInterest()






