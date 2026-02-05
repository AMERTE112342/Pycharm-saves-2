



# import time
# import random
#
# class Sim:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 50
#         self.energy = 100
#         self.is_alive = True
#
#     def eat(self):
#         if self.hunger >= 100:
#             print(f"{self.name} не хочет есть")
#         else:
#             self.hunger += 20
#             self.energy -= 5
#             print(f" 🐱‍🐉 {self.name} поел(а). Голод: {self.hunger}")
#
#     def live_day(self):
#         """Этот метод вызывает каждый ход. Жизнь идет, ресурсы тратяться."""
#         self.hunger -= 10
#         self.energy -= 10
#
#         if self.hunger <= 0 or self.energy <= 0:
#             self.is_alive = False
#             print(f" {self.name} не выдержал сурововй жизни и покинул чат😈🤣")
#
#     def status(self):
#         alive_status = "Жив" if self.is_alive else "Мертв"
#         return f"{self.name} | Голод: {self.hunger} | Энергия: {self.energy} | {alive_status}"
#
#
# class Human(Sim):
#     def __init__(self, name, job):
#         super().__init__(name)
#         self.job = job
#         self.money = 50
#
#     def work(self):
#         if self.energy >= 30:
#             self.energy -= 30
#             self.hunger -= 20
#             self.money += 100
#             print(f" {self.name} сходил на работу ({self.job}) +100$. Энергия: {self.energy}")
#         else:
#             print(f" {self.name} слишком устал для работы!")
#
#     def feed_pet(self, pet):
#         if self.money >= 20:
#             print(f" {self.name} покупает корм и кормит {pet.name}...")
#             self.money -= 20
#             pet.eat()
#         else:
#             print(f" У {self.name} нет денег на корм! Иди работай тварь!")
#
#     def repair_robot(self, robot):
#         if self.energy >= 20:
#             print(f" {self.name} чинит {robot.name}...")
#             self.energy -= 20
#             robot.eat()  # Робот "ест" - заряжается
#             print(f" {robot.name} полностью заряжен!")
#         else:
#             print(f" {self.name} слишком устал для ремонта!")
#
# class Czigan(Sim):
#     def money(self, human):
#         print(f" {self.name} пришел и тебует деньги 10$")
#         print('дать?')
#         a = input()
#         if a == "да":
#             player.money -= 10
#             print("вы отдали 10$ цыганенку, он доволен")
#             b = 0
#         else:
#             print('вы прогнали цыганенка с крыльца, он будет мстить')
#             b = 2
#
#
# class Dog(Sim):
#     def eat(self):
#         self.hunger += 30
#         if self.hunger > 100:
#             self.hunger = 100
#         print(f" {self.name} жадно грызет кость! Гав!")
#
#     def play(self, human):
#         print(f" {self.name} приносит мячик {human.name}.")
#         self.energy += 10
#         if self.energy > 100:
#             self.energy = 100
#         human.energy += 10
#         if human.energy > 100:
#             human.energy = 100
#         print(f" {human.name} повеселел!")
#
#
# class Robot(Sim):
#     def __init__(self, name):
#         super().__init__(name)
#         self.energy = 100
#         self.hunger = 0
#
#     def live_day(self):
#         self.energy -= 5
#
#         if self.energy <= 0:
#             self.is_alive = False
#             print(f" {self.name} разрядился навсегда!")
#
#     def eat(self):
#         print(f" {self.name} подключается к розетке. Зарядка...")
#         self.energy = 100
#
#     def cook_dinner(self, human):
#         if self.energy > 20:
#             print(f" {self.name} готовит ужин для {human.name}.")
#             self.energy -= 20
#             human.eat()
#         else:
#             print(f" {self.name}: БАТАРЕЯ СЕЛА НЕ МОГУ ГОТОВИТЬ.")
#
#
# player = Human("Алекс", "Программист")
# doggo = Dog("Бобик")
# robo = Robot("Вертер-1000")
# household = [player, doggo, robo]
# day = 1
# rebenok = Czigan("цыган")
# print("Добро пожаловать в Sims: Python DLC")
# b = 0
# while True:
#     print(f"\n=== ДЕНЬ {day} ===")
#
#
#     game_over = False
#     for sim in household:
#         if not sim.is_alive:
#             print(f"GAME OVER: {sim.name} погиб.")
#             game_over = True
#     if game_over:
#         break
#
#     print(f" Деньги: {player.money}$")
#     for sim in household:
#         print(sim.status())
#     c = random.randint(1, 4 - b)
#     if c == 1:
#         rebenok.money(player)
#
#     print("\nЧто будет делать Алекс?")
#     print("1. Пойти на работу")
#     print("2. Поесть самому (-20$ еда)")
#     print("3. Покормить Бобика")
#     print("4. Поиграть с Бобиком")
#     print("5. Попросить робота приготовить ужин")
#     print("6. Починить робота")
#     print("0. Выход")
#     choice = input("Ваш выбор: ")
#
#     if choice == "1":
#         player.work()
#     elif choice == "2":
#         if player.money >= 20:
#             player.money -= 20
#             player.eat()
#         else:
#             print("Нет денег!")
#     elif choice == "3":
#         player.feed_pet(doggo)
#     elif choice == "4":
#         doggo.play(player)
#     elif choice == "5":
#         robo.cook_dinner(player)
#     elif choice == "6":
#         player.repair_robot(robo)
#     elif choice == "0":
#         print("Пока")
#         break
#     else:
#         print("Неверный выбор!")
#
#     print("\nНаступает ночь... Все показатели падают.")
#     time.sleep(1)
#
#     for sim in household:
#         sim.live_day()
#
#         if sim.hunger > 100:
#             sim.hunger = 100
#         if sim.energy > 100:
#             sim.energy = 100
#
#     day += 1
#
import time
import random

