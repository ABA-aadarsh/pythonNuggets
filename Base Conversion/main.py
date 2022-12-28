class ConversionToDecimal:
    def baseValidity(self,base):
        if int(base)>1 and int(base)<11:
            return 1
        else:
            print("\nChoose a number that has base between 2 and 10")
            return 0
    def numValidity(self,base):
        if self.baseValidity(base)==1:
            validCharacters="."   #   '.' <---- included to represent decimal point
            for i in range(0,base):
                validCharacters=validCharacters+str(i)
            for i in range(len(num)):
                if num[i] in validCharacters:   #  making num string helps us here
                    permission=True
                else:
                    permission=False
                    break
            if permission:
                return 1 
            else:
                print("\nEnter valid input")
                return 0 
        else: 
            return
    def convertToDecimal(self,num,base):    # it will help to divide separately the long process of converting both integer part and fractional part 
        # remember num is still a string here
        if self.numValidity(base)==1:
            if(float(num)-int(float(num)))==0:
                decimalValue=self.convertIntPartToDecimal(str(int(num)),base)
                return (decimalValue)
            else:
                value1=self.convertIntPartToDecimal(str(int(float(num))),base)
                value2=self.convertFracPartToDecimal(num,base)
                decimalValue=value1+value2
                return (decimalValue)
        else:
            return "!@"
    def convertIntPartToDecimal(self,num,base):
        numList=[]
        for i in range(0,len(num)):
            numList.append(int(num[i]))
        numList.reverse()
        decimalIntValue=0 
        for i in range(0,len(numList)):
            decimalIntValue+=numList[i]*pow(base,i)
        return decimalIntValue
    
    def convertFracPartToDecimal(self,num,base):
        i=num.find(".")+1
        numList=[]
        decimalFracValue=0
        for j in range(i,len(num)):
            numList.append(int(num[j]))
        for i in range(0,len(numList)):
            decimalFracValue+=numList[i]*pow(base,-(i+1))
        return decimalFracValue

class ConversionToOtherBase:
    def CONVERT(self,num,base):
        if num-int(num)==0:
            value=self.convertInt(int(num),base)   # i want a string result 
            return value
        else:
            value1=self.convertInt(int(num),base)  # i want a string result
            value2=self.convertFrac(num-int(num),base)  # i want a string result
            value=value1+"."+value2  # i want a string result
            return value

    def convertInt(self,num,base):
        alist=[]
        if num%base==0:
            alist.append(str(0))
            while(num!=0):
                num=num/base
                alist.append(str(int(num%base)))
                num=num-num%base
            alist.reverse()
            value=""
            for i in range(0,len(alist)):
                value+=alist[i]
        else:
            alist.append(str(int(num%base)))
            num=num-num%base
            while(num!=0):
                num=num/base
                alist.append(str(int(num%base)))
                num=num-num%base
            alist.reverse()
            value=""
            for i in range(0,len(alist)):
                value+=alist[i]
        return value
    
    def convertFrac(self,num,base):
        value=""
        for i in range(0,15):
            num=num*base
            value+=str(int(num))
            num=num-int(num)
        return value
# .............................................................................
base=int(input("Enter the base of your number: "))
num=input("\nEnter the number: ")   # num is taken as string
number=ConversionToDecimal()
deci=number.convertToDecimal(num,base)   # deci is a number not a string here

'''if else statement is used below because deci will have "!@" ,
 if input by user is wrong otherwise it will give meaningful result'''
 
if(deci!="!@"):
    print("\n",end="")
    for base in range(2,11):
        number_s=ConversionToOtherBase()
        result=number_s.CONVERT(deci,base)
        print(f"IN BASE {base} :: {result}")
    a=input("Press any key to exit...")
else:
    pass   # i do not want to do anything further if input by user is invalid
# ............................................................................



