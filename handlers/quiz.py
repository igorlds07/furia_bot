import random
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

# Dados das perguntas
perguntas = {
    "furia": [
        {
            "pergunta": "Quem é o atual capitão da FURIA?",
            "respostas": ["arT", "FalleN", "KSCERATO", "yuurih"],
            "resposta_certa": "arT"
        },
        # Outras perguntas aqui...
    ],
}

# Estados do ConversationHandler
PERGUNTA = 1
usuario_pontos = {}
usuario_pergunta_index = {}

async def iniciar_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)
    usuario_pontos[usuario_id] = 0
    usuario_pergunta_index[usuario_id] = 0

    await update.message.reply_text(
        "🎮 Bora começar o quiz da FURIA! Responda com o número da alternativa correta.\n\n"
        "OBS.: Cada pergunta equivale a 1 ponto.\n"
        "Para cancelar o quiz digite: /cancelar"
    )

    return await enviar_pergunta(update, context)

async def enviar_pergunta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)
    todas_perguntas = [item for sublist in perguntas.values() for item in sublist]
    pergunta_index = usuario_pergunta_index[usuario_id]

    if pergunta_index >= len(todas_perguntas):
        pontos = usuario_pontos[usuario_id]
        await enviar_feedback(update, pontos)
        return ConversationHandler.END

    pergunta_info = todas_perguntas[pergunta_index]
    texto_respostas = "\n".join(
        f"{i+1}. {resposta}" 
        for i, resposta in enumerate(pergunta_info["respostas"])
    )

    await update.message.reply_text(
        f"{pergunta_info['pergunta']}\n{texto_respostas}"
    )

    return PERGUNTA

async def receber_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuario_id = str(update.effective_user.id)
    texto = update.message.text.strip()

    todas_perguntas = [item for sublist in perguntas.values() for item in sublist]
    pergunta_index = usuario_pergunta_index[usuario_id]
    pergunta_info = todas_perguntas[pergunta_index]

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
        feedback = f"🏆 Parabéns! Você acertou todas! Fez {pontos} pontos! \né sinal de que você é um Torcedor raiz!💛🖤"
    else:
        feedback = f"🎯 Você fez {pontos} ponto(s). Que tal tentar de novo? O time conta com você! 💛🖤"

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
