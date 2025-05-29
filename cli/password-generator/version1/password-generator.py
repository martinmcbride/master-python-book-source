import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
punctuation = "$?*&%@#=()"

password_characters ="".join([lowercase, uppercase, numbers, punctuation])

LENGTH = 16

def generate_password():
    password = []
    for i in range(LENGTH):
        password.append(random.choice(password_characters))

    return "".join(password)

def main():
    print("Your password is:")
    print(generate_password())

if __name__ == "__main__":
    main()
