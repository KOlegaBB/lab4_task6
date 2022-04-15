"""
Classes for game
"""


class Street:
    """
    Class for streets
    """

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.character = None
        self.item = None
        self.linked_streets = []
        self.task_point = False

    def set_description(self, description):
        """
        Set description of the street
        """
        self.description = description

    def link_street(self, street, direction):
        """
        Link street with another street in the given direction
        """
        self.linked_streets.append(tuple([street, direction]))

    def set_character(self, character):
        """
        Set character on the street
        """
        self.character = character

    def set_item(self, item):
        """
        Set item on the street
        """
        self.item = item

    def get_details(self):
        """
        Show information about street
        """
        print(self.description)
        print()
        for street in self.linked_streets:
            print(f"{street[0].name} в напрямку: {street[1]}")

    def get_character(self):
        """
        Get character from the street
        """
        return self.character

    def get_item(self):
        """
        Get item from the street
        """
        return self.item

    def set_task_point(self):
        """
        Set if this street is a task point
        """
        self.task_point = True

    def move(self, direction):
        """
        Return a street by chosen direction
        """
        for room in self.linked_streets:
            if room[1] == direction:
                return room[0]
        print(f"Немає вулиць в напрямку: {direction}")
        return self


class Character:
    """
    Class for characters
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = ""

    def set_conversation(self, conversation):
        """
        Set conversation with character
        """
        self.conversation = conversation

    def describe(self):
        """
        Show information about character
        """
        print(f"На вулиці хтось є!")
        print(f"{self.name}: {self.description}")

    def talk(self):
        """
        Print conversation with character
        """
        print(f"{self.name}: {self.conversation}")


class Enemy(Character):
    """
    Class for enemies, subclass of Character
    """

    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.health = health
        self.weapon = Weapon("2 Кулаки", "Стиснені разом пальці кисті рук", 1)

    def set_weapon(self, weapon):
        """
        Set weapon to the enemy
        """
        self.weapon = weapon

    def fight(self, player):
        """
        Fight with player
        """
        while self.health > 0 and player.health > 0:
            self.health -= player.weapon.damage
            player.health -= self.weapon.damage

    def describe(self):
        """
        Describe enemy
        """
        print(f"На вулиці хтось є!")
        print(f"{self.name}: {self.description}, він озброєний: "
              f"{self.weapon.name}, атака: {self.weapon.damage}")


class Friend(Character):
    """
    Class for friends, subclass of Character
    """

    def __init__(self, name, description, gift):
        super().__init__(name, description)
        self.gift = gift

    def get_gift(self):
        """
        Get a gift from friend
        """
        return self.gift


class Item:
    """
    Class for items
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        """
        Describe item
        """
        print(f"На цій вулиці щось є!")
        print(f"{self.name}: {self.description}")


class Weapon(Item):
    """
    Class for weapons, subclass of Item
    """

    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def describe(self):
        """
        Describe weapon
        """
        print(f"На цій вулиці щось є!")
        print(f"{self.name}: {self.description}. Атака: {self.damage}")


class Heal(Item):
    """
    Class for heal, subclass of Item
    """

    def __init__(self, name, description, heal):
        super().__init__(name, description)
        self.heal = heal

    def heal_me(self, player):
        """
        Heal character
        """
        player.health += self.heal

    def describe(self):
        """
        Describe heal
        """
        print(f"На цій вулиці щось є!")
        print(f"{self.name}: {self.description} Лікування: {self.heal}")


class Player:
    """
    Class for player
    """

    def __init__(self):
        self.health = 50
        self.weapon = Weapon("2 Кулаки", "Стиснені разом пальці кисті рук", 1)

    def info(self):
        """
        Show information about player, current weapon and hp
        """
        print(f"Поточна зброя: {self.weapon.name}, "
              f"{self.weapon.description} Атака: {self.weapon.damage}")
        print(f"Поточне здоров'я: {self.health}")
