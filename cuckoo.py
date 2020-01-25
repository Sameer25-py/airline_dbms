size=11
table1=["empty"]*size
table2=["empty"]*size

def hash1(x):
    return x%size
def hash2(x):
    return (x//size)%size

def rehash():
    global size
    global table1
    global table2
    new=[]
    for i in table1:
        if i!="empty":
            new.append(i)
    for j in table2:
        if j!="empty":
            new.append(j)
    size=size*2
    table1=["empty"]*size
    table2=["empty"]*size
    for k in new:
        insert(k,1,1,0)
    return

def insert(x,hashchoice,tablechoice,counter):
    if hashchoice==1:
        key=hash1(x)
    elif hashchoice==2:
        key=hash2(x)
    if tablechoice==1:
        table=table1
    elif tablechoice==2:
        table=table2
    if table[key]==x:
        print("element {} already exist in table{} at location {}".format(x,tablechoice,key))
    elif table[key]=="empty":
        table[key]=x
        print(" element {} inserted in Table{} at index {}".format(x,tablechoice,key))
        return
    else:
        catch=table[key]
        print("element {} removed in Table{} at index {}".format(catch,tablechoice,key))
        table[key]=x
        print(" element {} inserted in Table{} at index {}".format(x,tablechoice,key))
        if hashchoice==2:
            hashchoice=1
        else:
            hashchoice=2
        if tablechoice==1:
            tablechoice=2
        else:
            tablechoice=1
        
        if counter==size:
            print(" REHASHING WITH 2x ")
            rehash()
            
            
        insert(catch,hashchoice,tablechoice,counter+1)
        

def delete(x):
    key1=hash1(x)
    key2=hash2(x)
    if table1[key1]==x:
        table1[key1]="empty"
        print("KEY {} DELETED FROM TABLE {}".format(x,1))
    elif table2[key2]==x:
        table2[key2]="empty"
        print("KEY {} DELETED FROM TABLE {}".format(x,2))
    else:
        print("KEY {} not found ".format(x))

def search(x):
    key1=hash1(x)
    key2=hash2(x)
    if table1[key1]==x:
        print("KEY {} at index {} in table1".format(x,key1))
    elif table2[key2]==x:
        print("KEY {} at index {} in table2".format(x,key2))
    else:
        print("KEY : {} not found ".format(x))


hashchoice=1
tablechoice=1
while True:
    print("1-ADD KEY")
    print("2-REMOVE KEY")
    print("3-SEARCH KEY")
    print("4-SHOW TABLES")
    print("5-EXIT")
    y=input("ENTER CHOICE ")
    if y=="1":
        x1=int(input("ENTER KEY "))
        insert(x1,hashchoice,tablechoice,0)
        continue
    elif y=="2":
        x2=int(input("ENTER KEY "))
        delete(x2)
        continue
    elif y=="3":
        x3=int(input("ENTER KEY "))
        search(x3)
        continue
    elif y=="4":
        print("table 1",table1)
        print("-"*len(table2)*10)
        print("table 2",table2)
        continue
    else:
        break
    
    

             
        
    
    
