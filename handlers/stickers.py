import random
from telegram import Update
from telegram.ext import CallbackContext

# Lista de stickers (mantida igual)
stickers = [
    "CAACAgEAAxkBAAEOYXpoECqW7Jct_X2u4YkCjYapc0DtSQACrAcAAnmAgUTEJUikBw9ddDYE",
    "CAACAgEAAxkBAAEOYXxoECqbRnPO29usWiL1gXYL-vNwPAAC7QUAAkKEeETexcAXvA0YkDYE",
    "CAACAgEAAxkBAAEOYX5oECqejmQTB5WUiWon0kqL5uan-wAC1gMAAqwKgURjgwxp8iFTxDYE",
    "CAACAgEAAxkBAAEOYYBoECqhPpYZ_4akeEffcdOMn8fWHQACzQYAApWegUSBrTpl8UGoaDYE",
    "CAACAgEAAxkBAAEOYYJoECtMGZB_Iq8zP1mTEf5XDXNdlAACOwYAAs0HgUTOn9nGIcrC5zYE",
    "CAACAgEAAxkBAAEOYYRoECtO5KyDjlLoGdlbrcY70om0bwAC4AoAAtj4gERgjrOurac1ezYE"
]

# Função para enviar figurinha com mensagem
def figurinhas(update: Update, context: CallbackContext):
    sticker_id = random.choice(stickers)
    update.message.reply_text("Aqui vai uma figurinha da FURIA!")
    update.message.reply_sticker(sticker_id)

# Função para enviar apenas figurinha
def mandar_figurinha(update: Update, context: CallbackContext):
    update.message.reply_sticker(random.choice(stickers))

# Lista de gritos da torcida
gritos = [
    "VAMO FURIAAAA 🔥🔥🔥",
    "DOMINA ESMAGA! 💥",
    "VAI PRA CIMA DELES FURIA! 🐆",
    "AQUI É FURIA, PORRA! 🔥💛🖤",
    "A FURIA NUNCA DESISTE!"
]

# Função para enviar grito aleatório
def gritar(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(gritos))

# Lista de respostas da torcida simulada
respostas_torcida = [
    "E aí, #FuriaNation! Como estamos para o próximo jogo? 💥",
    "Isso aí! A FURIA não vai deixar nada passar, é o momento da vitória! 🙌",
    "É isso mesmo, a torcida é o nosso combustível! Rumo ao título! 💣",
    "Vamos FURIA, é tudo nosso! 💛🖤"
]

# Função para simular interação da torcida
def torcida_simulada(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(respostas_torcida))