#making a caesar cipher code
class CaesarCipher:
    def __init__(self,shift):
        self.shift=shift
        self.alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

    def encrypt(self):
        data=str(input("Please enter a text: "))
        if data.isalpha()==True:
            data=data.lower()
            pass
        else:
            raise IndexError("Please enter only alphabets not other symbols")
        
        k=list(data)
        x=[]
        for char in k:
            z=self.alpha.index(char)
            x.append(self.alpha[((z+self.shift)%26)])
        print("".join(x))
        return 
    def dencrypt(self):
        data=str(input("Please enter a text: "))
        if data.isalpha()==True:
            data=data.lower()
            pass
        else:
            raise IndexError("Please enter only alphabets not other symbols")
        k=list(data)
        x=[]
        for char in k:
            z=self.alpha.index(char)
            x.append(self.alpha[((z-self.shift)%26)])
        print("".join(x))
        return         
        
z=CaesarCipher(7)
z.encrypt()
z.dencrypt()
