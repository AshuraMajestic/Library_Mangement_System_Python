import string
from time import sleep
import choice
import show
def name():
    k = input("\n\nEnter the name of the book you want to check:")
    f =open('library.txt','r')
    lines = f.readlines()
    k = string.capwords(k)
    new_list = []
    idx=0
    count=0
    for line in lines:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
            count+=1
    f.close()
            
    if len(new_list)==0:
        print("\n\""+k+"\" is not available in library")
        name()
    else:
        print("\nThere are ",count," available in the book with this name\n")
        lineLen = len(new_list)
                
        for i in range(lineLen):
            print(end=new_list[i])
        l = int(input("\n\nIf yow want the summary of the following books Enter1 press \nIf you want to find another book enter 2 \npress 3 for exiting the search book:\n"))
        sleep(2);
        if(l==1):
            show.summary_name(k);
            choice.use()                                
        elif(l==2):
            name()
        else:
            choice.use()    
            
def author():
    k = input("\n\nEnter the name of the author you like:")
    f =open('library.txt','r')
    lines = f.readlines()
    k = string.capwords(k)
    new_list = []
    idx=0
    count=0
    for line in lines:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
            count+=1
    f.close()
            
    if len(new_list)==0:
        print("\nThe book of your favorite author is not available in the library")
        author()
    else:
        print("\nThere are ",count," available in the library with this author's name\n")
        l = int(input("\n\nIf yow want the summary of the following books Enter1 press \nIf you want to find another book enter 2 \npress 3 for exiting the search book:\n"))
        sleep(2);
        if(l==1):
            show.summary_author(k);
            choice.use()                
        elif(l==2):
            author()
        else:
            choice.use()  
            
def code():
    k = input("\n\nEnter the code of the book:")
    f =open('library.txt','r')
    lines = f.readlines()
    k = string.capwords(k)
    new_list = []
    idx=0
    count=0
    for line in lines:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
            count+=1
    f.close()
            
    if len(new_list)==0:
        sleep(2)
        print("\n\nThe book with this code is not available in the library")
        code()
    else:
        sleep(2)
        show.summary_code(k);
        i = int(input("\nEnter 1 to search another book with code \nEnter 2 to go to main choices"))
        if(i==1):
            code()
        elif(i==2):
            choice.use()
        else:
            print("\nWrong Input")