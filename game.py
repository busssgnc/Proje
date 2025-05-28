import time
import random
import mounts
import character
import spell
import exception
from character import create_character
from mounts import mounts

SUBCLASS = ["Geralt", "Yennefer", "Golem", "Obsidian Brute", "Crystal Witch", "Iron Fang Beast"]

def choose_subclass():
    print("Choose your subclass:")
    for i, subclass in enumerate(SUBCLASS, 1):
        print(f"{i}) {subclass}")
    while True:
        choice = input("> ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(SUBCLASS):
                return SUBCLASS[index]
        print("Invalid choice. Please enter a valid number.")

def choose_mount(char_name):
    options = mounts.get(char_name, [])
    if not options:
        return None
    print("\nChoose your mount:")
    for i, mount in enumerate(options, 1):
        print(f"{i}) {mount}")
    while True:
        choice = input("> ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(options):
                return options[index]
        print("Invalid input. Please enter a valid number.")

def fight(character1, character2):
    print(f"\nBattle: {character1.name} vs {character2.name}")

    while character1.health > 0 and character2.health > 0:
        for attacker, defender in [(character1, character2), (character2, character1)]:
            print(f"\n{attacker.name}'s turn")
            print(f"Health: {attacker.health} | Mana: {attacker.mana}")
            print("Spells:")
            for i, spell in enumerate(attacker.spells, 1):
                cd_remaining = max(0, int(spell.cooldown - (time.time() - spell.last_cast_time)))
                print(f"{i}) {spell.name} (Mana: {spell.mana_cost}, Damage: {spell.damage}, Cooldown: {cd_remaining}s)")
            
            # 30 saniyelik seçim süresi
            start_turn = time.time()
            choice = None
            while True:
                if time.time() - start_turn > 30:
                    print("Time's up! You missed your turn.")
                    break
                choice = input("Choose spell number or press Enter to meditate: ").strip()
                if choice == '' or choice.isdigit():
                    break
                else:
                    print("Invalid input, try again.")

            if choice == '' or (choice is None):
                print(f"{attacker.name} meditates to recover mana.")
                attacker.meditate()
                print(f"Mana is now {attacker.mana}")
                continue

            if not choice.isdigit():
                print("Turn skipped due to invalid input or timeout.")
                continue

            spell_index = int(choice) - 1
            if 0 <= spell_index < len(attacker.spells):
                spell = attacker.spells[spell_index]
                success = attacker.cast_spell(spell, defender)
                if success:
                    print(f"{defender.name} health: {defender.health} | mana: {defender.mana}")
                    if defender.health <= 0:
                        print(f"{defender.name} is defeated!")
                        return
            else:
                print("Invalid spell choice.")
            time.sleep(1)

def main():
    print("Welcome to the battle game!")
    
    start_time = time.time()
    
    subclass = choose_subclass()
    print(f"You chose: {subclass}")
    player = create_character(subclass)

    # Yeni düşmanlar listesi
    enemy_options = ["Golem", "Obsidian Brute", "Crystal Witch", "Iron Fang Beast"]
    if subclass in enemy_options:
        opponent_name = random.choice([char for char in enemy_options if char != subclass])
    else:
        opponent_name = random.choice(enemy_options)

    opponent = create_character(opponent_name)

    mount = choose_mount(subclass)
    if mount:
        print(f"You ride your {mount} into battle!")

    fight(player, opponent)

    end_time = time.time()
    elapsed = end_time - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    print(f"\nGame duration: {minutes} minutes and {seconds} seconds.")

if __name__ == "__main__":
    main()
