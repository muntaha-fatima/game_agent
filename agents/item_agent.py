# class ItemAgent:
#     def __init__(self, model):
#         self.model = model

#     def give_item(self, context: str) -> str:
#         prompt = f"In a fantasy adventure, give the player a magical or useful item after this situation: '{context}'. Make it feel rewarding."
#         response = self.model.generate_content(prompt)
#         return response.text




# agents/item_agent.py

from tools.game_tools import generate_event  # 👈 Import the tool-based event generator

class ItemAgent:
    def __init__(self, model):
        self.model = model

    def give_item(self, context: str) -> str:
        # First, use the tool-based generate_event to add some randomness
        event = generate_event()

        # Then, ask Gemini to give an item related to it
        prompt = (
            f"In a fantasy adventure, after this random event: '{event}', and the current situation: '{context}', "
            "give the player a magical or useful item. Make it feel exciting and rewarding."
        )
        response = self.model.generate_content(prompt)
        return response.text
