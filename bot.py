import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
WEB_APP_URL = os.environ.get("WEB_APP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇪🇹 አማርኛ", callback_data="lang_am"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome / እንኳን ደህና መጡ!\nእባክዎን የቋንቋ ምርጫዎን ይምረጡ:",
        reply_markup=reply_markup
    )

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("🏠 ተከራይ (Tenant)", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton("🔑 አከራይ (Landlord)", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton("🏢 ኤጀንት (Agent)", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="እባክዎን ሚናዎን ይምረጡ:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(set_language))
    app.run_polling()
