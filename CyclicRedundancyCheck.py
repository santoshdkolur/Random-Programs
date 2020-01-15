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
    return ([''.join(data),''.join(temp[1:])])

def reciever(codeword,key):
    codeword=list(str(codeword))
    key=list(str(key))
    temp=codeword[:len(key)]
    quotient=[]
    count=0;
    for i in range(len(codeword)):
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
        if(i<(len(codeword)-len(key))):
            temp.append(codeword[i+len(key)])
        else:
            break
        temp=temp[1:]
    for ele in temp[1:]:
        if(ele=='1'):
            return False
    return True


def main():
    dataword=input("Enter the dataword:")
    key=input("Enter the key:")
    Sender_return=Sender(dataword,key)
    #You can basically check if the recieved codeword is correct
    codeword_reciever=input("Enter the codeword at the reciever:")
    print("Successful transmission" if (reciever(codeword_reciever,key)) else "Error Detected")


if __name__== "__main__":
  main()

