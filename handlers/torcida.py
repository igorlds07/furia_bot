import random
from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime
import time  # Substitui o asyncio.sleep

# Variável global mantida
ultimo_status = None

# --- Função da Torcida Simulada (síncrona) ---
def torcida_simulada(update: Update, context: CallbackContext):
    respostas_torcida = [
        "E aí, #FuriaNation! Como estamos para o próximo jogo? 💥",
        "Isso aí! A FURIA não vai deixar nada passar, é o momento da vitória! 🙌",
        "É isso mesmo, a torcida é o nosso combustível! Rumo ao título! 💣",
        "Vamos FURIA, é tudo nosso! 💛🖤",
        "Ninguém segura a FURIAAAA! 🚀",
        "TRADIÇÃO, RAÇA E FÉ! 🔥",
        "HOJE É DIA DE FURIAAAAAA! 💛🖤",
    ]

    mensagens = random.sample(respostas_torcida, k=5)
    
    for mensagem in mensagens:
        update.message.reply_text(mensagem)
        time.sleep(5)  # Usando time.sleep em vez de asyncio.sleep

# --- Função de Status do Jogo (síncrona) ---
def status_jogo(update: Update, context: CallbackContext):
    global ultimo_status

    adversarios = ["NAVI", "Vitality", "G2 Esports", "FaZe Clan", "Team Liquid"]
    mapas = ["Mirage", "Inferno", "Ancient", "Overpass", "Vertigo"]

    if not ultimo_status or random.choice([True, False]):
        placar_furia = random.randint(0, 16)
        placar_adversario = random.randint(0, 16)

        situacoes = [
            f"🏁 **Jogo ao vivo**: FURIA {placar_furia} x {placar_adversario} {random.choice(adversarios)}\n"
            f"🗺️ Mapa: {random.choice(mapas)}\n"
            f"⏱️ Round atual: {random.randint(1, 30)}\n\n"
            f"{'🔥 FURIA dominando!' if placar_furia > placar_adversario else '⚡ Virando o jogo!'}",

            f"🎮 **Última atualização**:\n"
            f"FURIA {placar_furia} x {placar_adversario} {random.choice(adversarios)}\n"
            f"💥 Melhor jogador: KSCERATO ({random.randint(15, 30)} kills)\n\n"
            f"Próximo mapa: {random.choice(mapas)}"
        ]

        hora_atual = datetime.now().strftime("%H:%M")
        ultimo_status = f"🕒 Atualizado em {hora_atual}\n\n" + random.choice(situacoes)

    update.message.reply_text(ultimo_status, parse_mode="Markdown")

# --- Resposta Livre (síncrona) ---
def resposta_livre(update: Update, context: CallbackContext):
    frases = [
        "FURIA é emoção do começo ao fim! 😎",
        "Você viu aquele clutch do KSCERATO? Incrível!",
        "Torcer pra FURIA é torcer com o coração 💛🖤",
        "Bora pra mais um highlight 🔥"
    ]
    update.message.reply_text(random.choice(frases))