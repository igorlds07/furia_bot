import random
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

# --- Variável Global ---
ultimo_status = None  # Variável global usada como cache para armazenar o último status do jogo


# --- Função da Torcida Simulada ---
async def torcida_simulada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Lista de mensagens aleatórias simulando frases de torcedores da FURIA
    respostas_torcida = [
        "E aí, #FuriaNation! Como estamos para o próximo jogo? 💥",
        "Isso aí! A FURIA não vai deixar nada passar, é o momento da vitória! 🙌",
        "É isso mesmo, a torcida é o nosso combustível! Rumo ao título! 💣",
        "Vamos FURIA, é tudo nosso! 💛🖤",
        "Ninguém segura a FURIAAAA! 🚀",
        "TRADIÇÃO, RAÇA E FÉ! 🔥",
        "HOJE É DIA DE FURIAAAAAA! 💛🖤",
    ]

    # Seleciona 5 frases aleatórias sem repetir
    mensagens = random.sample(respostas_torcida, k=5)

    # Envia uma mensagem a cada 5 segundos
    for mensagem in mensagens:
        await update.message.reply_text(mensagem)
        await asyncio.sleep(5)


# --- Função de Status do Jogo (com cache) ---
async def status_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ultimo_status  # Utiliza a variável global para cache

    # Dados fictícios de adversários e mapas
    adversarios = ["NAVI", "Vitality", "G2 Esports", "FaZe Clan", "Team Liquid"]
    mapas = ["Mirage", "Inferno", "Ancient", "Overpass", "Vertigo"]

    # Verifica se deve atualizar o status: se não há cache ou aleatoriamente
    if not ultimo_status or random.choice([True, False]):
        placar_furia = random.randint(0, 16)  # Placar da FURIA
        placar_adversario = random.randint(0, 16)  # Placar do adversário

        # Cria duas situações possíveis (jogo ao vivo ou resumo)
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

        # Marca o horário atual da atualização
        hora_atual = datetime.now().strftime("%H:%M")

        # Salva o status na variável global
        ultimo_status = f"🕒 Atualizado em {hora_atual}\n\n" + random.choice(situacoes)

    # Envia o status atual para o usuário
    await update.message.reply_text(ultimo_status, parse_mode="Markdown")


# --- Resposta Livre ---
async def resposta_livre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensagens genéricas sobre a FURIA
    frases = [
        "FURIA é emoção do começo ao fim! 😎",
        "Você viu aquele clutch do KSCERATO? Incrível!",
        "Torcer pra FURIA é torcer com o coração 💛🖤",
        "Bora pra mais um highlight 🔥"
    ]
    await update.message.reply_text(random.choice(frases))
