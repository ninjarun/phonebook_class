import json

class contact:
    name=''
    pNum=''
    def __init__(self,name='',pNum='') -> None:
        self.name=name
        self.pNum=pNum
    def __str__(self) -> str:
        return json.dumps( {"name":self.name, "phone":self.pNum})

    def return_contact_name(self,name):
        return self.name
    def return_contact_num(self,name):
        return self.pNum