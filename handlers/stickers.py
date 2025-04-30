# Importa o módulo random para escolher elementos aleatórios
import random

# Importa as classes necessárias da biblioteca python-telegram-bot
from telegram import Update
from telegram.ext import ContextTypes

# Lista com os IDs das figurinhas da FURIA.
# Esses IDs são usados para enviar figurinhas específicas no Telegram.
stickers = [
    "CAACAgEAAxkBAAEOYXpoECqW7Jct_X2u4YkCjYapc0DtSQACrAcAAnmAgUTEJUikBw9ddDYE",  # Logo FURIA
    "CAACAgEAAxkBAAEOYXxoECqbRnPO29usWiL1gXYL-vNwPAAC7QUAAkKEeETexcAXvA0YkDYE",
    "CAACAgEAAxkBAAEOYX5oECqejmQTB5WUiWon0kqL5uan-wAC1gMAAqwKgURjgwxp8iFTxDYE",
    "CAACAgEAAxkBAAEOYYBoECqhPpYZ_4akeEffcdOMn8fWHQACzQYAApWegUSBrTpl8UGoaDYE",
    "CAACAgEAAxkBAAEOYYJoECtMGZB_Iq8zP1mTEf5XDXNdlAACOwYAAs0HgUTOn9nGIcrC5zYE",
    "CAACAgEAAxkBAAEOYYRoECtO5KyDjlLoGdlbrcY70om0bwAC4AoAAtj4gERgjrOurac1ezYE"
]


# Função assíncrona que envia uma figurinha aleatória junto com uma mensagem de texto
async def figurinhas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sticker_id = random.choice(stickers)  # Seleciona uma figurinha aleatória
    await update.message.reply_text("Aqui vai uma figurinha da FURIA!")  # Envia um texto
    await update.message.reply_sticker(sticker_id)  # Envia a figurinha


# Outra função que envia apenas uma figurinha aleatória da lista, sem texto
async def mandar_figurinha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(random.choice(stickers))


# Função que envia uma mensagem de "grito de torcida" aleatória
async def gritar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gritos = [
        "VAMO FURIAAAA 🔥🔥🔥",
        "DOMINA ESMAGA! 💥",
        "VAI PRA CIMA DELES FURIA! 🐆",
        "AQUI É FURIA, PORRA! 🔥💛🖤",
        "A FURIA NUNCA DESISTE!"
    ]
    await update.message.reply_text(random.choice(gritos))  # Envia um grito aleatório


# Função que simula mensagens da torcida, como se fosse uma interação pré-programada
async def torcida_simulada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respostas_torcida = [
        "E aí, #FuriaNation! Como estamos para o próximo jogo? 💥",
        "Isso aí! A FURIA não vai deixar nada passar, é o momento da vitória! 🙌",
        "É isso mesmo, a torcida é o nosso combustível! Rumo ao título! 💣",
        "Vamos FURIA, é tudo nosso! 💛🖤"
    ]
    resposta_inicial = random.choice(respostas_torcida)
    await update.message.reply_text(resposta_inicial)  # Envia uma mensagem da torcida simulada
