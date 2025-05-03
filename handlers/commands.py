from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random


# Seu código original com mínimas alterações async
proximos_jogos = [
    {"data": "01/05/2025", "hora": "18:00", "adversario": "NAVI", "campeonato": "CS Major"},
    {"data": "05/05/2025", "hora": "15:30", "adversario": "Vitality", "campeonato": "BLAST Premier"},
    {"data": "10/05/2025", "hora": "20:00", "adversario": "G2 Esports", "campeonato": "ESL Pro League"}
]

noticias_furia = [
    "📰 A FURIA classificou-se para o Major de CS:GO! 🏆",
    "🎯 FURIA: primeiro time BR no Top 3 mundial (2019)! 🌎",
    "📚 Venceu DreamHack Masters Spring NA 2020! 🔥",
    "💡 yuurih: um dos melhores riflers do mundo! 🎯",
    "🔥 Eliminou a Astralis no IEM NY 2020! 👏",
    "🏆 Campeã ESL Pro League S12 NA! 🐾"
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Salve, {update.effective_user.first_name}! 👊🔥\n"
        "Bem-vindo ao chat oficial dos torcedores da FURIA! 💛🖤\n"
        "Use os comandos abaixo para interagir:\n\n"
        "📅 /agenda - Ver a agenda dos próximos jogos\n\n"
        "📣 /noticias - Últimas notícias da FURIA\n\n"
        "🎬 /momentos - Melhores momentos\n\n"
        "🧠 /quiz - Teste seu conhecimento\n\n"
        "👥 /elenco - Conheça os jogadores\n\n"
        "🔥 /figurinhas - Figurinhas FURIA\n\n"
        "📢 /gritar - Grito da torcida\n\n"
        "💬 /torcida_simulada - Simule conversa de torcida\n\n"
        "👁 /statusjogo - Status do jogo ao vivo\n\n"
        "📱 /redes_sociais - Nossas redes sociais\n\n"
    )


async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = "📅 Próximos jogos da FURIA:\n\n"
    for jogo in proximos_jogos:
        mensagem += (
            f"🗓️ {jogo['data']} às {jogo['hora']}\n"
            f"🏆 {jogo['campeonato']}\n"
            f"⚔️ FURIA x {jogo['adversario']}\n\n"
        )
    await update.message.reply_text(mensagem)


async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogadores = [
        "🇧🇷 KSCERATO",
        "🇧🇷 yuurih",
        "🇧🇷 chelo",
        "🇧🇷 FalleN (IGL e AWP)",
        "🇧🇷 arT (entry fragger)"
    ]
    await update.message.reply_text("🎮 Line-up atual da FURIA:\n" + "\n".join(jogadores))

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    noticia_escolhida = random.choice(noticias_furia)
    await update.message.reply_text(noticia_escolhida)
