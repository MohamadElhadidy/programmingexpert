import json
import re

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex2 = re.compile(
    r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')


def is_file_empty(file_name):
    """ Check if file is empty by reading first character in it"""
    # open ile in read mode
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False


def open_file():
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    return contacts


if is_file_empty('contacts.json'):
    contacts = {"contacts": []}
else:
    contacts = open_file()


def exist(first_name, last_Name):
    if is_file_empty('contacts.json'):
        return True
    contacts = open_file()
    for lst in contacts['contacts']:
        if lst['first_name'] == first_name and lst['Last_Name'] == last_Name:
            print('A contact with this name already exists.')
            return False
    return True


def search(first_name, last_Name):
    contacts = open_file()
    count = 0
    for lst in contacts['contacts']:
        if first_name in lst['first_name'] and last_Name in lst['Last_Name']:
            count += 1
    return count


def list_search_data(first_name, last_Name):
    contacts = sorted(open_file()['contacts'],
                      key=lambda item: item['first_name'])
    for index, lst in enumerate(contacts):
        if first_name in lst['first_name'] and last_Name in lst['Last_Name']:
            print(f"{index + 1 }. ", end='')
            print(f"{lst['first_name']} {lst['Last_Name']}")
            if len(lst['phone']) > 0:
                print(' ' * 5, f"Mobile: {lst['phone']}")
            if len(lst['Home_Phone_Number']) > 0:
                print(' ' * 5, f"Home: {lst['Home_Phone_Number']}")
            if len(lst['Email_Address']) > 0:
                print(' ' * 5, f"Email: {lst['Email_Address']}")
            if len(lst['Address']) > 0:
                print(' ' * 5, f"Address: {lst['Address']}")


def delete_contact(first_name, last_Name):
    contacts = open_file()
    for index, lst in enumerate(contacts['contacts']):
        if lst['first_name'] == first_name and lst['Last_Name'] == last_Name:
            return True, index
    return False, 0


def isValidEmail(email):
    if len(email) == 0:
        return True
    if re.fullmatch(regex, email):
      return True
    else:
      print("Invalid email address.")
      return False


def isValidPhone(phone):
    if len(phone) == 0:
        return True
    if re.fullmatch(regex2, phone):
      return True
    else:
      print("Invalid mobile phone number.")
      return False


print('Welcome to your contact list!\n\nThe following is a list of useable commands:\n"add": Adds a contact. "delete": Deletes a contact.')
print('"delete": Deletes a contact.\n"list": Lists all contacts.\n"search": Searches for a contact by name.\n"q": Quits the program and saves the contact list.\n')
command = input('Type a command: ')
while command != 'q':
    if command == 'add':
        first_name = input('First Name: ')
        last_Name = input('Last Name: ')
        phone = input('Mobile Phone Number: ')
        Home_Phone_Number = input('Home Phone Number: ')
        email = input('Email Address: ')
        Address = input('Address: ')
        if exist(first_name, last_Name) and isValidPhone(phone) and isValidEmail(email):
            contacts['contacts'].append({"first_name": first_name, "Last_Name": last_Name, 'Email_Address': email,
                                        'phone': phone, 'Home_Phone_Number': Home_Phone_Number, 'Address': Address})
            with open("contacts.json", "w") as f:
                json.dump(contacts, f)
            print('Contact Added! ')
        else:
            print("You entered invalid information, this contact was not added.")

    elif command == 'delete':
        first_name = input('First Name: ')
        last_Name = input('Last Name: ')
        index = delete_contact(first_name, last_Name)
        if index[0]:
            confirm = input(
                'Are you sure you would like to delete this contact (y/n)?')
            if confirm == 'y':
                contact = open_file()['contacts']
                contact.pop(index[1])
                contacts['contacts'] = contact
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f)
                print('Contact deleted!')
        else:
            print('No contact with this name exists.')

    elif command == 'list':
        lists = open_file()
        for index, lst in enumerate(lists['contacts']):
            print(f"{index + 1 }. ", end='')
            print(f"{lst['first_name']} {lst['Last_Name']}")
            if len(lst['phone']) > 0:
                print(' ' * 5, f"Mobile: {lst['phone']}")
            if len(lst['Home_Phone_Number']) > 0:
                print(' ' * 5, f"Home: {lst['Home_Phone_Number']}")
            if len(lst['Email_Address']) > 0:
                print(' ' * 5, f"Email: {lst['Email_Address']}")
            if len(lst['Address']) > 0:
                print(' ' * 5, f"Address: {lst['Address']}")
    elif command == 'search':
        first_name = input('First Name: ')
        last_Name = input('Last Name: ')
        count = search(first_name, last_Name)
        print(f"Found {count} matching contacts.")
        if count > 0:
            list_search_data(first_name, last_Name)

    else:
        print('Unknown command')
    command = input('Type a command: ')

print('Contacts were saved successfully.')
