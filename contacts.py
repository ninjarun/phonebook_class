import json
from contact import contact

class contacts:
    contacts=[]
    def __init__(self,contacts=[]) -> None:
        self.contacts=contacts

    def __str__(self) -> str:
        res=''
        for contact in self.contacts:
            res+=contact.__str__()
        return res

    def addContact(self,name,pNum):
        self.contacts.append(contact(name,pNum))
    
    def jason(self,data):
        res=[]
        for contact in self.contacts:
            res.append( json.loads(contact.__str__()))
        with open(data,'r+')as f:
            tmp=json.load(f)
            for i in res:
                tmp.append(i)
        with open(data,'w')as f:
            json.dump(tmp,f,indent=4)
        self.contacts.clear()
        
    def rmvContact(self,name,data):
        with open(data,'r')as f:
            file=json.load(f)
            counter=0
            for i in (file):
                if i['name']==name:
                    del file[counter]
                counter+=1
        with open(data,'w')as f:
            json.dump(file,f,indent=4)
    
    def srcContact(self,name,data):
        with open(data,'r')as f:
            file=json.load(f)
            for i in file:
                if i['name']==name:
                    print(i)
