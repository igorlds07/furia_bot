from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
import random


# Lista dos próximos jogos da FURIA com data, hora, adversário e campeonato
proximos_jogos = [
    {"data": "01/05/2025", "hora": "18:00", "adversario": "NAVI", "campeonato": "CS Major"},
    {"data": "05/05/2025", "hora": "15:30", "adversario": "Vitality", "campeonato": "BLAST Premier"},
    {"data": "10/05/2025", "hora": "20:00", "adversario": "G2 Esports", "campeonato": "ESL Pro League"}
]

noticias_furia = [
   # Últimas notícias (2023-2024)
    "📢 FURIA anuncia nova line-up para 2024 com reforços internacionais! 🌍",
    "🏆 Classificada para o PGL Major Copenhagen 2024 - maior torneio do ano!",
    "🔥 Vitória histórica contra NAVI no IEM Katowice 2024!",
    "💥 FalleN retorna à FURIA como coach em 2024! #LendaVoltou",
    "deckz e cz danil.molodoy se juntam à FURIA para 2025!",
    "💪 FURIA vence o campeonato de CS:GO na DreamHack 2024!",
    "🌟 KSCERATO e yuurih são os MVPs do IEM Rio 2024!"  
    # Curiosidades e conquistas
    "🎯 KSCERATO: 3º melhor jogador do mundo em 2023 pela HLTV!",
    "💡 arT revoluciona o CS com estilo agressivo de liderança!",
    "💰 Maior organização de esports do Brasil em valor de mercado!",
    "🌎 Primeiro time brasileiro a vencer um Intel Grand Slam",
    
    # Estatísticas recentes
    "📈 78% de aproveitamento em mapas de Inferno em 2024",
    "🤯 yuurih com 1.25 de rating em 2024 (top 5 mundial)",
    "🛡️ chelo com 85% de clutches vencidos no último major",
    
    # Próximos compromissos
    "🗓️ Próximo jogo: FURIA vs Vitality - BLAST Premier Spring Final",
    "✈️ Em breve: ESL Pro League Season 19 em Malta",
    
    # Curiosidades históricas
    "📅 Fundada em 2017, chegou ao top 3 mundial em apenas 2 anos!",
    "🇧🇷 Único time brasileiro a vencer um Big Event na Europa (2022)"
]


# Comando /start - Mensagem de boas-vindas
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


# Comando /elenco - Mostra a line-up atual
async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogadores = [
        "🇧🇷 KSCERATO",
        "🇧🇷 yuurih",
        "🇧🇷 chelo",
        "🇧🇷 FalleN (IGL e AWP)",
        "🇧🇷 arT (entry fragger)",
        "cz danil.molodoy ",
    ]
    await update.message.reply_text("🎮 Line-up atual da FURIA:\n" + "\n".join(jogadores))


# Comando /noticias - Mostra uma notícia aleatória e uma curiosidade
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    noticia_escolhida = random.choice(noticias_furia)
    await update.message.reply_text(noticia_escolhida)
