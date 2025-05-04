import random
from telegram import Update
from telegram.ext import ContextTypes

# Lista de stickers (mantida igual)
stickers = [
    "CAACAgEAAxkBAAEOYXpoECqW7Jct_X2u4YkCjYapc0DtSQACrAcAAnmAgUTEJUikBw9ddDYE",
    "CAACAgEAAxkBAAEOYXxoECqbRnPO29usWiL1gXYL-vNwPAAC7QUAAkKEeETexcAXvA0YkDYE",
    "CAACAgEAAxkBAAEOYX5oECqejmQTB5WUiWon0kqL5uan-wAC1gMAAqwKgURjgwxp8iFTxDYE",
    "CAACAgEAAxkBAAEOYYBoECqhPpYZ_4akeEffcdOMn8fWHQACzQYAApWegUSBrTpl8UGoaDYE",
    "CAACAgEAAxkBAAEOYYJoECtMGZB_Iq8zP1mTEf5XDXNdlAACOwYAAs0HgUTOn9nGIcrC5zYE",
    "CAACAgEAAxkBAAEOYYRoECtO5KyDjlLoGdlbrcY70om0bwAC4AoAAtj4gERgjrOurac1ezYE"
]


# Função assíncrona para enviar figurinha com mensagem
async def figurinhas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sticker_id = random.choice(stickers)
    await update.message.reply_text("Aqui vai uma figurinha da FURIA!")
    await update.message.reply_sticker(sticker_id)


# Função assíncrona para enviar apenas figurinha
async def mandar_figurinha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(random.choice(stickers))

# Lista de gritos da torcida
gritos = [
    "VAMO FURIAAAA 🔥🔥🔥",
    "DOMINA ESMAGA! 💥",
    "VAI PRA CIMA DELES FURIA! 🐆",
    "AQUI É FURIA, PORRA! 🔥💛🖤",
    "A FURIA NUNCA DESISTE!"
]

# Função assíncrona para enviar grito aleatório
async def gritar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(gritos))

# Lista de respostas da torcida simulada
respostas_torcida = [
    "E aí, #FuriaNation! Como estamos para o próximo jogo? 💥",
    "Isso aí! A FURIA não vai deixar nada passar, é o momento da vitória! 🙌",
    "É isso mesmo, a torcida é o nosso combustível! Rumo ao título! 💣",
    "Vamos FURIA, é tudo nosso! 💛🖤"
]

# Função assíncrona para simular interação da torcida
async def torcida_simulada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(respostas_torcida))
