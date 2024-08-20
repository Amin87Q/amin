from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TELEGRAM_API_TOKEN = "7381119633:AAFuQrupXHZpqEqQcDTZZHXEJCWOwswG0V8"

def start(update, context):
    update.message.reply_text("سلام! من یک ربات ساده هستم.")

def help_command(update, context):
    update.message.reply_text("دستورات: /start /help")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
