open_list=["[","{","("] 
close_list=["]","}",")"] 
class parenthisis:
    def str_check(self,myStr): 
        bracket=[] 
        for i in myStr: 
            if i in open_list: 
                bracket.append(i) 
            elif i in close_list: 
                pos=close_list.index(i) 
                if((len(bracket)>0)and(open_list[pos]==bracket[len(bracket)-1])): 
                    bracket.pop() 
                else: 
                    return "Invalid"
        if len(bracket)==0: 
            return "Valid"
pr=parenthisis()
string = str(raw_input("Enter the String of parenthisis: "))
print(string,"-",pr.str_check(string)) 
