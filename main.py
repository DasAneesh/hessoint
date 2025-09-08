from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN = "8443518235:AAGHq8YwUXTW8jOkwpPuJpigKZZM2kJGQm8"
Counter_dict = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # user = update.effective_user
    # await update.message.reply_html(
    #     f"Привет, {user.mention_html()}! Я простой эхо-бот."
    # )
    keyboard = [
        [InlineKeyboardButton("Опция 1", callback_data='1')],
        [InlineKeyboardButton("Опция 2", callback_data='2')],
        [InlineKeyboardButton("Опция 3", callback_data='3'),
         InlineKeyboardButton("Опция 4", callback_data='4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('пожайлуста выберите:', reply_markup=reply_markup)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Чем тебе помочь ? Hi <b>how can i help u</b> "
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.data in Counter_dict:
        Counter_dict[query.data]+=1
    else:
        Counter_dict[query.data]=1
    await query.answer()
    await query.edit_message_text(text=f"Вы выбрали опцию: {query.data}")


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = ""
    for key, val in Counter_dict.items():
        message+=f"You used option <b>{key}</b>: <i>{val}</i> times\n"
    await update.message.reply_html(message)    


async def html_ex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Это <b>bold</b> <i>cursive</i> <code>code</code> <a href = 'https://www.deepseek.com/'>link</a>"
    await update.message.reply_html(message)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("html", html_ex))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Бот запущен...")
    application.run_polling()

if __name__ =="__main__":
    main()