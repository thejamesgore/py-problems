from cryptography.fernet import Fernet
import os.path

master_pwd = input("What is the master password? ")


def load_key():
    file_exists = os.path.exists('key.key')
    while True:
        if file_exists == True:
            file = open("key.key", "rb")
            key = file.read()
            file.close()
            return key
            break
        else:
            print('Looks like this is your first time running the password manager.')
            break

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def write_key():
    file_exists = os.path.exists('key.key')
    while True:
        if file_exists == True:
            # print('key hash already exists')
            break
        else:
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
            print('Key hash written to file')
            break
write_key()



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"User: {user} | Password: ", fer.decrypt(pwd.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    mode = input("Would you like to (a)dd a new credentials or (v)iew existing ones? Press (q) to quit. ").lower()
    if mode == 'q':
        break

    if mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid mode.")
        continue
