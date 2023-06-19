"""
CONTACT BOOK OPERATIONS:
1. Add
2. Search
3. Display
4. Edit
5. Delete
6. Exit
"""

contact = {}


def display_contact():
    print("Name\t\tContact Number")  # \t are tab statements
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))  # {} placeholders for displaying name and contact n.o, .format() formats specific
        # values and inserts those into placeholders

while True:
    choice = int(input("1. Add new contact \n2. Search contact\n3. Display contact\n4. Edit contact "
                       "\n5. Delete Contact \nEnter your choice "))# \n is new line
    if choice == 1:
        name = input("Enter contact name ")
        phone = input("Enter mobile number ")
        contact[name] = phone

    elif choice == 2:
        # Check contact name and see if it is available in the dictionary
        search_name = input("Enter contact name ")
        if search_name in contact:
            print(f"{search_name}'s contact number is {contact[search_name]}")
        else:
            print("Name cannot be found in the contact book.")

    elif choice == 3:
        # See all contacts of contact book.
        # 1. Check cases if dictionary is empty or not.
        if not contact:
            print("Empty contact book.")
        else:
            display_contact()

    elif choice == 4:
        edit_contact = input("Edit contact name ")
        if edit_contact in contact:
            phone = input("Enter new mobile number ")
            contact[edit_contact] = phone
            print("Contact number updated.")
        else:
            print("Name cannot be found in the contact book.")

    elif choice == 5:
        del_contact = input("Delete contact ")
        if del_contact not in contact:
            print("Name cannot be found in the contact book.")
        else:
            confirm = input("Do you want to delete this contact, Y/N?\n ")
            if confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
                # .pop removes an item at the specified index from a list
                # Don't need to do the case N
                print(f'{name} has been deleted from your contacts')

    elif print("Enter integer values 1 to 5 only."):
        break


