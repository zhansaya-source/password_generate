import random

alphabe = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
           "n","o","p","q","r","s","t","u","v","w","x","y","z"]

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

special = ["&","#","!","@","$","%","^","*"]

choices = alphabe + numbers + special


def generate_password(length):
    password = []
    count = 0

    while count < length:
        password.append(random.choice(choices))
        count += 1

    return "".join(map(str, password))


def check_password_strength(password):
    if len(password) < 8:
        return "Слабый пароль"

    elif (any(s in password for s in special) and
          any(str(n) in password for n in numbers) and
          any(b in password for b in alphabe) and
          len(password) <= 10):
        return "Сильный пароль"

    else:
        return "Средний пароль"


choice = input("Выберите команду generate/check: ")

if choice == "generate":
    length = int(input("Введите длину пароля: "))
    password = generate_password(length)
    print(password)

elif choice == "check":
    password = input("Введите пароль: ")
    strength = check_password_strength(password)
    print(strength)