import pickle

def create():
    phonebook = {}
    while True:
        name = input("Enter a name (or for exit plz type= 1): ")
        if name.lower() == '1':
            break
        phonenumber = input("Enter the phone number: ")
        phonebook[name] = phonenumber

    with open('phone_book.dat', 'wb') as file:
        pickle.dump(phonebook, file)

    print("Phone book has been created and stored in 'phone_book.bin'.")
if __name__ =="__main__":
    create()