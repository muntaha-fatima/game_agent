
# from tools.game_tools import roll_dice
# class MonsterAgent:
#     def __init__(self, model):
#         self.model = model

#     def run(self, user_input: str) -> str:
#         dice = roll_dice()

#     def attack(self, context: str) -> str:
#         prompt = f"In a fantasy game, describe a dramatic monster encounter following this situation: '{context}'. Include action!"
#         response = self.model.generate_content(prompt)
#         return response.text



# agents/monster_agent.py

from tools.game_tools import roll_dice  # ✅ YES, correct import

class MonsterAgent:
    def __init__(self, model):
        self.model = model

    def attack(self, context: str) -> str:
        # Get dice result
        dice_result = roll_dice()

        # Use Gemini for dynamic combat description
        prompt = (
            f"{dice_result}\n"
            f"In a fantasy game, describe a dramatic monster encounter after this situation: '{context}'. "
            "Include what kind of monster it is, what it does, and how the player reacts."
        )
        response = self.model.generate_content(prompt)
        return response.text
