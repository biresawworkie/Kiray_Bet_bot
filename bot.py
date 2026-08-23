
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = "8999460289:AAEPnNSotffmjsoVQ-N_ouq-h0yemaxJaZU"
WEB_APP_URL = "https://kiray-bet-bot.onrender.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("🇪🇹 አማርኛ", callback_data="lang_am"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ],
        [
            InlineKeyboardButton("🏠 Open KirayBet App", web_app=WebAppInfo(url=WEB_APP_URL))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "እንኳን ወደ ኪራይ ቤት ቦት በደህና መጡ! / Welcome to KirayBet Bot!\nእባክዎን ቋንቋ ይምረጡ፡",
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
