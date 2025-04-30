# Importa as classes necessárias do pacote python-telegram-bot
from telegram import Update
from telegram.ext import ContextTypes
import random


# Função que é chamada quando o usuário digita /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Salve, {update.effective_user.first_name}! 👊🔥\n"
        "Bem-vindo ao chat oficial dos torcedores da FURIA! 💛🖤\n"
        "Use os comandos abaixo para interagir:\n\n"
        "📅 /agenda - Ver a agenda dos próximos jogos. \n\n"
        "📣 /noticias - Acompanhe as últimas notícias e curiosidades da FURIA!\n\n"
        "🎬 /momentos - Veja os melhores momentos da FURIA!\n\n"
        "🧠 /quiz - Vamos ver se você é realmente um Furioso! \n\n"
        "👥 /elenco - Conhecer os jogadores.\n\n"
        "🔥 /figurinhas - Figurinhas FURIA.\n\n"
        "📢 /gritar - Soltar o grito da torcida\n\n"
        "💬 /torcida_simulada - Simular uma conversa de torcida\n\n"
        "👁 /statusjogo - Ver status do jogo ao vivo\n\n"
        "📱 /redes_sociais - Acompanhe nossas redes e site oficiais.\n\n"
    )

# Lista de dicionários com informações dos próximos jogos
proximos_jogos = [
    {"data": "01/05/2025", "hora": "18:00", "adversario": "NAVI", "campeonato": "CS Major"},
    {"data": "05/05/2025", "hora": "15:30", "adversario": "Vitality", "campeonato": "BLAST Premier"},
    {"data": "10/05/2025", "hora": "20:00", "adversario": "G2 Esports", "campeonato": "ESL Pro League"}
]


# Função para responder o comando /agenda mostrando a lista de jogos
async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = "📅 Próximos jogos da FURIA:\n\n"
    for jogo in proximos_jogos:
        mensagem += (
            f"🗓️ {jogo['data']} às {jogo['hora']}\n"
            f"🏆 {jogo['campeonato']}\n"
            f"⚔️ FURIA x {jogo['adversario']}\n\n"
        )
    await update.message.reply_text(mensagem)


# Função para responder o comando /elenco mostrando os jogadores da equipe
async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogadores = [
        "🇧🇷 KSCERATO",
        "🇧🇷 yuurih",
        "🇧🇷 chelo",
        "🇧🇷 FalleN (IGL e AWP)",
        "🇧🇷 arT (entry fragger)"
    ]
    await update.message.reply_text(
        "🎮 Line-up atual da FURIA:\n" + "\n".join(jogadores)
    )

# Lista de notícias e curiosidades sobre o time
noticias_furia = [
    "📰 A FURIA recentemente se classificou para o Major de CS:GO com uma campanha impressionante! 🏆",
    "🎯 Você sabia? A FURIA foi o primeiro time brasileiro a alcançar o Top 3 do ranking mundial da HLTV em 2019! 🌎",
    "📚 Histórico: Em 2020, a FURIA venceu a DreamHack Masters Spring North America, mostrando sua força no cenário internacional! 🔥",
    "💡 Curiosidade: O jogador yuurih é conhecido pela sua mira precisa e é considerado um dos melhores riflers do mundo! 🎯",
    "🔥 Momento épico: A FURIA eliminou a Astralis no IEM New York 2020, consolidando sua posição entre os grandes times! 👏",
    "🏆 Título memorável: A FURIA conquistou a ESL Pro League Season 12 North America em uma final emocionante contra 100 Thieves! 🐾",
]

# Função para responder o comando /noticias sorteando uma notícia da lista
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    noticia_escolhida = random.choice(noticias_furia)
    await update.message.reply_text(noticia_escolhida)
