from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def redes_sociais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensagem com links para as redes sociais
    mensagem = (
        "Para interagir diretamente com a FURIA, você pode acessar as nossas redes e sites oficiais! 📱\n\n"
        "📲 Entre em contato com a gente no WhatsApp exclusivo!\n\n"
        "📸 Nos siga no Instagram para acompanhar nosso conteúdo exclusivo!\n\n"
        "🛒 Confira a nossa loja oficial e vista o manto da FURIA com orgulho!"
    )

    # Criar botões para interação
    keyboard = [
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/5511993404466?text=Oi,%20quero%20saber%20mais%20sobre%20a%20FURIA!"),
         InlineKeyboardButton("Instagram", url="https://www.instagram.com/furiagg/?hl=pt-br")],
        [InlineKeyboardButton("FURIA Store", url="https://www.furia.gg/")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar mensagem com os botões
    await update.message.reply_text(mensagem, reply_markup=reply_markup)

    # Enviar os ícones das redes sociais
    whatsapp_icon_url = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
    instagram_icon_url = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"

    # Enviar o ícone do WhatsApp
    await update.message.reply_photo(
        whatsapp_icon_url,
        caption="Clique no ícone para conversar com a FURIA pelo WhatsApp! 📱"
    )

    # Enviar o ícone do Instagram
    await update.message.reply_photo(
        instagram_icon_url,
        caption="Clique no ícone para seguir a FURIA no Instagram! 📸"
    )
