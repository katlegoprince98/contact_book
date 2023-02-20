contact = {}


def display_contact():
    print("Name\t\tcontact number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    choice = int(input('1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete '
                       'contact \n 6. Exit'))

    if choice == 1:
        name = input('Enter contact name ')
        phone = input('Enter the mobile number')
        contact[name] = phone

    elif choice == 2:
        search_name = input('Enter the contact name you are looking for ')
        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("The name is not available on the contact book")

    elif choice == 3:
        if not contact:
            print("Contact book is empty")
        else:
            display_contact()

    elif choice == 4:
        edit_con = input("Enter contact you want to edit ")
        if edit_con in contact:
            phone = input('Enter mobile number')
            contact[edit_con] = phone
            print("Contact is updated")
            display_contact()
        else:
            print("Contact not found")

    elif choice == 5:
        del_cont = input("Enter the contact you wish to delete")
        if del_cont in contact:
            confirm = input("Are you sure that you want to delete the contact??")
            if confirm == "yes" or confirm == "Yes" or confirm == "Y" or confirm == "y" or confirm == "YES":
                contact.pop(del_cont)
                display_contact()

            else:
                print("Contact not deleted")
                exit()
                
        else:
            print("Contact not found")

    else:
        print("Good bye")
        break
