class student:
    def __init__(self,s_id,s_age,s_marks):
        self.s_id=s_id
        self.s_age=s_age
        self.s_marks=s_marks
        
    def validate_marks(self):
        if(self.marks>0 and self.marks<101):
            return True
        else:
            return False
        
    def validate_age(self):
        if(self.s_age>20):
            return True
        else:
            return False
        
    def qualification(self):
##        x=validate_marks()
##        y=validate_age()
        if(self.s_marks>=65 and self.s_age>20):
            return True
        else:
            return False
            
    def setdata(self):
        self.s_id=int(input("Enter Student id:"))
        self.s_age=int(input("Enter Student age:"))
        self.s_marks=int(input("Enter Student marks:"))
        
    def getdata(self,s_id,s_age,s_marks):
        return self.s_id
        return self.s_age
        return self.s_marks

s=student(0,0,0)
t=s.setdata()
u=s.qualification()
if(u==True):
    print("valid")

else:
    print("invalid")
v=s.getdata(0,0,0)
