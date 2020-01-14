def Sender(data,key):
    data=list(str(data))
    key=list(str(key))
    temp=data[:len(key)]
    quotient=[]
    count=0;
    for i in range(len(data)):
        if(temp[0]=='0'):
            quotient.append('0')
            count=count+1;
        else:
            quotient.append('1')
            count=count+1;
        k2=key
        if(quotient[-1]=='0'):
            k2=['0' for i in range(len(key))]
        for j in range(1,len(key)):
            if(temp[j]==k2[j]):
                temp[j]='0'
            else:
                temp[j]='1'
        if(i<(len(data)-len(key))):
            temp.append(data[i+len(key)])
        else:
            break
        temp=temp[1:]
    
    for i in range(len(key)-1):
        data[-(i+1)]=temp[-(i+1)]
    print(''.join(data))
    print(''.join(temp[1:]))
    print(''.join(quotient))



Sender(100100000,1101)
