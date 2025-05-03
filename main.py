import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    ContextTypes
)
from dotenv import load_dotenv
import os
import asyncio

# Carrega handlers
from handlers.commands import start, agenda, elenco, noticias
from handlers.stickers import gritar, figurinhas
from handlers.torcida import torcida_simulada, status_jogo, resposta_livre
from handlers.quiz import iniciar_quiz, cancelar_quiz, PERGUNTA, receber_resposta
from handlers.redes_sociais import redes_sociais
from handlers.momentos import momentos_furia

# Configuração inicial
load_dotenv()
TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("URL")
WEBHOOK_URL = f"{BASE_URL}/webhook" if BASE_URL else None
PORT = int(os.environ.get("PORT", 5000))

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Cria aplicação
application = Application.builder().token(TOKEN).build()
app = Flask(__name__)


def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("elenco", elenco))
    app.add_handler(CommandHandler("gritar", gritar))
    app.add_handler(CommandHandler("torcida_simulada", torcida_simulada))
    app.add_handler(CommandHandler("momentos", momentos_furia))
    
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("quiz", iniciar_quiz)],
        states={
            PERGUNTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_resposta)]
        },
        fallbacks=[CommandHandler("cancelar", cancelar_quiz)],
    ))
    
    app.add_handler(CommandHandler("figurinhas", figurinhas))
    app.add_handler(CommandHandler("statusjogo", status_jogo))
    app.add_handler(CommandHandler("redes_sociais", redes_sociais))
    app.add_handler(CommandHandler("noticias", noticias))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_livre))


register_handlers(application)


@app.route('/')
def index():
    return 'FURIA Bot is running!'


@app.route('/webhook', methods=['POST'])
async def webhook():
    if request.method == "POST":
        try:
            json_data = await request.get_json()
            update = Update.de_json(json_data, application.bot)
            
            # Cria um novo loop de evento se necessário
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            await application.process_update(update)
            return '', 200
        except Exception as e:
            logger.error(f"Erro no webhook: {str(e)}")
            return '', 200
    return '', 403


async def set_webhook():
    await application.bot.set_webhook(
        url=WEBHOOK_URL,
        drop_pending_updates=True,
        max_connections=100
    )

if __name__ == "__main__":
    if not TOKEN or not BASE_URL:
        logger.error("TOKEN e URL devem estar definidos no .env!")
        exit(1)

    # Configura o webhook
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_webhook())
    
    # Inicia o servidor
    app.run(host='0.0.0.0', port=PORT)