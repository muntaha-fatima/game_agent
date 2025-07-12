
# 🎮 Game Master Agent

An interactive AI-powered game system using **Chainlit** and **Gemini AI**, built with **OpenAI Agent SDK-style logic**. This project uses **multiple agents and tools with handoff logic** to simulate a text-based adventure game.

---

## ✅ Requirements Met

| Requirement                              | Implemented ✅ |
|------------------------------------------|----------------|
| Use at least **2 Tools**                 | ✅ `Roll Dice`, `Generate Event` |
| Use at least **2 Agents**                | ✅ `NarratorAgent`, `MonsterAgent`, `ItemAgent` *(3 total)* |
| Handoff Logic between Agents & Tools     | ✅ Implemented |
| Use of **OpenAI Agent SDK-style logic**  | ✅ Follows `on_message`, tool decorators, and agent design |
| Well-structured code folder              | ✅ Yes |
| `README.md` with agent and flow details  | ✅ You're reading it! |

---

## 🧠 What This Agent Does

This agent turns user input into a **mini adventure game**. The game flow includes:

1. Narrated **story introduction**
2. A simulated **event** (via `Generate Event` tool)
3. A **monster attack** using the `MonsterAgent`
4. A **magical item reward** via the `ItemAgent`
5. A **dice roll** for randomness

It’s all triggered just by your message!

---

## 🔁 Flow Logic

```text
User Message
   │
   ▼
NarratorAgent → Introduction
   │
   ▼
generate_event_tool(context)
   │
   ▼
MonsterAgent.attack(context)
   │
   ▼
ItemAgent.give_item(context)



📁 Project Structure

game-master-agent/
├── agents/
│   ├── narrator_agent.py
│   ├── monster_agent.py
│   └── item_agent.py
├── tools/
│   └── game_tools.py
├── main.py
├── .env
├── README.md
└── requirements.txt

## 🧠 What This Agent Does

This AI Agent turns user input into a **text-based roleplay adventure game**. Based on your message, it:

1. Generates a **narrated story intro**
2. Simulates an **event** (via `Generate Event` tool)
3. Triggers a **monster encounter** (via `MonsterAgent`)
4. Rewards the player with an **item** (via `ItemAgent`)
5. Uses a **dice roll tool** to determine random elements

---



## 🛠️ Tools Used

| Tool Name         | Purpose |
|-------------------|---------|
| `roll_dice_tool`  | Simulates rolling a dice with custom sides |
| `generate_event_tool` | Uses `NarratorAgent` to create an adventure event based on user input |

---
| Tool Name             | Description                                           |
| --------------------- | ----------------------------------------------------- |
| `roll_dice_tool`      | Simulates dice rolls with any number of sides         |
| `generate_event_tool` | Generates a random adventure event using the narrator |

---

## 🔁 Handoff Logic

The handoff flow works like this:

```txt
User Input →
  → NarratorAgent (intro)
  → Generate Event Tool (event based on context)
  → MonsterAgent (enemy encounter)
  → ItemAgent (gives an item)

🙋 Created By SEERAT FATIMA 🎓 GIAIC Student | 🧠 Passionate about AI & Career Empowerment
