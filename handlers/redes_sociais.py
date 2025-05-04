from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def redes_sociais(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Mensagem com links para as redes sociais
    mensagem = (
        "Para interagir diretamente com a FURIA, você pode acessar as nossas redes e sites oficiais! 📱\n\n"
        "📲 Entre em contato com a gente no WhatsApp exclusivo!\n\n"
        "📸 Nos siga no Instagram para acompanhar nosso conteúdo exclusivo!\n\n"
        "🛒 Confira a nossa loja oficial e vista o manto da FURIA com orgulho!"
    )

    # Criar botões para interação
    keyboard = [
        [
            InlineKeyboardButton("WhatsApp", url="https://wa.me/5511993404466?text=Oi,%20quero%20saber%20mais%20sobre%20a%20FURIA!"),
            InlineKeyboardButton("Instagram", url="https://www.instagram.com/furiagg/?hl=pt-br")
        ],
        [InlineKeyboardButton("FURIA Store", url="https://www.furia.gg/")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar mensagem com os botões
    await update.message.reply_text(mensagem, reply_markup=reply_markup)
