import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
import os

from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent
from tools.game_tools import roll_dice, generate_event

# Load env & model
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Agents
narrator = NarratorAgent(model)
monster = MonsterAgent(model)
item = ItemAgent(model)

@cl.on_chat_start
async def start_chat():
    await cl.Message(content="🎮 Welcome to the Game Master Agent! Type anything to begin your adventure.").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    await cl.Message(content=narrator.intro(user_input)).send()
    await cl.Message(content=generate_event(user_input, narrator)).send()
    await cl.Message(content=monster.attack(user_input)).send()
    await cl.Message(content=item.give_item(user_input)).send()
