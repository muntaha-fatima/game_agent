import random

def generate_event() -> str:
    events = [
        "👹 A monster jumps out of the bushes!",
        "💰 You stumble upon a hidden treasure chest!",
        "🌲 The path is quiet... nothing happens.",
        "⛲ You find a mystic fountain that restores your energy!"
    ]
    return random.choice(events)
