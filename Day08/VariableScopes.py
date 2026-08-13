class XYZ:

    #class level variable
    school = 'XYZ'

    def __init__(self,name):
        self.name = name
        # self.school = school

    #instance method
    def action(self):
        # instance level variable
        y  = 10
        school = 'Tejaswi'
        phone = ''
        print(f'calling from an instance method - {self.school}')

    """
        cls
        self
    """
    
    #class method
    @classmethod #- decorator
    def ClsAction(cls):
        print(f'calling from an class method - {cls.school}')
        # print(y) #- thrown an error

    
    #static method
    @staticmethod
    def staticMethod(first_name, last_name):
        print(f'calling from an static method - {first_name} - {last_name}')
        print(XYZ.school)
        return first_name + last_name
    

x = XYZ('sam')
x.action()
XYZ.ClsAction()
XYZ.school
result = XYZ.staticMethod('sam','v')
print(result)