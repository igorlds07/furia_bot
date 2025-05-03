import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackContext
)
# Import handlers (versões síncronas)
from handlers.commands import start, agenda, elenco, noticias
from handlers.stickers import gritar, figurinhas
from handlers.torcida import torcida_simulada, status_jogo, resposta_livre
from handlers.quiz import iniciar_quiz, cancelar_quiz, PERGUNTA, receber_resposta
from handlers.redes_sociais import redes_sociais
from handlers.momentos import momentos_furia

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("URL")
WEBHOOK_URL = f"{BASE_URL}/webhook" if BASE_URL else None

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Initialize bot and application
bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()



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


@app.route('/')
def index():
    return 'FURIA Bot is running!'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        update = Update.de_json(request.get_json(), bot)
        application.process_update(update)
        return '', 200
    return 'Bad request', 400


def set_webhook():
    try:
        bot.set_webhook(
            url=WEBHOOK_URL,
            drop_pending_updates=True
        )
        logger.info(f"Webhook configurado com sucesso em: {WEBHOOK_URL}")
    except Exception as e:
        logger.error(f"Erro ao configurar webhook: {e}")
        raise

if __name__ == "__main__":
    # Verifica se as variáveis necessárias estão definidas
    if not TOKEN or not BASE_URL:
        logger.error("TOKEN e URL devem estar definidos no .env!")
        exit(1)

    # Configura o webhook
    set_webhook()
    
    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))