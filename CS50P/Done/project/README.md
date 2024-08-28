# Goblin Gauntlet
#### Video Demo: https://youtu.be/jOW462EztMo
#### Description:
Goblin gauntlet is a text-based dungeon crawler game designed to be a fun way to test your wits through combat and stragetic planning.
The players are set in a dark and twisted labyrith trying to advance through different stages of a dungeon.
The ultimate goal of game is to beat this dungeon's trial and defeat the Orc Warchief

### Project Overview
In Goblin Gauntlet, the player becomes an adventurer trying to navigate through this dungeon.
The game has a variety of mechanics including combat, item usage, and encounters with enemies.
As the player progesses, the enemy faced becomes increasingly stronger.

### Game Features
1. **Character Stats**: Players start with 100 HP, 50 Gold, an Attack Power of 10, and no Armor or Healing Potions.
These stats are changed based on the selected difficulty, and other actions taken with in game such as being healed,
taking damage and upgrading the player's weapon.

2. **Turn-Based Combat**: The game uses a turn-based system where the player goes first.
The player is able to select 4 options, attack, heal, special equipment or flee.

3. **Encounters**: Each stage presents a stronger and stronger enemy.
Encounters include Goblin Grunts, Goblin Warriors, and the final boss, the Orc Warchief.

4. **Shop Mechanics**: Players can visit a shop to buy items such as Healing Potions, Sword Upgrades, Light Armor, Fire Bombs, and Perks.
The shop allows the players to purchase items multiple times.

5. **Perks System**: Perks serve as an additional buff for the players, enhancing the players stats.

6. **Random Trap Encounters**: The player has a chance to accidentally trigger an trap while advancing to the next stage causing player's to lose health.

7. **Combat System**: During combat both the player's and enemy's hp is displayed before each move. This is to make the game feel smoother and allows players to descide what to do with their next turn.

8. **Item Use**: Certain items bought from are comsumables such as healing potions and firebombs. These tiems provide different uses and gives the player's an edge during battles
- fire bomb deals damage over time
- healing potions heal 20 hp

9. **Flee Mechanic**: If the player choses to flee during combat, they return to the surface allowing them to keep their stats and items.
They are fully healed and the game restarts from Stage 1. This mechanic is only used for those realizes they can't beat it first try (DO BETTER LOL)

10. **Shop**: The shop sells players different items for gold. Players earn gold from beating up enemies and are used to buy various upgrades and items in the shop.

shop_items = [
    (healing_potion, 20),
    (sword_upgrade, 30),
    (armor_upgrade, 40),
    (fire_bomb, 25),
    (unlock_perk, 50)
]

11. **Stats Display**: This allows players to see their stats including health, how much damage they do, how many items they have of each comsumable, and perks.(for a better experience)

### Code Breakdown
1. **`Character` Class**:
   - Defines the player's attributes such as health, gold, attack power, armor, and potions.
   - It also includes the method (the game features) for attacking enemies, using potions, buying items, and fleeing from combat.

2. **`Enemy` Class**:
   - Represents different enemies with attributes such as name, health, attack power, and armor.
   - includes only the methods of attacking the player.

3. **`Item` Class**:
   - Handles items that can be bought from the shop and their effects on the player.
   - Healing potions, sword upgrades, and fire bombs.

4. **Game Functions**:
   - **`show_shop()`**: Displays available items in the shop and handles the purchasing process.
   - **`combat()`**: Manages the combat between the player and an enemy, including player and enemy actions.
   - **`goblin_encounter()`, `goblin_warrior_encounter()`, `orc_warchief_encounter()`**: Handle specific enemy encounters with descriptive environmental setups.
   - **`random_encounter()`**: Simulates a random trap encounter with the player.
   - **`main()`**: Initializes the game, handles player choices, and progresses through the dungeon stages.
