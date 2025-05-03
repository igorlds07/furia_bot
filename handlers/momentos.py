import random
from telegram import Update
from telegram.ext import CallbackContext

# Lista com momentos marcantes da FURIA (mantida igual)
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

# Função síncrona para o comando /momentos
def momentos_furia(update: Update, context: CallbackContext):
    # Escolhe aleatoriamente um momento
    momento = random.choice(momentos)
    
    # Monta a resposta baseada no tipo
    if momento["tipo"] == "vídeo":
        update.message.reply_text(
            f"🎥 {momento['titulo']}\nAssista esse momento épico da FURIA: {momento['url']}"
        )
    
    elif momento["tipo"] == "imagem":
        update.message.reply_photo(
            momento["url"],
            caption=f"📸 {momento['titulo']}"
        )
    
    elif momento["tipo"] == "meme":
        update.message.reply_text(
            f"😂 {momento['titulo']}\nConfira esse meme clássico: {momento['url']}"
        )
    
    elif momento["tipo"] == "destaque_jogador":
        update.message.reply_text(
            f"💥 {momento['titulo']}\nDestaque incrível: {momento['url']}"
        )