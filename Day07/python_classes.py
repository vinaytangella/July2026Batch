class Student:
    #constructor
    def __init__(self,name,standard):
        # s1_obj == self
        #properties - to add more props
        self.name = name
        self.standard = standard

    #actions - methods
    def attendClass(self,class_name,time_period):
        print(f'{self.name} is attending {class_name} at {time_period} session.')

    def submitAssignment(self,subject,deadline,type_of_submission,date_time_of_submission):
        print(f'{self.name} is submitting {subject} assignment on {date_time_of_submission} and the mode of submission is {type_of_submission}. This assignment has a deadline until {deadline}.')


#how to make it real - is to create objects

#blueprint - construct an house(livable)

# s1_obj = Student()
# print(s1_obj)
# print(type(s1_obj))
# s1_obj.name='rohit'
# s1_obj.standard='10'

# s2_obj = Student()
# s2_obj.name = 'sam'
# s2_obj.standard = '9'

# s3_obj = Student()
# s3_obj.name = 'Harshitha'
# s3_obj.standard = '8'

#constructors - come handy

s1_obj = Student('rohit','10')
s2_obj = Student('sam','9')
s3_obj = Student('harshita','8')

print(s1_obj.name,s1_obj.standard)
s1_obj.attendClass('Python','Evening')
#self,subject,deadline,type_of_submission,date_time_of_submissio
s1_obj.submitAssignment('Python','08-12-2026', 'Online', '08-11-2026 11:00 AM')

#self - 
