import os
import logging
import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
from dotenv import load_dotenv

# Carregar variáveis de ambiente
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("URL")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{BASE_URL}{WEBHOOK_PATH}"

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

# Telegram Application
telegram_app = Application.builder().token(TOKEN).build()

# Importar handlers (ajuste para seu projeto)
from handlers.commands import start, agenda, elenco, noticias
from handlers.stickers import gritar, figurinhas
from handlers.torcida import torcida_simulada, status_jogo, resposta_livre
from handlers.quiz import iniciar_quiz, cancelar_quiz, PERGUNTA, receber_resposta
from handlers.redes_sociais import redes_sociais
from handlers.momentos import momentos_furia

# Registrar handlers
def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("elenco", elenco))
    app.add_handler(CommandHandler("gritar", gritar))
    app.add_handler(CommandHandler("momentos", momentos_furia))
    app.add_handler(CommandHandler("figurinhas", figurinhas))
    app.add_handler(CommandHandler("statusjogo", status_jogo))
    app.add_handler(CommandHandler("redes_sociais", redes_sociais))
    app.add_handler(CommandHandler("noticias", noticias))

    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("quiz", iniciar_quiz)],
        states={PERGUNTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_resposta)]},
        fallbacks=[CommandHandler("cancelar", cancelar_quiz)],
    ))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_livre))

register_handlers(telegram_app)

# Endpoint raiz
@app.get("/")
def root():
    return {"message": "FURIA Bot is live with FastAPI!"}

# Endpoint do webhook
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

# Inicializa Webhook no Telegram
@app.on_event("startup")
async def on_startup():
    await telegram_app.initialize()
    await telegram_app.bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)
    logger.info(f"Webhook configurado: {WEBHOOK_URL}")
