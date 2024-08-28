import random
import json
class Player():
    def __init__(self, hp, attack, mana, coins):
        self.hp = hp
        self.attack = attack
        self.mana = mana
        self.coins = coins
        self.skills = []
        self.artifacts = []

    def add_artifact(self, artifact):
        self. artifacts.append(artifact)
        self.hp += artifact.hp_boost
        self.attack += artifact.attack_boost
        self.mana += artifact.mana_boost

    def add_skill(self, skill):
        self.skills.append(skill)

    def dict(self):
        return{
            "hp": self.hp,
            "attack": self.attack,
            "mana":self.mana,
            "coins":self.coins,
            "skills":[(skill.name, skill.damage, skill.mana_cost) for skill in self.skills],
            "artifacts":[(artifact.name, artifact.hp_boost, artifact.hp_boost, artifact.attack_boost, artifact.mana_boost) for artifact in self.artifacts]
        }
    def from_dict(data):
        player = Player(hp=data["hp"], attack = data["attack"], mana = data["mana"], coins = data["coins"])
        for skill_data in data["skills"]:
            player.add_skill(Skill(*skill_data))
        for artifact_data in data["artifacts"]:
            player.add_artifact(Artifact(*artifact_data))
        return player

class Goblin:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

class Artifact:
     def __init__(self, name, hp_boost=0, attack_boost=0, mana_boost=0):
        self.name=name
        self.hp_boost = hp_boost
        self.attack_boost = attack_boost
        self.mana_boost = mana_boost

class Skill:
     def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
def save_game(player, stage):
    save_data = {
        "player": player.dict(),
        "stage": stage
    }
    with open("savegame.json", "w") as sf:
        json.dump(save_data, sf)
    print("Game saved successfully.")

def load_game():
    try:
        with open("savegame.json", "r") as sf:
            save_data = json.load(sf)
            player = Player.from_dict(save_data["player"])
            stage = save_data["stage"]
            print("Game loaded siccessfilly.")
            return player, stage
    except FileNotFoundError:
        print("No saved game found.")
        return None, None

def battle(player, goblin):
    while player.hp >0 and goblin.hp >0:
        print(f"\npPlayer HP: {player.hp}, Mana: {player.mana}, Gobline HP: {goblin.hp}")
        action = input("Choose an action (attack/skill): ").lower()

        if action == "attack" or action == "atk" or action == "a":
            goblin.hp -= player.attack

        elif action == "skill" or action == "s" and player.skills:
            print("choose a skill:")
            for i, skill in enumerate(player.skills):
                print(f"{i+1}.{skill.name} (Damage: {skill.damage}, Mana Cost: {skill.mana_cost})")
            skill_choice = int(input("Choose skill number: "))-1
            skill = player.skills[skill_choice]

            if player.mana>= skill.mana_cost:
                player.mana-= skill.mana_cost
                goblin.hp -= skill.damage
                print(f"You used {skill.name} for {skill.damage} damage. Mana left: {player.mana}")
            else:
                print("Not enough mana!")
        else:
            print("Invalid action or no skills available.")
            continue
        if goblin.hp > 0:
            player.hp -= goblin.attack
            print(f"The goblin attacked you for {goblin.attack} damage.")
        else:
            print("You were defeated by the goblin...")
            return "lose"
def visit_shop(player):
    print("Welcome to the shop! You have", player.coins, "coins.")
    print("1. Buy Health Potion (+20 HP) - 10 coins")
    print("2. Buy Sword (+5 Attack) - 15 coins")
    print("3. Buy Mana Potion (+20 Mana) - 10 coins")
    print("4. Leave Shop")

    choice = input("Choose an option: ")

    if choice =="1" and player.coins>=10:
        player.hp += 20
        player.coins -= 10
        print("You bought a Health Potion!")
    elif choice == "2" and player.coins >= 15:
        player.attack += 5
        player.coins -=15
        print("You bought a Mana Potion!")
    elif choice == "4":
        print("You left the shop.")
    else:
        print("Invalid choice or not enough coins.")
    return player

def cpath():
    print("\nChoose your path:")
    print("1. Battle")
    print("2. Shop")
    print("3. Event")

    choice = input("Enter a number: ")

    if choice == "1":
        return "battle"
    elif choice == "2":
        return "shop"
    elif choice == "3":
        return "event"
    else:
        print("Invalid choice. Defaulting to battle.")
        return "battle"
def main():
    choice = input("Would you like to start new(1) or load previous save(2)?")
    if choice == "2":
        player, stage = load_game()
        if player is None:
            player = Player(hp = 100, attack = 10, mana = 50, coins = 0)
            stage = 1
    else:
            player = Player(hp = 100, attack = 10, mana = 50, coins = 0)
            stage = 1
    stages = 5
    for current_stage in range(1, stages+1):
        print(f"\nStage{current_stage}:")
        path = cpath()

        if path == "battle":
            goblin = Goblin(hp=30+stage*10, attack = 5+stage*2)
            result = battle(player, goblin)
            if result == "lose":
                print("Game Over!")
                return
            player.coins +=10*stage
        elif path == "shop":
           player = visit_shop(player)
        elif path == "event":
            print("You found a hidden artifact!")
            artifact = Artifact(name ="Amulet of Wisdom", hp_boost= 10, attack_boost=3, mana_boost = 20)
            player.add_artifact(artifact)
            print(f"You obtained {artifact.name} (+{artifact.hp_boost} HP, +{artifact.attack_boost} Attack, +{artifact.mana_boost} Mana)")
    print("\nFinal Boss: The Hobo Goblin!")
    hobo_goblin = Goblin(hp=3 * 100, attack=3 * 10)
    final_result = battle(player, hobo_goblin)
    if final_result == "win":
        print("Congratulations! You defeated the Hobo Goblin and won the game!")
    else:
        print("The Hobo Goblin was too strong. Better luck next time!")

if __name__ == "__main__":
    main()
