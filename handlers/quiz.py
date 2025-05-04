import random
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

# Dicionário com as perguntas separadas por categoria (FURIA, CSGO, Curiosidades)
perguntas = {
    "furia": [
            {
                "pergunta": "Quem é o atual capitão da FURIA?",
                "respostas": ["arT", "FalleN", "KSCERATO", "yuurih"],
                "resposta_certa": "arT"
            },
            {
                "pergunta": "Qual é o nome da organização de esports da FURIA?",
                "respostas": ["FURIA Esports", "FURIA Gaming", "FURIA Team", "FURIA CS"],
                "resposta_certa": "FURIA Esports"
            },
            {
                "pergunta": "Qual jogador da FURIA é conhecido pelo nickname 'KSCERATO'?",
                "respostas": ["Kaike", "Vini", "Yuurih", "KSCERATO"],
                "resposta_certa": "KSCERATO"
            },
            {
                "pergunta": "Em qual torneio a FURIA conquistou seu primeiro título de CS:GO?",
                "respostas": ["DreamHack Masters", "ESL Pro League", "IEM Katowice", "CS:GO Major"],
                "resposta_certa": "DreamHack Masters"
            },
            {
                "pergunta": "Qual é a cor predominante no logo da FURIA?",
                "respostas": ["Azul", "Vermelho", "Preto", "Amarelo"],
                "resposta_certa": "Amarelo"
            },
        ], "csgo": [
            {
                "pergunta": "Qual é o nome do mapa clássico de CS:GO com a bomba A e B?",
                "respostas": ["Dust2", "Inferno", "Mirage", "Overpass"],
                "resposta_certa": "Dust2"
            },
            {
                "pergunta": "Quantos jogadores são necessários para jogar uma partida de CS:GO?",
                "respostas": ["4", "5", "6", "7"],
                "resposta_certa": "5"
            },
            {
                "pergunta": "O que acontece quando um jogador morre em uma partida de CS:GO?",
                "respostas": ["Ele respawn imediatamente", "Ele fica espectador até a próxima rodada", "Ele é eliminado por toda a partida", "Nada, ele volta à vida"],
                "resposta_certa": "Ele fica espectador até a próxima rodada"
            },
            {
                "pergunta": "Quantos tipos de granadas existem em CS:GO?",
                "respostas": ["3", "4", "5", "6"],
                "resposta_certa": "5"
            },
            {
                "pergunta": "Qual é o objetivo do time terrorista em CS:GO?",
                "respostas": ["Proteger a bomba", "Destruir o time adversário", "Colocar a bomba nos pontos A ou B", "Capturar a área de segurança"],
                "resposta_certa": "Colocar a bomba nos pontos A ou B"
            },
        ], "curiosidades": [
            {
                "pergunta": "Qual é o grito de guerra da torcida da FURIA?",
                "respostas": ["Vai FURIA", "Vamo FURIAAA", "FURIA é nossa", "A FURIA nunca desiste"],
                "resposta_certa": "Vamo FURIAAA"
            },
            {
                "pergunta": "Em qual ano a FURIA foi fundada?",
                "respostas": ["2015", "2016", "2017", "2018"],
                "resposta_certa": "2015"
            },
            {
                "pergunta": "Qual é a mascote da FURIA?",
                "respostas": ["Pantera", "Falcão", "Leão", "Águia"],
                "resposta_certa": "Falcão"
            },
            {
                "pergunta": "Qual foi o primeiro torneio internacional que a FURIA jogou?",
                "respostas": ["ESL One Cologne", "DreamHack Masters", "IEM Katowice", "ESL Pro League"],
                "resposta_certa": "IEM Katowice"
            },
            {
                "pergunta": "A FURIA é considerada uma das melhores equipes de CS:GO de qual país?",
                "respostas": ["Brasil", "Argentina", "Chile", "Portugal"],
                "resposta_certa": "Brasil"
            },
        ]
    }

# Definição de estado para o ConversationHandler
PERGUNTA = 1
usuario_pontos = {}   # Armazena a pontuação de cada usuário
usuario_pergunta_index = {}    # Armazena qual pergunta o usuário está respondendo



