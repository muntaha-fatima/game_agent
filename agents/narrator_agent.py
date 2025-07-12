class NarratorAgent:
    def __init__(self, model):
        self.model = model

    def intro(self, name: str) -> str:
        prompt = f"Introduce the player named {name} into a fantasy adventure world. Be immersive and engaging."
        response = self.model.generate_content(prompt)
        return response.text

    def generate_event(self, context: str) -> str:
        prompt = f"Continue the fantasy story based on the player's choice or situation: '{context}'. Add mystery and options."
        response = self.model.generate_content(prompt)
        return response.text
