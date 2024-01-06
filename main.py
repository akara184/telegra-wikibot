from typing import Final
from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes, filters


TOKEN: Final  = '6936743062:AAEv65LYT02MDSl_08G6Lj7t3dE_N9_tjgk' 
BOT_USERNAME: Final = '@purgatorioWiki_bot' 

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bem-vindo ao wiki do b")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("mensagem de help")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("esse é um comando custom")




async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

  


def main() -> None:
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()


    # Commands

    app.add_handler(CommandHandler("start",start_command))
    app.add_handler(CommandHandler("help_command",help_command))
    app.add_handler(CommandHandler("start",start_command))

    print('Starting polling')
        


if __name__ == "__main__":
    main()