import logging
import nest_asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from dotenv import load_dotenv
import os
from threading import Thread

# Import handlers
from handlers.commands import start, agenda, elenco, noticias
from handlers.stickers import gritar, figurinhas
from handlers.torcida import torcida_simulada, status_jogo, resposta_livre
from handlers.quiz import iniciar_quiz, cancelar_quiz, PERGUNTA, receber_resposta
from handlers.redes_sociais import redes_sociais
from handlers.momentos import momentos_furia

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL") + '/webhook'

# Apply nest_asyncio for async compatibility
nest_asyncio.apply()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Create Flask app
flask_app = Flask(__name__)

# Create Telegram application
application = ApplicationBuilder().token(TOKEN).build()

# Add handlers
def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("elenco", elenco))
    app.add_handler(CommandHandler("gritar", gritar))
    app.add_handler(CommandHandler("torcida_simulada", torcida_simulada))
    app.add_handler(CommandHandler("momentos", momentos_furia))
    
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("quiz", iniciar_quiz)],
        states={PERGUNTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_resposta)]},
        fallbacks=[CommandHandler("cancelar", cancelar_quiz)],
    ))
    
    app.add_handler(CommandHandler("figurinhas", figurinhas))
    app.add_handler(CommandHandler("statusjogo", status_jogo))
    app.add_handler(CommandHandler("redes_sociais", redes_sociais))
    app.add_handler(CommandHandler("noticias", noticias))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_livre))

# Register handlers
register_handlers(application)

@flask_app.route('/')
def index():
    return 'FURIA Bot is running!'

@flask_app.route('/webhook', methods=['POST'])
async def webhook():
    if request.headers.get('content-type') == 'application/json':
        update = Update.de_json(request.get_json(force=True), application.bot)
        await application.update_queue.put(update)
        return 'ok'
    return 'Bad request', 400

async def setup_webhook():
    await application.bot.set_webhook(
        url=URL,
        drop_pending_updates=True
    )
    logger.info("Webhook set up successfully at %s", URL)

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Set webhook
    Thread(target=setup_webhook).start()

    # Run Flask server
    run_flask()
