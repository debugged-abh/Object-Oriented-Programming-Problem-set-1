# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class pay:

    def __init__(self):
        self.x = int(input("Enter balance on credit card:"))
        self.y = float(input("Enter annual interest rate on credit card: "))
        self.z = float(input("Enter minimum monthly payment on credit card: "))

    def Minimumpayment(self):
        counter=[]

        for i in range (1,13):

            mmp = self.z * self. x
            ip = (self.y//12) * self.x
            pp = mmp - ip
            rb = self.x - pp
            self.x = rb
            counter.append(mmp)




            print("Month:",i)
            print("Minimum monthly payment", mmp)
            print("Remaining Balance:",rb)


        print("Total amount paid: ",sum(counter))
        print("Remaining Balance: ",rb)

class debtoff:

    def __init__(self):
        self.x = int(input("Enter balance on credit card:"))
        self.y = float(input("Enter annual interest rate on credit card: "))
        self.z = int(input("Enter the number of months have the debt paid off by: "))

    def payoff(self):
        n = self.z+1
        pod = self.x / self.z

        for i in range (0,n):

            mmp = self.z * self.x
            mip = self.y / self.z
            ubem = self.x * (1 + mip) - mmp
            self.x = ubem

        print("RESULT")
        print("Monthly payment to pay off debt in 1 year: ",pod)
        print("Balance: ",ubem)




g = int(input("select 1 or 2:" ))


if g==1:
    a = pay()
    a.pay()
else:
    b = debtoff()
    b.payoff()






































a=pay()
a.Minimumpayment()
























