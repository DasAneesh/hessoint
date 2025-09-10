from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

from gemini import chat_response

Counter_dict = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
         f"Привет, {user.mention_html()}! Я gemini bot."
     )
    
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Чем тебе помочь ? Hi <b>how can i help u</b> "
    )

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = " ".join(context.args)
    
    if not question:
        await update.message.reply_text("Пожалуйста, задайте вопрос после команды /ask")
        return
        
    res = chat_response(question, update.message.chat.id)
    
    # Конвертируем Markdown в простой HTML для Telegram
    formatted_text = res
    formatted_text = formatted_text.replace('**', '<b>').replace('**', '</b>')
    formatted_text = formatted_text.replace('*', '<i>').replace('*', '</i>')
    formatted_text = formatted_text.replace('`', '<code>').replace('`', '</code>')
    formatted_text = formatted_text.replace('__', '<u>').replace('__', '</u>')
    
    # Экранируем HTML символы
    formatted_text = formatted_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    try:
        await update.message.reply_text(formatted_text, parse_mode="HTML")
    except:
        await update.message.reply_text(res) 

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)
