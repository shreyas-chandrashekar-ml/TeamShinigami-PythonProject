# TeamShinigami-PythonProject

# ⚔️ Two-Player Weapon Battle Game

This is a simple terminal-based two-player battle game in Python. Each player takes turns attacking the other with randomly earned weapons to reduce the opponent's HP to zero and win the match.

---

## 📖 Table of Contents

- [Features](#-features)
- [Gameplay](#-gameplay)
- [Weapons and Damage](#-weapons-and-damage)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Example Gameplay](#-example-gameplay)
- [Game Log](#-game-log)
- [Notes](#-notes)
- [License](#-license)

---

## 🚀 Features

✅ Two-player turn-based gameplay  
✅ Random weapon looting on attacks  
✅ Weapon-specific damage mechanics  
✅ Player inventory management  
✅ Input validation for player names  
✅ Automatic game logging to `game_log.txt`

---

## 🕹️ Gameplay

1. Run the game script.
2. Enter valid player names (only letters are allowed).
3. Players take turns to attack:
   - Choose to attack with a weapon from inventory (if available) or perform a normal melee attack.
   - Weapons deal different damage and are consumed upon use.
4. The game continues until one player’s HP reaches zero. The winner is announced.

---

## 🔫 Weapons and Damage

| Attack Type | Looted Weapon | Damage | Available Quantity |
|-------------|---------------|--------|---------------------|
| Critical    | Laser Gun     | 100    | 2                   |
| Headshot    | holo grenade  | 50     | 3                   |
| Bodyshot    | AR            | 40     | 4                   |
| Legshot     | pistol        | 3      | 3                   |
| Normal      | melee         | 10     | Unlimited           |

- Weapons are earned based on **random attack outcomes**.
- **Normal attacks** do not provide any loot but always deal **10 damage**.

---

## 💻 Installation

No external libraries are required apart from Python’s standard library.

```bash
git clone https://github.com/yourusername/weapon-battle-game.git
cd weapon-battle-game
