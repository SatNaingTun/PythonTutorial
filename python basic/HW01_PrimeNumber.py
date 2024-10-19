def isPrimeNumber(num):
    primeFlag=False
    if num>1:
        if num==2: 
            return True
        for i in range(2,num):
            if num%i==0 and num!=i:
                primeFlag=False
                break
            else:
                primeFlag=True
        
        if (primeFlag == True):
            return True
        else:
            return False
    else:
        return False
                                   
primeNumber=[i for i in range(0,100) if isPrimeNumber(i)==True ]
print(primeNumber)

        
