import time

while True:
    length = int(input("the Length of your password(not less than 8): "))
    if length > 0 and length >= 8:
        print("The length is suitable")
        break
    else:
        print("You entered a password that was too small.")

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
all_chars = uppercase + lowercase + digits + symbols

def get_random(limit):
    return abs(hash(time.time_ns())) % limit

password_length = length
password = ""

for i in range(password_length):
    index = get_random(len(all_chars))
    password += all_chars[index]

print("Ваш пароль:", password)
