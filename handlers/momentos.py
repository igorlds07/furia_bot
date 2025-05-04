import random
from telegram import Update
from telegram.ext import ContextTypes

# Lista com momentos marcantes da FURIA
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


# Handler assíncrono para o comando /momentos
async def momentos_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    momento = random.choice(momentos)

    if momento["tipo"] == "vídeo":
        await update.message.reply_text(
            f"🎥 {momento['titulo']}\nAssista esse momento épico da FURIA: {momento['url']}"
        )

    elif momento["tipo"] == "imagem":
        await update.message.reply_photo(
            momento["url"],
            caption=f"📸 {momento['titulo']}"
        )

    elif momento["tipo"] == "meme":
        await update.message.reply_text(
            f"😂 {momento['titulo']}\nConfira esse meme clássico: {momento['url']}"
        )

    elif momento["tipo"] == "destaque_jogador":
        await update.message.reply_text(
            f"💥 {momento['titulo']}\nDestaque incrível: {momento['url']}"
        )

    else:
        await update.message.reply_text("❓ Momento desconhecido. Tente novamente mais tarde.")
