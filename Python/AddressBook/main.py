import os, time

contacts = {}
f = open("Contacts.txt","r")
for line in f:
  key = line.split("|")[0]
  value = line.split("|")[1]
  contacts[key] = value
f.close()





def add():
    phone = input(f"{name}'s phone number:")
    email = input(f"{name}'s Email Address:")
    contacts[name] = {"phone": phone, "email": email}
    time.sleep(1)
    os.system("clear")

def viewall():
    for contact_name, contact_info in contacts.items():
        print(contact_name, ":")
        for key, value in contact_info.items():
            print(key, value)
    print()

def viewone():
    for key, value in contacts[search].items():
        print(key, value)

while True:
    menu = input("add, view, edit, or remove?")
    if menu == "add":
        name = input("Contact's name:")
        add()
    elif menu == "view":
        search = input("Show all or search by name:")
        if search == "all":
            viewall()
        elif search in contacts:
            print(search)
            viewone()
    elif menu == "edit":
        name = input("Which contact do you want to edit?")
        if name in contacts:
            changeto = input(f"What do you want to change {name} to:")
            newphone = input(f"What is {changeto}'s phone number:")
            newemail = input(f"What is {changeto}'s email address:")
            # Update the existing contact under the new name
            contacts[changeto] = {"phone": newphone, "email": newemail}
            del contacts[name]  # Remove the old contact
        else:
            print(f"{name} cannot be edited as it does not exist in your contacts")
    elif menu == "remove":
        to_remove = input("Enter the name of the contact to remove:")
        if to_remove in contacts:
            del contacts[to_remove]  # Remove the contact
            print(f"{to_remove} has been removed from your contacts.")
        else:
            print(f"{to_remove} not found in your contacts.")
          
    f = open("Contacts.txt","w")
    for key,value in contacts.items():
      addendum = f"{key} | {value} \n"
      f.write(addendum)
    f.close()
