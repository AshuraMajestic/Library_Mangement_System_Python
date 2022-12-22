from posixpath import split
from time import sleep
import string
import show
import choice
def back():
    k=input("\n\nEnter the book of the code you want to return")
    f=open("Lend.txt","r")
    l=open("library.txt","a")
    f2=open("bin1.txt","w")
    k= string.capwords(k)
    panda= f.read()
    x = panda.split(",")
    j=0
    for line in x:
       if(k in line):
           l.write(line+",")
           j=1
       else:
           f2.write(line+",")
       f.close()
       f2.close()
       f = open("lend.txt",'w')
       f2 = open("bin1.txt",'r')
       for lines in f2:
           f.write(lines)
       f.close()
       f2.close()
       l.close()
    if(j==0):
        print("\n\nThe book is not issued or you have entered a wrong code please re-enter")
        back()
    else:
        print("\n\nBook is Returned please visit again")
        choice.use()
        

def issue():
    k = input("\n\nEnter the code of the book to issue:")
    f = open("Lend.txt","r")
    l1 =open('library.txt','r')
    l2 =open('bin2.txt','w')
    lines = l1.readlines()
    k = string.capwords(k)
    new_list = []
    idx=0
    count=0
    for line in lines:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
            count+=1
    l1.close();
    f.close()
    l2.close()
    f= open("Lend.txt","r")
    panda = f.read()
    x=panda.split(",")
    for lines in x:
        if(k in x):
            print("Book is already issued")
            choice.use()
    if len(new_list)==0:
        sleep(2)
        print("\n\nThe book with this code is not available in the library")
        issue()
    else:
        sleep(2)
        right = show.summary_code(k)
        j=int(input("\nEnter 1 to issue the book \n press 2 to reenter the code\n"))
        f.close()
        f = open("Lend.txt","a")
        if(j==1):
            book=""
            for ele in right:
                book += ele
            f.write(book+",")
            sleep(2)
            print("Book successfully issued.")
            l1 =open('library.txt','r')
            l1.close()        
            l2.close()
            l1=open('library.txt','r')
            l2 = open('bin2.txt','w')
            kola = l1.read()
            x= kola.split(",")
            for line in x:
                if k not in line:
                    l2.write(line+",")
            l1 =open('library.txt','w')  
            l2=open('bin2.txt','r')
            for lines in l2:
                l1.write(lines)
            sleep(2)
            l1.close()
            l2.close()
            
            choice.use()
        elif(j==2):
            issue()
        else:
            print("wrong input")
            sleep(1)
            print("Entering the main menu")
            choice.use()
            sleep(2)
    f.close()