async def iniciar_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)    # Pega o ID do usuário
    usuario_pontos[usuario_id] = 0    # Inicia pontuação com 0
    usuario_pergunta_index[usuario_id] = 0    # Começa pela primeira pergunta

    await update.message.reply_text(
        "🎮 Bora começar o quiz da FURIA! Responda com o número da alternativa correta.\n\n"
        "OBS.: Cada pergunta equivale a 1 ponto.\n"
        "Para cancelar o quiz digite: /cancelar"
    )

    return await enviar_pergunta(update, context)    # Envia a primeira pergunta


async def enviar_pergunta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)

    # Junta todas as perguntas de todas as categorias
    todas_perguntas = [item for sublist in perguntas.values() for item in sublist]
    pergunta_index = usuario_pergunta_index[usuario_id]

    # Se já respondeu todas, envia o feedback e encerra
    if pergunta_index >= len(todas_perguntas):
        pontos = usuario_pontos[usuario_id]
        await enviar_feedback(update, pontos)
        return ConversationHandler.END

    # Pega a pergunta atual
    pergunta_info = todas_perguntas[pergunta_index]
    
    # Formata as alternativas em formato de lista numerada
    texto_respostas = "\n".join(
        f"{i+1}. {resposta}" 
        for i, resposta in enumerate(pergunta_info["respostas"])
    )
    # Envia a pergunta com as opções
    await update.message.reply_text(
        f"{pergunta_info['pergunta']}\n{texto_respostas}"
    )

    return PERGUNTA


async def receber_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)
    texto = update.message.text.strip()   # Texto enviado pelo usuário

    todas_perguntas = [item for sublist in perguntas.values() for item in sublist]
    pergunta_index = usuario_pergunta_index[usuario_id]
    pergunta_info = todas_perguntas[pergunta_index]

    # Se o usuário não digitou um número
    if not texto.isdigit():
        await update.message.reply_text("Por favor, envie apenas o número da resposta! 📩")
        return PERGUNTA

    escolha = int(texto)
    
    if escolha < 1 or escolha > len(pergunta_info["respostas"]):
        await update.message.reply_text("Escolha um número válido entre 1 e 4! 🔢")
        return PERGUNTA

    if pergunta_info["respostas"][escolha-1] == pergunta_info["resposta_certa"]:
        usuario_pontos[usuario_id] += 1

    usuario_pergunta_index[usuario_id] += 1
    return await enviar_pergunta(update, context)


async def enviar_feedback(update: Update, pontos: int) -> None:
    total_perguntas = len([item for sublist in perguntas.values() for item in sublist])

    if pontos == total_perguntas:
        feedback = f"🏆 Parabéns! Você acertou todas! Fez {pontos} ponto(s)! \nÉ sinal de que você é um torcedor raiz! 💛🖤"
    elif pontos >= total_perguntas * 0.7:
        feedback = f"👏 Muito bem! Você fez {pontos} ponto(s) de {total_perguntas}! Você conhece bastante a FURIA!"
    elif pontos >= total_perguntas * 0.4:
        feedback = f"🔍 Você fez {pontos} ponto(s) de {total_perguntas}. Ainda dá pra melhorar, continue acompanhando a FURIA!"
    else:
        feedback = f"😅 Você fez apenas {pontos} ponto(s) de {total_perguntas}. Tá na hora de estudar mais sobre a FURIA!"

    await update.message.reply_text(feedback)
    

async def cancelar_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)
    pontos = usuario_pontos.get(usuario_id, 0)
    total_perguntas = len([item for sublist in perguntas.values() for item in sublist])

    if pontos == total_perguntas:
        feedback = f"🏆 Parabéns! Acertou todas! {pontos} pontos! \nTorcedor raiz!💛🖤"
    else:
        feedback = f"🎯 Você fez {pontos} ponto(s). Tente novamente! 💛🖤"

    await update.message.reply_text(f"Quiz cancelado! {feedback}")
    return ConversationHandler.END
