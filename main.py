from flask import Flask, request, jsonify
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
import os
import logging
from functools import wraps

# Configuração básica
app = Flask(__name__)
TOKEN = os.getenv("TOKEN")
application = Application.builder().token(TOKEN).build()

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Decorator para verificar o método HTTP
def post_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method != 'POST':
            return jsonify({"error": "Method not allowed"}), 405
        return f(*args, **kwargs)
    return decorated_function


@app.route('/webhook', methods=['POST', 'GET'])
@post_only
async def webhook():
    try:
        # Verifica se o conteúdo é JSON
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        data = request.get_json()
        update = Update.de_json(data, application.bot)
        
        # Processa a atualização
        await application.process_update(update)
        return '', 200
        
    except Exception as e:
        logger.error(f"Error processing update: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/')
def index():
    return "FURIA Bot Webhook - POST requests to /webhook"


if __name__ == '__main__':
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 5000)),
        webhook_url=os.getenv("URL") + "/webhook",
        drop_pending_updates=True
    )