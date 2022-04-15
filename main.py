"""
Game
"""
from labs.lab_2_4.task_6.game import *


def main():
    """
    Whole game
    """
    patyk = Weapon('Патик', 'Ним добре бити когось', 3)
    kropyva = Weapon('Кропива', 'Ай, печеться!', 5)
    katana = Weapon('Катана', 'Як вона тут опинилась?', 8)
    javelin = Weapon('Джавелін',
                     'Британський переносний зенітно-ракетний комплекс', 50)
    rozochka = Weapon('Розочка', 'Розбита скляна бутилка', 4)
    knife = Weapon('Ножик', 'Ним можна нарізати моркву', 6)
    velichie = Weapon('Русское величие', 'Нічого з себе не представляє', 0)

    bun = Heal("Надкушена булочка", "Досі апетитна", 5)
    pill = Heal("Таблетка від всіх болячок", "Лікує від всього", 10)
    zakladka = Heal("Закладка", "Не для книжки", 25)

    kavaler = Friend("Кавалєр", "Красунчик з цієї вулиці, у нього щось є", bun)
    kavaler.set_conversation("Хоч булку, мені не сподобалась")
    volunteer = Friend("Волонтер", "За легендою може наволонтерити будь-що",
                       javelin)
    volunteer.set_conversation("Тобі щось треба? Зараз пошукаю")
    student = Character("Бідний студент", "Нічого не має")
    student.set_conversation("Щось потрібно? Ось тобі нічого! Не дякуй...")
    laydak = Character("Лайдак", "Вбога людина")
    laydak.set_conversation("...И если бы за шесть часов до операции не был "
                            "нанесен превентивный удар по позициям...")
    lotr = Enemy("Лотр", "Негідник, розбійник, грабіжник, ще й наривається", 5)
    lotr.set_conversation("Гони бабки, ботан.")
    zbuy = Enemy("Збуй", "Розбійник, грабіжник, наркоман, пр...", 25)
    zbuy.set_weapon(rozochka)
    zbuy.set_conversation("<Страхітливо мовчить>")
    batyar = Enemy("Батяр", "Місцевий алкаш, в душі романтик", 40)
    batyar.set_weapon(knife)
    batyar.set_conversation("Життя таке бентежне...")
    moskal = Enemy("Москаль", "Просто москаль хоче бути побитим", 1)
    moskal.set_weapon(velichie)
    moskal.set_conversation('При чем тут я, это все путин')

    franko = Street("вул. Івана Франка")
    franko.set_description("Довга простора вулиця")
    rynok_sq = Street("Площа ринок")
    rynok_sq.set_description("Площа з пам'ятником Шевченку")
    rynok_sq.set_character(student)
    rynok_sq.set_item(patyk)
    zaliznychna = Street("вул. Залізнична")
    zaliznychna.set_description("Вулиця, що прямує до вокзалу")
    zaliznychna.set_character(volunteer)
    bili = Street("Білі Казарми")
    bili.set_description("Північно-східна частина міста")
    bili.set_character(lotr)
    bili.set_item(kropyva)
    golden = Street("вул. Золота")
    golden.set_description("Центральна вулиця міста")
    golden.set_character(kavaler)
    january_22 = Street("вул. 22 Січня")
    january_22.set_description("Просто вулиця")
    january_22.set_character(zbuy)
    january_22.set_item(pill)
    lesi = Street("вул. Лесі Українки")
    lesi.set_description("Вулиця, що прямує до стадіону")
    lesi.set_character(laydak)
    lesi.set_item(katana)
    park = Street("Майдан Свободи")
    park.set_description("Парк в центрі міста")
    park.set_character(batyar)
    park.set_item(zakladka)
    filvarky = Street("Великі Фільварки")
    filvarky.set_description("Передмістя Бродів")
    filvarky.set_character(moskal)

    franko.link_street(rynok_sq, "north")
    rynok_sq.link_street(franko, "south")
    franko.link_street(bili, "west")
    bili.link_street(franko, "east")
    rynok_sq.link_street(zaliznychna, "north")
    zaliznychna.link_street(rynok_sq, "south")
    rynok_sq.link_street(golden, "west")
    golden.link_street(rynok_sq, "east")
    zaliznychna.link_street(january_22, "west")
    january_22.link_street(zaliznychna, "east")
    january_22.link_street(filvarky, "west")
    filvarky.link_street(january_22, "east")
    january_22.link_street(golden, "south")
    golden.link_street(january_22, "north")
    filvarky.link_street(park, "south")
    park.link_street(filvarky, "north")
    park.link_street(golden, "east")
    golden.link_street(park, "west")
    park.link_street(lesi, "south")
    lesi.link_street(park, "north")
    lesi.link_street(bili, "east")
    bili.link_street(lesi, "west")
    bili.link_street(golden, "north")
    golden.link_street(bili, "south")

    filvarky.task_point = True
    player = Player()
    current_street = franko
    previous_street = ""
    dead = False
    completed_tasks = 0

    print("Вітаю в Бродах!")
    print("Тут казали люди, що на Великих Фільварках бачили москаля!!!")
    print("Розберись з цим!")
    print()
    print("north, east, south, west - піти в якомусь з цих напрямків")
    print("talk - поговорити з місцевим")
    print("info - інформація про гравця")
    print("take - взяти предмет")
    print("gift - взяти предмет від доброзичливого місцевого")
    print("fight - битись з ворогом")
    print("back - втікти від ворога")
    while not dead:

        print("\n")

        if completed_tasks == 2:
            print("Вітаю, ти переміг!")
            break

        print(current_street.name)
        current_street.get_details()

        inhabitant = current_street.get_character()
        if inhabitant is not None:
            print()
            inhabitant.describe()
            if isinstance(inhabitant, Enemy):
                print("Тобі прийдеться з ним битись, або можеш втекти.")

                command = input("> ")

                if command == "back":
                    current_street = current_street.move(previous_street)
                    continue
                elif command == "talk":
                    inhabitant.talk()
                    continue
                elif command == "fight":
                    inhabitant.fight(player)
                    if player.health <= 0:
                        dead = True
                        print("На жаль, ти програв цей бій...")
                        continue
                    elif inhabitant.health <= 0:
                        current_street.character = None
                        print(f"Ти переміг {inhabitant.name}!")
                        print(f"Тепер твоє здоров'я становить: "
                              f"{player.health}")
                        continue
                elif command == "info":
                    player.info()
                    continue
                else:
                    print("Я не знаю команди " + command)
                    continue
        if current_street.task_point:
            current_street.task_point = False
            completed_tasks += 1
            if current_street != franko:
                franko.task_point = True
                print()
                print("Тепер вернись до дому на вулиці Івана Франка")
            else:
                continue
        item = current_street.get_item()
        if item is not None:
            print()
            item.describe()

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            current_street = current_street.move(command)
            if command == "north":
                previous_street = "south"
            elif command == "south":
                previous_street = "north"
            elif command == "west":
                previous_street = "east"
            elif command == "east":
                previous_street = "west"
        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "gift":
            if isinstance(inhabitant, Friend):
                if isinstance(inhabitant.gift, Weapon):
                    changed_item = player.weapon
                    player.weapon = inhabitant.get_gift()
                    inhabitant.gift = changed_item
                    print(f"Ти поміняв {changed_item.name} на "
                          f"{player.weapon.name}")
                    player.info()
                elif isinstance(inhabitant.gift, Heal):
                    inhabitant.gift.heal_me(player)
                    print(f"Ти полікувався на {inhabitant.gift.heal}")
                    player.info()
                    inhabitant.gift = None
                else:
                    print(f"{inhabitant.name}: Я не маю, що тобі дати(")
            else:
                print("Тут когось, хто міг би тобі щось дати.")
        elif command == "take":
            if item is not None:
                if isinstance(item, Weapon):
                    changed_item = player.weapon
                    player.weapon = item
                    current_street.item = changed_item
                    print(f"Ти поміняв {changed_item.name} на "
                          f"{player.weapon.name}")
                    player.info()
                elif isinstance(item, Heal):
                    item.heal_me(player)
                    print(f"Ти полікувався на {item.heal} одиниці")
                    player.info()
                    current_street.item = None
            else:
                print("Тут нічого немає!")
        elif command == "info":
            player.info()
        else:
            print("Я не можу виконати команду " + command)


if __name__ == "__main__":
    main()
