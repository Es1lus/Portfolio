import random

chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,.~!@#$%^&*()_+QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"

password_len = int(input("Type a length of the password: "))
password_count = int(input("Type how many passwords would u like to generate: "))

for x in range(0,password_count):
    print("passowrd number:, ", x+1)
    password = ""
    for x in range(0, password_len):
        password_char = random.choice(chars)
        password += password_char
    print(password)
