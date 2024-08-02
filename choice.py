from time import sleep
import string
import show
import search_book
import work
def use():
    print("Please Enter your Order:\n")
    print("[1] To check all books")
    print("[2] to check book by name")
    print("[3] To check book by author's name")
    print("[4] to check book by code")
    print("[5] To Issue a book")
    print("[6] To return a book")
    print("[7] When you find your desired book")
    order = int(input("Choose Wisely:"))
    if(order==1):
        sleep(2)
        print("\nThis is all Our Treasures:")
        f = open('library.txt','r')
        file_contents = f.read()
        for s in file_contents:
            s=s.replace('{','')
            s=s.replace('}','')
            s=s.replace('"','')
            s=s.replace(",","")
            print(s,end="")
        input("\npress Enter to continue")
        f.close()
        use()                                
    elif(order==2):
        sleep(1)
        search_book.name()      
    elif(order==3):
        sleep(1)
        search_book.author()
    elif(order==4):
        sleep(1)
        search_book.code()        
    elif(order==5):
        sleep(1)
        work.issue();
        use();
    elif(order==6):
        sleep(1)
        work.back();
        use()        
    elif(order==7):
        sleep(1)
        sleep(1)
        print("\nA",end="")
        sleep(1)
        print("\tS",end="")
        sleep(1)
        print("\tH",end="")
        sleep(1)
        print("\tU",end="")
        sleep(1)
        print("\tR",end="")
        sleep(1)
        print("\tA",end="")
        sleep(1)
        print("\nThanking You....")
        sleep(3)
        exit(0)
    else:
        sleep(1)
        print("Wrong input")
        use()
