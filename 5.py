class CallDetail:
    def __init__(self,a,b,c,d):
        self.callfrom=a;
        self.callto=b;
        self.duration=c;
        self.type=d;

    def print(self):
        print("callfrom:",self.callfrom)
        print("callto:",self.callTO)
        print("duration:",self.duration)
        print("type:",self.type)
        print()

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        l=[]
        for i in range(len(list_of_call_string)):
            a=list_of_call_string[i].split(",")
            b=CallDetail(a[0],a[1],a[2],a[3])
            b.print()
            l.append(b)
    
call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call1,call2,call3]

Util().parse_customer(list_of_call_string)
