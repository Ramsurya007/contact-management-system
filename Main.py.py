def add_contact():
    with open('contact.txt','a+') as f :
        name = input("Enter a Name:")
        number = input("Enter a Number:")
        f.write(f'{name}-{number}\n')

def display_contact():
    with open('contact.txt','r') as f :
        for i in f:
            name, number =i.split('-')
            print(f'Name:{name}->Number:{number}')
def delete_contacr():
    with open('contact.txt','r') as f :
        contact=f.readlines()
    name = input("Enter a name to delete:")
    new_contact=[]
    for i in contacts:
        stored_name, number = i.strip().split('-')
        if stored_name != name:
            new_contacts.append(i)
    with open('contact.txt','w') as f :
        f.writelines(new_contact)
        

while True:
    choice = int(input("\n1. Add Contact\n2. Display Contact\n3. Delete Contact\n4. Exit\nEnter choice: "))

    match choice:
        case 1:
            add_contact()
        case 2:
            display_contact()
        case 3:
            delete_contact()
        case 4:
            break
        case _:
            print("Enter valid option")
