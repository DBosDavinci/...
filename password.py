import random
import re
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRESTUVWXYZ1234567890@#$%&_?"
special_characters = ["@","#","$","%","&","_","?"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
password = ""

def passwordGenerator():
    global password
    random_characters = [random.choice(characters) for i in range(24)]
    password = "".join(random_characters)
    passwordCheck()

def passwordCheck():
    passwordList = list(password)
    if numbers in passwordList not in range(4,8):
        passwordGenerator()
    if lowercase in passwordList < 8:
        passwordGenerator()
    if uppercase in passwordList not in range(2,7):
        passwordGenerator()
    if special_characters in passwordList < 3:
        passwordGenerator()
    if passwordList[0] in special_characters:
        passwordGenerator()
    if passwordList[23] in special_characters:
        passwordGenerator()
    if numbers in passwordList[0:4]:
        passwordGenerator()

passwordGenerator()
print(password)