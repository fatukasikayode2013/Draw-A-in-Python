h = eval(input('Enter the width of Alphabeth A: '))
for i in range(h):
    if i==0:
        print(" "*(h-i)+"*"*(2*i+1))
    if i>0:
        if i==int(h/2):
            print(" "*(h-i)+"*"*(2*i+1))
        else:
            print(" "*(h-i)+("*"*(2*i+1))[0]+" "*(len("*"*(2*i+1))-2)+("*"*(2*i+1))[-1])    
