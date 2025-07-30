from telebot import TeleBot, types
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = TeleBot(TOKEN)

# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("📞 Calling phrases"),
        types.KeyboardButton("📝 Documents"),
        types.KeyboardButton("📍 Load status"),
        types.KeyboardButton("🚛 Pickup phrases"),
        types.KeyboardButton("🚚 Transit phrases"),
        types.KeyboardButton("🏁 Delivery phrases"),
        types.KeyboardButton("💵 Rate negotiation"),
        types.KeyboardButton("📋 Load form"),
        types.KeyboardButton("📄 Paperwork")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! Choose a category:", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    responses = {
        "📞 Calling phrases": "\n".join([
            "Hi, I'm calling about the load from [City] to [City]. Is it still available?",
            "Can you tell me the rate and the weight?",
            "I'm with dispatch.",
            "Are there any accessorials?"
        ]),

        "📝 Documents": "\n".join([
            "Please send the rate confirmation to our email.",
            "Could you send me the ratecon?",
            "Our MC number is [your MC number].",
            "What are the appointment times?"
        ]),

        "📍 Load status": "\n".join([
            "The driver is empty and can pick up today at [time].",
            "He's at the pickup now.",
            "The load is delivered.",
            "Driver is stuck in traffic, will be late."
        ]),

        "🚛 Pickup phrases": "\n".join([
            "Is it a live load or drop and hook?",
            "Do you need the trailer number?",
            "He's checking in now.",
            "They said it's not ready yet."
        ]),

        "🚚 Transit phrases": "\n".join([
            "The driver is on the way.",
            "He's stuck in traffic.",
            "He’ll arrive around [time].",
            "Can I get an ETA?"
        ]),

        "🏁 Delivery phrases": "\n".join([
            "Is it a live unload?",
            "They're unloading now.",
            "Can we get a POD?",
            "Delivery is complete."
        ]),

        "💵 Rate negotiation": "\n".join([
            "Can you go higher on the rate?",
            "We need at least $[amount].",
            "If you can do $[amount], I’ll book it now.",
            "Sorry, my driver wants more."
        ]),

        "📋 Load form": "\n".join([
            "PU date/time",
            "PU City/State",
            "Delivery date/time",
            "Delivery City/State",
            "Loaded distance",
            "Commodity",
            "Weight",
            "Broker + MC#"
        ]),

        "📄 Paperwork": "\n".join([
            "Rate confirmation",
            "POD (Proof of Delivery)",
            "BOL (Bill of Lading)",
            "Lumper receipt"
        ])
    }

    reply = responses.get(message.text, "Please choose a button from the menu.")
    bot.send_message(message.chat.id, reply)

bot.polling()
