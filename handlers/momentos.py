import random
from telegram import Update
from telegram.ext import ContextTypes

# Lista com momentos marcantes da FURIA
# Cada item é um dicionário com tipo, título e link
momentos = [
    {
        "tipo": "vídeo",
        "titulo": "CLASSIFICAMOS NOS PLAYOFFS DA #ESLPROLEAGUE",
        "url": "https://www.youtube.com/watch?v=8aIcU-_5W34"
    },
    {
        "tipo": "meme",
        "titulo": "COMUNICAÇÃO DA FURIA NA #IEMCOLOGNE 😂",
        "url": "https://www.youtube.com/watch?v=1Xa9-wxluZY"
    },
    {
        "tipo": "destaque_jogador",
        "titulo": "KSCERATO, o monstro!",
        "url": "https://www.youtube.com/watch?v=07R2067Js8k"
    }
]


# Função que será chamada quando o usuário usar o comando /momentos
async def momentos_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Escolhe aleatoriamente um momento da lista
    momento = random.choice(momentos)

    # Se for vídeo, manda texto com link
    if momento["tipo"] == "vídeo":
        await update.message.reply_text(
            f"🎥 {momento['titulo']}\nAssista esse momento épico da FURIA: {momento['url']}"
        )

    # Se for imagem, envia como foto (não há imagem no exemplo, mas o código está preparado)
    elif momento["tipo"] == "imagem":
        await update.message.reply_photo(
            momento["url"],
            caption=f"📸 {momento['titulo']}"
        )

    # Se for meme, manda como texto com link (igual ao vídeo nesse caso)
    elif momento["tipo"] == "meme":
        await update.message.reply_text(
            f"🎥 {momento['titulo']}\nAssista esse momento épico da FURIA: {momento['url']}"
        )

    # Se for destaque de jogador, também manda texto com link
    elif momento["tipo"] == "destaque_jogador":
        await update.message.reply_text(
            f"💥 {momento['titulo']}\nConfira esse destaque incrível: {momento['url']}"
        )
