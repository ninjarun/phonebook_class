"""
contacts application
contact: name,phone number
add contact
remove contact
search contact
"""
from contacts_helper import *
from contacts import contacts


def main():
    data_file='contacts_cell.json'
    phonebook=contacts()
    selection=1
    chkJson(data_file)
    while selection != 'x':
        menu()
        selection = input('enter your selection')
        if selection == 'a': phonebook.addContact(input('enter contact name: '),input('enter contact phone number: '))
        if selection == 'r':phonebook.rmvContact(input('what name would you like to remove? '),data_file)
        if selection == 's':phonebook.srcContact(input('what name would you like to search? '),data_file)
        if selection == 'p':print(phonebook)
        phonebook.jason(data_file)



if __name__ == "__main__":
    main()