import random
import re

# =============================
# 🔰 Base class for all characters
# =============================
class Global_Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
        # Attack type limits
        self.attack_items = {
            "critical": 2,
            "headshot": 3,
            "bodyshot": 4,
            "legshot": 3,
            "normal": float('inf')  # Normal attacks are unlimited
        }

        # Attack outcomes and their corresponding weapons
        self.outcomes = {
            "critical": "Laser Gun",
            "headshot": "holo grenade",
            "bodyshot": "AR",
            "legshot": "pistol",
            "normal": "melee"
        }

        # Damage associated with each weapon
        self.each_weapon_damage = {
            "Laser Gun": 100,
            "holo grenade": 50,
            "AR": 40,
            "pistol": 30,
            "melee": 10
        }

        # Player inventory to store earned weapons
        self.inventory = []

    # Check if character is still alive
    def is_alive(self):
        return self.hp > 0

    # Apply damage to character
    def take_damage(self, damage):
        self.hp -= damage

    # Main attack method
    def attack(self, target):
        def normal_attack():
            print(f"{self.name} attacks the enemy with base damage: 10")
            target.take_damage(10)
            self.add_inventory()

        # Ask user if they want to use a weapon from inventory or do a normal attack
        n = int(input(f"Your inventory has {self.inventory}\nAttack from inventory (1) or normal attack (0):"))

        if n == 1:
            if self.inventory:
                print("Your Inventory:")
                for idx, weapon in enumerate(self.inventory, 1):
                    print(f"{idx}. {weapon} (Damage: {self.each_weapon_damage[weapon]}) \n To cancel use 100")

                try:
                    user_choice = int(input("Select weapon by number: "))
                    selected_weapon = self.inventory[user_choice - 1]
                    damage = self.each_weapon_damage[selected_weapon]
                    print(f"{self.name} uses {selected_weapon} dealing {damage} damage!")
                    target.take_damage(damage)
                    self.inventory.remove(selected_weapon)
                except (ValueError, IndexError):
                    print("Invalid selection. Performing normal attack.")
                    normal_attack()
            else:
                print("Your inventory is empty.")
                normal_attack()
        else:
            normal_attack()

    # Adds a weapon to inventory based on random attack type
    def add_inventory(self):
        while True:
            attack = random.choice(list(self.attack_items.keys()))

            if attack == "normal":
                print(f"{self.name} did a {attack.upper()} attack. No loot earned.")
                break

            if self.attack_items[attack] > 0:
                weapon = self.outcomes[attack]
                self.inventory.append(weapon)
                self.attack_items[attack] -= 1
                print(f"{self.name} received: {weapon} from {attack.upper()} attack")
                break

# =============================
# 👤 Character subclass
# =============================
class Character(Global_Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)

# =============================
# 📄 Log writer
# =============================
def write_log(content):
    with open("game_log.txt", "a") as f:
        for c in content:
            f.write(f"->{c}\n")

# =============================
# ✅ Name validation input
# =============================
def get_valid_name(player_number):
    while True:
        name = input(f"Enter Player {player_number} name: ")
        if re.fullmatch(r"[A-Za-z]+", name):
            return name
        else:
            print("❌ Invalid name! Only letters are allowed. Please try again.")

# =============================
# 🕹️ Game setup and loop
# =============================
def start_game(attacker_1, attacker_2):
    attacker1 = Character(attacker_1, 200)
    attacker2 = Character(attacker_2, 200)

    print("\n🎮 Game Start!")
    print(f"{attacker1.name} vs {attacker2.name}")
    print(f"{attacker1.name} HP: {attacker1.hp}, {attacker2.name} HP: {attacker2.hp}")
    print("========================================")
    
    # Initial log entries
    write_log([f"{'='*7}End of the game{'='*7}",
               f"{'='*7}Game starts{'='*7}",
               f"{'='*7}{attacker1.name} vs {attacker2.name}{'='*7}"])

    turn = 0
    while attacker1.is_alive() and attacker2.is_alive():
        print(f"\n➡️  Turn {turn + 1}")
        write_log([f"Turn - {turn + 1}"])

        # Alternate turns
        if turn % 2 == 0:
            print(f"🎯 {attacker1.name}'s move")
            write_log([f"{attacker1.name}(hp:{attacker1.hp}) has attacked {attacker2.name}(hp:{attacker2.hp}) has inventory {attacker1.inventory}"])
            attacker1.attack(attacker2)
            print(f"🩸 {attacker2.name}'s HP: {attacker2.hp}")
        else:
            print(f"🎯 {attacker2.name}'s move")
            write_log([f"{attacker2.name}(hp:{attacker2.hp}) has attacked {attacker1.name}(hp:{attacker1.hp}) has inventory {attacker2.inventory}"])
            attacker2.attack(attacker1)
            print(f"🩸 {attacker1.name}'s HP: {attacker1.hp}")

        # Check for a winner after each attack
        if not attacker1.is_alive():
            print(f"\n💥 {attacker1.name} has been defeated!")
            print(f"🏆 {attacker2.name} wins the battle!")
            write_log([f"{attacker1.name} lost to {attacker2.name}"])
            break
        elif not attacker2.is_alive():
            print(f"\n💥 {attacker2.name} has been defeated!")
            print(f"🏆 {attacker1.name} wins the battle!")
            write_log([f"{attacker2.name} lost to {attacker1.name}"])
            break

        turn += 1

# =============================
# 🚀 Game Entry Point
# =============================
p1 = get_valid_name(1)
p2 = get_valid_name(2)
start_game(p1, p2)

    