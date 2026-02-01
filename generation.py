import secrets

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
all_chars = uppercase + lowercase + digits + symbols


while True:
    length = int(input("the Length of your password(not less than 8): "))
    if length > 0 and length >= 8:
        print("The length is suitable")
        break
    else:
        print("You entered a password that was too small.")

password = ""
for i in range(length):
    password += secrets.choice(all_chars)
print("Your password:", password)

