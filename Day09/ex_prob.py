class Company:

    Name="TCS"
    #super constructor
    def __init__(self,CEO="Kiran",HR="Bhanu",Floor="3rd"):
        self.CEO=CEO
        self.HR=HR
        self.Floor=Floor

class ravi(Company):
    def __init__(self,ID,Salary):
        self.ID = ID
        self.Salary = Salary
        super().__init__()
        print(f"Iam working in {self.Name}, My company CEO is {self.HR}. Iam in {self.Floor} Floor, My ID is {self.ID} and my salary is {self.Salary}")

com = ravi(1,10000)


