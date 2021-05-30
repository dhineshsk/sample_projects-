y = input (' enter  some nummber')
a = int(y)
prime=1
if a>1 :
    for x in range (2,a):
        print(x);print(a) ;print(a%x)
        if (a%x==0):
            prime=0
            print ("noot [prime")
            break
        
    if(prime==1):
        print ("prime number")
    
else :
    print ("not prime")
