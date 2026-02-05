# def u# def get_factors(num):
#   factors = []
#   for i in range(1, num + 1):
#          if num % i == 0:
#           factors.append(i)
#    return factors
#
# def a(x1,y1,x2,y2):
#     b = (x1 + x2) / 2
#     c = (y1 + y2) / 2
#     return b,c
# print(a(0,0,10,0))
#
# def c(a,b):
#     v = []
#     for i in range(len(a)):
#         if b in a[i]:
#             v.append(i)
#     return v
# print(c('abcdabcaaa',  'a'))
# print(c('abcabcaaa',  'e'))
# print(c('abcadbcaaa',  'd'))
# def a(b,c):
#    v =[]
#    b.extend(c)
#    for i in range(len(b)):
#        v.append(min(b))
#        b.remove(min(b))
#    return v
# print(a([1, 2, 3],[5, 6, 7, 8]))
# print(a([1, 7, 10, 16], [5, 6, 13, 20]))
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 57, 48, 53, 65, 70, 81, 84, 84, 90]
# list3 = quick_merge(list1, list2)
# print(list3)
# class Cat:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#             return f"{self.name} бррррррр "
# my_cat = Cat('alah')
# print(my_cat.speak())
# my_cat.name = 'обрыган'
# print(my_cat.name)
# class Zombie:
#     def __init__(self,name):
#       self.name = name
#       self.health = 50
# z1 = Zombie("Тупой")
# print(z1.name)
# print(z1.health)


# class Zombie:
#     def __init__(self,name):
#         self.name = name
#         self.health = 100
#     def growl(self):
#             return f"{self.name} говорит: ам ам ам "
# z1 = Zombie("Тупой")
# print(z1.growl())
# print("🎮=== БИТВА ГЕЕВ ===\n")
# class Character:
#     def __init__(self, name, health=100, max_health=None, damage=20):
#         self.name = name
#         self.health = health
#         self.max_health = max_health or health
#         self.damage = damage
#
#     def status(self):
#         percent = (self.health / self.max_health) * 100
#         return f"⚔ {self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%) | Урон: {self.damage}!"
#     def attack(self, target):
#            return f"⚔ {self.name} бьет {target.name} на {self.damage}!"
#     def take_damage(self, damage):
#         self.health -= damage
#         if self.health < 0:
#             self.health = 0
#         return f"😈 {self.name} получил {damage} урона! Осталось: {self.health} HP"
#     def is_alive(self):
#         return self.health > 0
# class Enemy:
#     def __init__(self,name, health=60, damage=15):
#         self.name = name
#         self.health = health
#         self.damage = damage
#         self.max_health = health
#     def status(self):
#         percent = (self.health / self.max_health) * 100
#         return f"🧟 {self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%) | Урон: {self.damage}"
#     def attack(self, target):
#         return f"⚔ {self.name} бьет {target.name} на {self.damage}!"
#     def take_damage(self, damage):
#         self.health -= damage
#         if self.health < 0:
#              self.heath = 0
#         return f"💀 {self.name} получил {damage}! Осталось: {self.health} HP"
#
#     def is_alive(self):
#         return self.health > 0
#
# print("🏛 СОБИРАЕМ ГЕЕВ ПО ЧЕРТЕЖАМ...\n")
# hero = Character("🛡 Шнеля", 120, damage=25)
# daun = Enemy("👹 Квадробер", 50, 12)
# boss = Enemy("🤦🤡👹‍ ЖЕНЩИНА", 200, 30)
#
# army = [hero, daun, boss]
#
# print("😝 СОСТАВ ГЕЕВ:")
# for unit in army:
#      print(unit.status())
#
# print("\n" + "="*50 + "\n")
#
# def battle_round(attacker, defender):
#     """Один раунд боя"""
#     print(f"\n🦞 РАУНД БОЯ:")
#     print(attacker.status())
#     print(attacker.status())
#
#     print(attacker.attack(defender))
#     print(defender.take_damage(attacker.damage))
#
#     print(defender.status())
#     print("-"*30)
#
# print("⚔ НАЧИНАЕТЬСЯ БИТВА!\n")
#
# battle_round(daun, hero)
# battle_round(hero, daun)
# battle_round(boss, hero)
# battle_round(hero, boss)
#
# print("\n" + "="*50 + "\n")
#
# print("🤦‍♂ ИТОГ БИТВЫ:")
# for unit in army:
#     status = unit.status()
#     if not unit.is_alive():
#         status += " 🤡ЗДОХ"
#     print(status)
#
# print("\n === Конец демонстрации ООП ===\n")
# print(" Классы = чертежи")
# print(" Обьекты = фигурки")
# print(" Методы = умения")
# print(" Атрибуты =  характеристики (урон, здоровье)")
# print(" Готово к уроку - тесттировано!")
# print(" текствовое рпг про захватчиков других планет (Warhammer) но это HElldivers хелдыйверы встречают противников котоыре мешают захватить планеты")
# # print(" (1: Helldiver A1  2: helldiver Y2 3: helldiver b4) хорошие захватчики ")
# # print(" (33876 батальон Автаматонов) считаеться как один герой")
# class Sim:
#     def __init__(self, name, home, job):
#         self.name = name
#         self.energy = 50
#         self.money = 100
#         self.home = home
#         self.job = job
#
#     def eat(self):
#         print(f"{self.name} ест")
#         self.energy += 10
#         self.money -= 5
#
#     def show_status(self):
#         print("------")
#         print(f"Имя: {self.name}")
#         print(f"Энергия: {self.energy}")
#         print(f"Деньги: {self.money}")
#
#
# class Home:
#     def __init__(self, name):
#         self.name = name
#
#     def sleep(self, sim):
#         print(f"{sim.name} спит в доме {self.name}")
#         sim.energy += 20
#
#
# class Job:
#     def __init__(self, title, salary):
#         self.title = title
#         self.salary = salary
#
#     def work(self, sim):
#         print(f"{sim.name} работает как {self.title}")
#         sim.money += self.salary
#         sim.energy -= 15
#
#
# if __name__ == "__main__":
#     # Создаем объекты
#     home = Home("Уютный дом")
#     job = Job("Программист", 50)
#
#     sim = sim("Bob", home, job)
#
#     sim.show_status()
#
#     sim.job.work(sim)
#     sim.home.sleep(sim)
#     sim.eat()
#
#     sim.show_status()
class Sim:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.if_alive = True
    def eat(self):
        if self.hunger >= 100:
            print(f"{self.name} не хочет есть")
        else:
            self.hunger += 20
            self.energy -= 5
            print(f" 🐱‍🐉 {self.name} поел(а). Голод: {self.hunger}")
