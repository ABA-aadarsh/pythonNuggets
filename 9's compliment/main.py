def complement(m,s):
    with open("result.txt","w") as f:
        f.write("\n...........................................................")
        f.write(f"\nMinuend={m}\nSubtrahend={s}")
        f.write(f"\nUsing 9's complement,\n\n9's complement of {s} is")
        f.write("\n\t "+"9"*len(s))
        f.write("\n\t-"+s)
        f.write("\n\t=> "+str(int("9"*len(s))-int(s)))
        f.write(f"\nAdding with {m}, we get,")
        f.write("\n\t "+str(int("9"*len(s))-int(s)))
        f.write("\n\t+"+m)
        f.write("\n\t=> "+str(int("9"*len(s))-int(s)+int(m)))
        z=int("9"*len(s))-int(s)+int(m)
        zs=str(z)
        if(len(zs)==len(m)):
            f.write(f"\nSince there is no overflow digit,\nanswer will be negative and be obtained by taking the 9's complement of {z},")
            f.write("\n\t "+"9"*len(s))
            f.write("\n\t-"+str(z))
            answer=str((int("9"*len(s))-z))
            answer="0"*(len(m)-len(answer))+answer
            f.write("\n\t=> "+answer)
            f.write(f"\n\nHence the answer is,(-{answer})")
        else:
            f.write(f"\nSince there is overflow digit, answer will be positive and \nbe obtained by removing the over flow digit with the last result without overflow digit,")
            answer=int(zs[1:])+int(zs[0])
            answer="0"*(len(m)-len(str(answer)))+str(answer)
            f.write(f"\n\nHence the answer is, {answer}")
        f.write("\n...........................................................")

m=(input("Minuend = "))
s=(input("Subtrahend = "))
if(len(m)==len(s)):
    complement(m,s)
else:
    if len(m)>len(s):
        s="0"*(len(m)-len(s))+s
        complement(m,s)
    else :
        m="0"*(len(s)-len(m))+m
        complement(m,s)
print("See the file named 'result.txt'")
a=input("\nPress any key to exit...")


