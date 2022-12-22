from posixpath import split
import string

def summary_name(k):
    f = open('library.txt','r')
    lines= f.read()
    x = lines.split(",")
    new_list=[]
    idx=0
    for line in x:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
    f.close()
    lineLen = len(new_list)
    for i in range(lineLen):
        print(end=new_list[i]) 
    
    
def summary_author(k):
    f = open('library.txt','r')
    lines= f.read()
    x = lines.split(",")
    new_list=[]
    idx=0
    for line in x:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
    f.close()
    lineLen = len(new_list)
    for i in range(lineLen):
        print(end=new_list[i]) 

def summary_code(k):
    f = open('library.txt','r')
    lines= f.read()
    x = lines.split(",")
    new_list=[]
    idx=0
    for line in x:
        if k in line:
            new_list.insert(idx, line)
            idx += 1
    f.close()
    lineLen = len(new_list)
    for i in range(lineLen):
        print(end=new_list[i])    
    return new_list
