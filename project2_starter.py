"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Jelani Campbell
Date: 11/11/25

AI Usage: AI assistance was used responsibly to **support** coding, not replace learning or design.  
Specifically:
- **ChatGPT (GPT-5)** was used for:
  - Guidance on implementing inheritance and method overriding.  
  - Generating docstrings and professional-style inline comments.  
  - Reviewing logic for the `attack`, `take_damage`, and special ability methods.
  All final logic, code structure, and debugging were completed by me.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

import random 

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health 
        self.strength = strength 
        self.magic = magic 
        
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health = self.health - damage 
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage and now has {self.health} health.")
            
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"\n--- {self.name}'s Stats ---")
        print(f"Health   : {self.health}")
        print(f"Strength : {self.strength}")
        print(f"Magic    : {self.magic}") 


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.weapon = None 

    def equip_weapon(self, weapon):
        """
        Equip a weapon for this player.
        The weapon provides additional damage bonus during attacks.
        """
        self.weapon = weapon
        print(f"{self.name} has equipped the {weapon.name} (Damage Bonus: +{weapon.damage_bonus})")
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
     
        super().display_stats()
        print(f"Class      : {self.character_class}")
        print(f"Level      : {self.level}")
        print(f"Experience : {self.experience}")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        damage = self.strength + 5
        print(f"{self.name} slashes {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = (self.strength * 2) + 10
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20)
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        damage = self.magic + 3
        print(f"{self.name} cast a magic bolt at {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = (self.magic * 2) + 5
        print(f"{self.name} hurls a massive fireball at {target.name} for {damage} damage!")
        target.take_damage(damage)

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        damage = self.strength
        crit_roll = random.randint(1, 10)
        if crit_roll <= 3:
            damage *= 2
            print(f"Critical hit! {self.name} backstabs {target.name} for {damage} damage!")
        else:
            print(f"{self.name} swiftly strikes {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = self.strength * 2
        print(f"{self.name} performs a deadly sneak attack on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus 
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        print(f"Weapon {self.name} | Damage Bonus: +{self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("\n⚔️ CHARACTER ABILITIES SHOWCASE ⚔️")
    print("Testing inheritance, polymorphism, and method overriding")
    print("-" * 50)

    # Create characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Create weapons
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    # Equip weapons
    warrior.equip_weapon(sword)
    mage.equip_weapon(staff)
    rogue.equip_weapon(dagger)

    # Display stats
    print("\n🧍 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Test polymorphism
    print("\n🎭 Testing Polymorphism (same method name, different behavior):")
    dummy_target = Character("Training Dummy", 100, 0, 0)
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy

    # Test special abilities
    print("\n🔥 Testing Special Abilities:")
    enemy = Character("Enemy", 100, 0, 0)
    warrior.power_strike(enemy)
    mage.fireball(enemy)
    rogue.sneak_attack(enemy)

    # Test battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, rogue)
    battle.fight()

    print("\n✅ Testing complete!")

