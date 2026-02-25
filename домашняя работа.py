import random

choices = {1: "камень", 2: "ножницы", 3: "бумага"}

user = int(input("1 - камень, 2 - ножницы, 3 - бумага: "))
computer = random.randint(1, 3)

print("Я:", choices[user])
print("Твоя шиза:", choices[computer])

if user == computer:
    print("Ничья")
elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print("Красавчик твоя взяла")
else:
    print("ну ты лох")