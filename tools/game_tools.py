# tools/game_tools.py (clean version)

import random

def roll_dice(sides: int = 6) -> str:
    result = random.randint(1, sides)
    return f"🎲 You rolled a {result} on a {sides}-sided dice."

def generate_event() -> str:
    events = [
        "👹 A monster jumps out of the bushes!",
        "💰 You stumble upon a hidden treasure chest!",
        "🌲 The path is quiet... nothing happens.",
        "⛲ You find a mystic fountain that restores your energy!"
    ]
    return random.choice(events)