# --- 1. БАЗОВЫЙ КЛАСС (Основа для всех) ---
polytion_chance = 10


class Resident:

    def __init__(self, name):
        self.name = name
        self.hunger = 60
        self.energy = 80
        self.is_alive = True

    def status(self):
        return f"{self.name} | 🍗 Голод: {self.hunger} | ⚡️ Энергия: {self.energy}"

    def live_day(self):
        """Пассивное старение/усталость (базовая логика)"""
        self.hunger -= 15
        self.energy -= 15
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False

    def react_to_mess(self):
        """Пример полиморфизма: каждый житель по-разному реагирует на хлам"""
        pass


class WorkerSim(Resident):
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money

    def work(self):
        print(f'{self.name} ушел на заработки в Сибирь')
        self.money += 150
        self.energy -= 30
        self.hunger -= 20

    def react_to_mess(self):
        print(f'{self.name}: Как в свинарнике! -10 энергии')
        self.energy -= 10


class LazySim(Resident):
    def __init__(self, name):
        super().__init__(name)
        self.laziness = 100

    def live_day(self):
        self.hunger -= 5
        self.energy -= 5
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False

    def sleep_on_trash(self):
        print(f'{self.name} прилег на мусор')
        self.energy += 40
        self.hunger -= 5

    def react_to_mess(self):
        print(f'{self.name}: Какой мусор? Это моя кровать от гуччи')


worker = WorkerSim('работяга Петрович', 100)
lazy_guy = LazySim('Ларри (ленивец)')
roommates = [worker, lazy_guy]
day = 1
is_messy = True
print('СИМУЛЯТОР КОММУНАЛКИ ЗАПУЩЕН')

while True:
    print(f"\n=== День {day} ===")

    if not all(r.is_alive for r in roommates):
        dead = next(r for r in roommates if not r.is_alive)
        print(f"конец игры. {dead.name} покинул этот мир")

    print(f"Деньги Петровича: {worker.money} | Состояние: {'ХЛАМ' if is_messy else 'Чисто'}")
    for r in roommates:
        print(r.status())

    print('\n ВАШ ВЫБОР')
    print('1. Петрович: Пойти на работу (+150$)')
    print("2. Петрович: Купить пиццу на всех (-50$)")
    print("3. Ларри: Поспать в куче хлама (+энергия)")
    print("4. Ларри: Попросить у Петровича денег на еду")
    print("5. Убраться в комнате (Петрович теряет энергию)")
    print("0. Выход")
    choice = input('Действие: ')
    if choice == '1':
        worker.work()
    elif choice == '2':
        if worker.money >= 50:
            worker.money -= 50
            worker.energy += 50
            for r in roommates:
                r.hunger += 40

            print('Все поели')
        else:
            print('ноу мани')
    elif choice == '3':
        if is_messy:
            lazy_guy.sleep_on_trash()
        else:
            print('Хлама нет, сплю на полу')
            lazy_guy.energy += 10
    elif choice == '4':
        print(f'ларри клянчит деньги. Петрович в ярости.')
        worker.energy -= 5
    elif choice == '5':
        print('Петрович вынес весь мусор Лари')
        is_messy = False
        worker.energy -= 30
    elif choice == "0":
        break
    print('ночь в коммуналке')
    time.sleep(1)
    for r in roommates:
        r.live_day()
        if is_messy:
            r.react_to_mess()

    day += 1
print('игра завершена')
