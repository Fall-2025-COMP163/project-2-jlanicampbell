# 🧙‍♂️ Character Battle System  
**COMP 163 — Project 2: Object-Oriented Programming**

---

## 🪄 Bonus Creative Features
In addition to the core requirements, I added several creative elements to make the project more engaging and realistic:

- **Weapon Composition System:** Players can now equip a weapon object that adds bonus attack damage.  
- **Formatted Output:** All stats and battle actions print with clear, readable formatting for better visualization.  
- **Critical Hits for Rogues:** Introduced a random critical hit mechanic (30% chance) to make combat more dynamic.  
- **Powerful Special Moves:** Each subclass has a distinct ability — *Power Strike*, *Fireball*, and *Sneak Attack* — with unique damage formulas.  
- **Battle Simulator Ready:** The provided `SimpleBattle` system integrates perfectly with my character classes for easy testing.

---

## 🤖 AI Usage
AI assistance was used responsibly to **support** coding, not replace learning or design.  
Specifically:
- **ChatGPT (GPT-5)** was used for:
  - Guidance on implementing inheritance and method overriding.  
  - Generating docstrings and professional-style inline comments.  
  - Reviewing logic for the `attack`, `take_damage`, and special ability methods.  
  - Formatting this `README.md` file for clear documentation.  
All final logic, code structure, and debugging were completed by me.

---

## ⚙️ How to Run

### 1️⃣ Run Tests (for grading)
To verify that all class implementations meet the rubric:
```bash
pytest -q
