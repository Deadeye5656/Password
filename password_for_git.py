import os
import json


def clear():
    os.system('cls')


def encrypt(my_dict):
    for key in my_dict:
        username = my_dict[key][0]
        pass_word = my_dict[key][1]
        temp_user = ""
        temp_pass = ""
        for i in range(len(username)):
            temp_user += chr(ord(username[i]))  # to encrypt, enter set value to power of prime and then modulo by number
        for j in range(len(pass_word)):
            temp_pass += chr(ord(pass_word[j]))  # to encrypt, enter set value to power of prime and then modulo by number
        my_dict[key] = [temp_user, temp_pass]
    return my_dict


def decrypt(my_dict):
    for key in my_dict:
        username = my_dict[key][0]
        pass_word = my_dict[key][1]
        temp_user = ""
        temp_pass = ""
        for i in range(len(username)):
            temp_user += chr(ord(username[i]))  # to decrypt, enter set value to power of new prime and then modulo by same number
        for j in range(len(pass_word)):
            temp_pass += chr(ord(pass_word[j]))  # to decrypt, enter set value to power of new prime and then modulo by same number
        my_dict[key] = [temp_user, temp_pass]
    return my_dict


def save(my_dict):
    f = 'enter path to json file here'
    my_dict = encrypt(my_dict)
    with open(f, 'w') as file_object:
        json.dump(my_dict, file_object)
    return decrypt(my_dict)


with open('enter path to json file here', 'r') as file_object:
    storage = json.load(file_object)

storage = decrypt(storage)

password = ""

while password != "enter your password here":
    password = input("Enter Password: ")

clear()
print("Correct Password")
print()

while True:
    print("Main Menu")
    print("Add password: add [website name] [username] [password]")
    print("Update password: update [website name] [username] [password]")
    print("Remove password: del [website name]")
    print("Find password: find [website name]")
    print("Show all accounts: all")
    inp = []
    while len(inp) == 0:
        inp = input("Command: ").split()
    if len(inp) > 1:
        for i in range(0, 2):
            inp[i] = inp[i].lower()
    else:
        inp[0] = inp[0].lower()
    if inp[0] != "add" and inp[0] != "find" and inp[0] != "update" and inp[0] != "del" and inp[0] != "all":
        print("Incorrect command")
        input()
        clear()
        continue
    if inp[0] == "find":
        if inp[1] in storage:
            print("Username: " + storage[inp[1]][0])
            print("Password: " + storage[inp[1]][1])
            input()
            clear()
            continue
        else:
            print("No Username/Password for this website")
            input()
            clear()
            continue
    if inp[0] == "add":
        if inp[1] in storage:
            print("Username/Password for this website already exists")
            input()
            clear()
            continue
        else:
            storage[inp[1]] = [inp[2], inp[3]]
            print("Username: " + storage[inp[1]][0])
            print("Password: " + storage[inp[1]][1])
            storage = save(storage)
            input()
            clear()
            continue
    if inp[0] == "update":
        if inp[1] in storage:
            storage[inp[1]] = [inp[2], inp[3]]
            print("Username: " + storage[inp[1]][0])
            print("Password: " + storage[inp[1]][1])
            storage = save(storage)
            input()
            clear()
            continue
        else:
            print("No Username/Password for this website")
            input()
            clear()
            continue
    if inp[0] == "del":
        if inp[1] in storage:
            storage.pop(inp[1])
            storage = save(storage)
            print("Successfully removed")
            input()
            clear()
            continue
        else:
            print("No Username/Password for this website")
            input()
            clear()
            continue
    if inp[0] == "all":
        websites = []
        for key in storage:
            websites.append(key)
        websites.sort()
        clear()
        for website in websites:
            print(website)
            print("Username: " + storage[website][0])
            print("Password: " + storage[website][1])
            print()
        input()
        clear()
        continue
