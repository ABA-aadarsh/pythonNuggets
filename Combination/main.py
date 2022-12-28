def findout(ml,v_o,seats):
    if(len(v_o)!=1):
        s=ml[0:v_o[0]+1]
        b=ml[v_o[0]+1:v_o[1]+v_o[0]+2]
        c=[]
        for i in range(0,len(s)):
            for j in range(0,len(b)):
                c.append(s[i]+b[j])
        for i in range(0,v_o[1]+v_o[0]+2):
            ml.pop(0)
        ml=c+ml
        v_o.pop(0)
        v_o.pop(0)
        v_o.insert(0,len(c)-1)
        findout(ml,v_o,seats)
    else:
        printout(ml,v_o,seats)
def printout(ml,v_o,seats):
    with open("results.txt","a") as f:
        for i in range(0,seats+1):  
            counter=0
            for j in ml:
                if j==i:
                    counter+=1
            f.write(f"\n{counter} possible combinations for r={i}")
# ..
number_of_different_values=int(input("How many different types of elements are there? "))
v_o=[]
ml=[]
print("\n",end="")
for i in range(1,number_of_different_values+1):
    v_o.append(int(input(f"Occurence of {i} element :: ")))
seats=sum(v_o)
for i in v_o:
    for j in range(0,i+1):
        ml.append(j)
with open("results.txt","w") as f:
    astr="["
    t=1
    for i in v_o:
        for j in range(0,i):
            astr=astr+str(t)+","
        t+=1
    astr=astr[:-1]+"]"
    f.write(astr)
findout(ml,v_o,seats)
print("\nDone. Check file named 'results.txt'")
a=input("\nPress any key to exit...")



