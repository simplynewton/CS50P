import random
import time

class Character:
    def __init__(self, hp, gold, attack_power, armor, potions):
        self.hp = hp
        self.gold = gold
        self.attack_power = attack_power
        self.armor = armor
        self.potions = potions
        self.fire_bombs = 0
        self.perks = []

    def attack(self, enemy):
        damage = max(0, self.attack_power - enemy.armor)
        enemy.hp -= damage
        print(f"\nYou slashed the {enemy.name} and dealt {damage} damage!")
        if enemy.hp <= 0:
            print(f"\nThe {enemy.name} has been defeated!")

    def use_potion(self):
        if self.potions > 0:
            self.hp = min(100, self.hp + 20)
            self.potions -= 1
            print(f"\nYou used a Healing Potion. Your HP is now {self.hp}.")
        else:
            print("\nYou don't have any Healing Potions left!")

    def use_fire_bomb(self, enemy):
        if self.fire_bombs > 0:
            damage = 20
            enemy.hp -= damage
            print(f"\nYou used a Fire Bomb. It dealt {damage} damage to the {enemy.name}!")
            self.fire_bombs -= 1
        else:
            print("\nYou don't have any Fire Bombs left!")

    def check_stats(self):
        print(f"\n--- Stats ---\nHP: {self.hp}\nGold: {self.gold}\nAttack Power: {self.attack_power}\nArmor: {self.armor}\nHealing Potions: {self.potions}\nFire Bombs: {self.fire_bombs}\nPerks: {', '.join(self.perks) if self.perks else 'None'}")

    def buy_item(self, item, cost):
        if self.gold >= cost:
            self.gold -= cost
            item.apply(self)
            print(f"\nYou bought {item.name} for {cost} gold.")
        else:
            print("\nYou don't have enough gold!")

    def flee(self):
        print("\nYou fled the dungeon and returned to the surface. You are fully healed and ready to try again.")
        self.hp = 100  # Fully heal the player
        return True

class Enemy:
    def __init__(self, name, hp, attack_power, armor):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.armor = armor

    def attack(self, player):
        damage = max(0, self.attack_power - player.armor)
        player.hp -= damage
        print(f"\nThe {self.name} attacked you and dealt {damage} damage!")

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply(self, player):
        self.effect(player)

# Shop Items
def healing_potion_effect(player):
    player.potions += 1

def sword_upgrade_effect(player):
    player.attack_power += 5

def armor_upgrade_effect(player):
    player.armor += 2

def fire_bomb_effect(player):
    player.fire_bombs += 1

def unlock_perk_effect(player):
    perk = "Custom Perk"  # Placeholder for an actual perk
    player.perks.append(perk)
    print(f"\nYou unlocked a new perk: {perk}!")

healing_potion = Item("Healing Potion", healing_potion_effect)
sword_upgrade = Item("Sword Upgrade", sword_upgrade_effect)
armor_upgrade = Item("Light Armor", armor_upgrade_effect)
fire_bomb = Item("Fire Bomb", fire_bomb_effect)
unlock_perk = Item("Unlock Perk", unlock_perk_effect)

shop_items = [
    (healing_potion, 20),
    (sword_upgrade, 30),
    (armor_upgrade, 40),
    (fire_bomb, 25),
    (unlock_perk, 50)
]

def show_shop(player):
    while True:
        print("\n--- Welcome to the Shop! ---")
        for i, (item, cost) in enumerate(shop_items, 1):
            print(f"{i}. {item.name} - {cost} Gold")
        print("6. Leave the Shop")

        choice = int(input("\nChoose an item to buy (1-6): "))
        if 1 <= choice <= 5:
            player.buy_item(shop_items[choice - 1][0], shop_items[choice - 1][1])
        elif choice == 6:
            print("\nYou leave the shop.")
            break
        else:
            print("\nInvalid choice!")

def combat(player, enemy):
    while enemy.hp > 0 and player.hp > 0:
        print(f"\n--- Combat ---\nYour HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
        print("\nChoose your action:")
        print("1. Slash")
        print("2. Use Healing Potion")
        print("3. Use Fire Bomb")
        print("4. Check Stats")
        print("5. Flee")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            player.attack(enemy)
            if enemy.hp > 0:
                enemy.attack(player)
        elif choice == 2:
            player.use_potion()
            if enemy.hp > 0:
                enemy.attack(player)
        elif choice == 3:
            player.use_fire_bomb(enemy)
            if enemy.hp > 0:
                enemy.attack(player)
        elif choice == 4:
            player.check_stats()
        elif choice == 5:
            if player.flee():
                return False
        else:
            print("\nInvalid choice!")

        if player.hp <= 0:
            print("\nYou have been defeated. Game over.")
            return False

    return True

def goblin_encounter(player):
    goblin = Enemy("Goblin Grunt", 30, 5, 0)
    print("\nYou enter a dimly lit chamber, and a Goblin Grunt leaps out, brandishing a rusty dagger!")
    print(f"\n--- Encounter ---\nYour HP: {player.hp} | Goblin Grunt HP: {goblin.hp}")
    return combat(player, goblin)

def goblin_warrior_encounter(player):
    warrior = Enemy("Goblin Warrior", 50, 8, 0)
    print("\nDeeper in the dungeon, a Goblin Warrior awaits with a wicked grin, ready for battle!")
    print(f"\n--- Encounter ---\nYour HP: {player.hp} | Goblin Warrior HP: {warrior.hp}")
    return combat(player, warrior)

def orc_warchief_encounter(player):
    orc = Enemy("Orc Warchief", 100, 15, 0)
    print("\nIn the final chamber, the fearsome Orc Warchief stands tall, ready to crush you!")
    print(f"\n--- Encounter ---\nYour HP: {player.hp} | Orc Warchief HP: {orc.hp}")
    return combat(player, orc)

def random_encounter(player):
    print("\nYou stumble into a hidden trap!")
    player.hp -= 15
    print(f"You lost 15 HP. Your HP is now {player.hp}.")

def main():
    print("Welcome, Adventurer, to the Goblin Gauntlet!")
    print("A dark and twisted labyrinth awaits you, filled with danger, treasure, and foes.")
    print("Your journey begins now. Can you survive the dungeon and defeat the Orc Warchief?")

    player = Character(hp=100, gold=50, attack_power=10, armor=0, potions=0)

    difficulty = input("\nChoose your difficulty level (Easy, Normal, Hard): ").lower()
    if difficulty == "easy":
        player.hp = 120
        player.gold += 20
    elif difficulty == "hard":
        player.hp = 80

    while True:
        # Stage 1: Goblin Grunt
        if goblin_encounter(player):
            player.gold += 10
            print(f"\nVictory! You earned 10 Gold. Current Gold: {player.gold}")
        else:
            continue

        # Shop
        show_shop(player)

        # Stage 2: Goblin Warrior
        if goblin_warrior_encounter(player):
            player.gold += 20
            print(f"\nVictory! You earned 20 Gold. Current Gold: {player.gold}")
        else:
            continue

        # Random Encounter
        if random.choice([True, False]):
            random_encounter(player)

        # Final Stage: Orc Warchief
        if orc_warchief_encounter(player):
            print("\nCongratulations! You have defeated the Orc Warchief and completed the Goblin Gauntlet!")
            break
        else:
            continue

if __name__ == "__main__":
    main()
