import pytest
from project import Character, Enemy, Item, shop_items

@pytest.fixture
def player():
    return Character(hp=100, gold=50, attack_power=10, armor=0, potions=0)

@pytest.fixture
def goblin():
    return Enemy(name="Goblin Grunt", hp=30, attack_power=5, armor=0)

@pytest.fixture
def orc_warchief():
    return Enemy(name="Orc Warchief", hp=100, attack_power=15, armor=0)

def test_character_initial_stats(player):
    assert player.hp == 100
    assert player.gold == 50
    assert player.attack_power == 10
    assert player.armor == 0
    assert player.potions == 0
    assert player.fire_bombs == 0
    assert player.perks == []

def test_enemy_initial_stats(goblin):
    assert goblin.name == "Goblin Grunt"
    assert goblin.hp == 30
    assert goblin.attack_power == 5
    assert goblin.armor == 0

def test_player_attack(player, goblin):
    player.attack(goblin)
    assert goblin.hp == 20

def test_enemy_attack(player, goblin):
    goblin.attack(player)
    assert player.hp == 95

def test_use_healing_potion(player):
    player.hp = 50
    player.potions = 1
    player.use_potion()
    assert player.hp == 70
    assert player.potions == 0

def test_buying_item(player):
    # Test buying a healing potion
    item = shop_items[0][0]  # Healing Potion
    cost = shop_items[0][1]  # 20 Gold
    player.buy_item(item, cost)
    assert player.potions == 1
    assert player.gold == 30

    # Test buying a fire bomb
    item = shop_items[3][0]  # Fire Bomb
    cost = shop_items[3][1]  # 25 Gold
    player.gold = 30  # Reset gold for testing
    player.buy_item(item, cost)
    assert player.fire_bombs == 1
    assert player.gold == 5

def test_flee(player):
    player.hp = 50
    result = player.flee()
    assert player.hp == 100  # Player is fully healed
    assert result is True
