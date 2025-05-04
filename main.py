import os
import logging
import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, ConversationHandler, MessageHandler, filters
)
from dotenv import load_dotenv

# Importar handlers
from handlers.commands import start, agenda, elenco, noticias
from handlers.stickers import gritar, figurinhas
from handlers.torcida import torcida_simulada, status_jogo, resposta_livre
from handlers.quiz import iniciar_quiz, cancelar_quiz, PERGUNTA, receber_resposta
from handlers.redes_sociais import redes_sociais
from handlers.momentos import momentos_furia

# Carregar variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("URL")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{BASE_URL}{WEBHOOK_PATH}"

# Configurar logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

# Telegram Application
telegram_app = Application.builder().token(TOKEN).build()


# Registrar todos os handlers
def register_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("agenda", agenda))
    application.add_handler(CommandHandler("elenco", elenco))
    application.add_handler(CommandHandler("gritar", gritar))
    application.add_handler(CommandHandler("momentos", momentos_furia))
    application.add_handler(CommandHandler("figurinhas", figurinhas))
    application.add_handler(CommandHandler("statusjogo", status_jogo))
    application.add_handler(CommandHandler("redes_sociais", redes_sociais))
    application.add_handler(CommandHandler("noticias", noticias))
    application.add_handler(CommandHandler("torcida_simulada", torcida_simulada))


    # Corrigido: Quiz com ConversationHandler assíncrono
    quiz_handler = ConversationHandler(
        entry_points=[CommandHandler("quiz", iniciar_quiz)],
        states={
            PERGUNTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_resposta)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar_quiz)],
    )
    application.add_handler(quiz_handler)

    # Mensagens livres
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_livre))


# Chama registro
register_handlers(telegram_app)

# Raiz
@app.get("/")
def root():
    return {"message": "FURIA Bot is live with FastAPI!"}

# Webhook
@app.post(WEBHOOK_PATH)
async def handle_webhook(request: Request):
    try:
        data = await request.json()
        update = Update.de_json(data, telegram_app.bot)
        await telegram_app.process_update(update)
    except Exception as e:
        logger.error(f"Erro no processamento do webhook: {e}")
        return {"status": "error"}
    return {"status": "ok"}

# Inicializar Webhook no Telegram
@app.on_event("startup")
async def on_startup():
    await telegram_app.initialize()
    await telegram_app.bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)
    logger.info(f"Webhook configurado com sucesso: {WEBHOOK_URL}")
