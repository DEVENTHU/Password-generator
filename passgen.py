import random
import string


if __name__ == "__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    passlen=input('Enter your password length\n')
    while True:
        if passlen.isdigit():
            plen=int(passlen)
            break
        else:
            print('Invalid value!')
            passlen=input('Enter length in digits: ')
        
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print('Your Password is')
    print("".join(s[0:plen]))
     
    
    
    