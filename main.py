import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

TOKEN = os.getenv("token.env")
bot = telebot.TeleBot(TOKEN)

vouches = 245
orders = 234

stock_text = f"""
╔════════════════════╗
      Roblox stock
╚════════════════════╝

👑 ACCOUNT INVENTORY
━━━━━━━━━━━━━━━━━━
🟣 23x Korblox Accounts
⚫ 12x Headless Accounts
🌗 32x Korblox + Headless

🎩 LIMITEDS
━━━━━━━━━━━━━━━━━━
☠️ 2x Poisoned Horns
❄️ 1x Frozen Horns
🔥 3x Horns of Fiery

📊 SELLER STATS
━━━━━━━━━━━━━━━━━━
✅ {vouches}+ Vouches
📦 {orders}+ Orders Done
🟢 Status: Online
⚡ Delivery: Instant
🛡️ Trusted Seller

💰 PAYMENTS
━━━━━━━━━━━━━━━━━━
💸 Crypto
💳 PayPal
🎮 Giftcards

━━━━━━━━━━━━━━━━━━
"""

@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup(row_width=2)

    stock = InlineKeyboardButton(
        "📦 Stock",
        callback_data="stock"
    )

    prices = InlineKeyboardButton(
        "💸 Prices",
        callback_data="prices"
    )

    vouch = InlineKeyboardButton(
        "✅ Vouches",
        callback_data="vouches"
    )

    delivery = InlineKeyboardButton(
        "⚡ Delivery",
        callback_data="delivery"
    )

    contact = InlineKeyboardButton(
        "💬 Contact",
        url="https://t.me/youruser"
    )

    channel = InlineKeyboardButton(
        "📢 Channel",
        url="https://t.me/yourchannel"
    )

    markup.add(stock, prices)
    markup.add(vouch, delivery)
    markup.add(contact, channel)

    bot.send_photo(
        message.chat.id,
        "https://i.imgur.com/8Km9tLL.jpeg",
        caption=stock_text,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "stock":
        bot.answer_callback_query(call.id, "📦 Stock Synced")
        bot.send_message(call.message.chat.id, stock_text)

    elif call.data == "prices":

        prices_text = """
💸 PRICE LIST
━━━━━━━━━━━━━━━━━━
🟣 Korblox Account — $45
⚫ Headless Account — $40
🌗 Combo Account — $75

☠️ Poisoned Horns — $150
❄️ Frozen Horns — $200
🔥 Fiery Horns — $170
━━━━━━━━━━━━━━━━━━
"""

        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, prices_text)

    elif call.data == "vouches":

        fake_vouches = [
            "✅ Smooth trade vouch",
            "🔥 Legit seller",
            "⚡ Fast delivery",
            "💯 Trusted",
            "🛡️ Bought again"
        ]

        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "
".join(fake_vouches)
        )

    elif call.data == "delivery":

        loading = bot.send_message(
            call.message.chat.id,
            "⚡ Preparing delivery..."
        )

        time.sleep(2)

        bot.edit_message_text(
            "✅ Delivery completed successfully",
            call.message.chat.id,
            loading.message_id
        )

@bot.message_handler(commands=['admin'])
def admin(message):

    admin_text = """
👑 ADMIN PANEL
━━━━━━━━━━━━━━━━━━
/addstock
/removestock
/updateprices
/broadcast
━━━━━━━━━━━━━━━━━━
"""

    bot.send_message(message.chat.id, admin_text)

print("🔥 Elite Seller Bot Running...")
bot.infinity_polling()
