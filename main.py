import logging
import nest_asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from dotenv import load_dotenv
import os

import asyncio

# Importação dos handlers (funções de comandos e interações)
from handlers.commands import start, agenda, elenco, noticias
from handlers.stickers import gritar, figurinhas
from handlers.torcida import torcida_simulada, status_jogo, resposta_livre
from handlers.quiz import iniciar_quiz, cancelar_quiz, PERGUNTA, receber_resposta
from handlers.redes_sociais import redes_sociais
from handlers.momentos import momentos_furia


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Carrega o token do bot a partir do arquivo .env
TOKEN = os.getenv("TOKEN")

# Patch para rodar asyncio corretamente em cima de outro asyncio já em execução (necessário para o Telegram bot)
nest_asyncio.apply()

# Configuração do logging para monitorar o funcionamento do bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# Função principal do bot
async def main():
    # Cria a aplicação do bot usando o token
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona handlers para os comandos do bot (comandos como /start, /agenda, etc.)
    app.add_handler(CommandHandler("start", start))  # Comando /start
    app.add_handler(CommandHandler("agenda", agenda))  # Comando /agenda
    app.add_handler(CommandHandler("elenco", elenco))  # Comando /elenco
    app.add_handler(CommandHandler("gritar", gritar))  # Comando /gritar
    app.add_handler(CommandHandler("torcida_simulada", torcida_simulada))  # Comando /torcida_simulada
    app.add_handler(CommandHandler("momentos", momentos_furia))  # Comando /momentos

    # Cria o conversacional handler para o quiz, com pontos de entrada e respostas de estado
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("quiz", iniciar_quiz)],  # Comando /quiz inicia o quiz
        states={  # Quando estiver no estado da pergunta, o bot vai esperar por uma resposta
            PERGUNTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_resposta)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar_quiz)],  # Comando para cancelar o quiz
    ))
    app.add_handler(CommandHandler("figurinhas", figurinhas))  # Comando /figurinhas
    app.add_handler(CommandHandler("statusjogo", status_jogo))  # Comando /statusjogo
    app.add_handler(CommandHandler("redes_sociais", redes_sociais))  # Comando /redes_sociais
    app.add_handler(CommandHandler("noticias", noticias))  # Comando /noticias

    # Adiciona um handler para mensagens de texto gerais (não comandos)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_livre))  # Respostas livres para o bot

    # Exibe uma mensagem no console para informar que o bot está rodando
    print("Bot da FURIA rodando no Telegram! ⚡")

    # Inicia o polling do bot para ficar esperando por novas mensagens
    await app.run_polling()


if __name__ == "__main__":
    # Rodando a função assíncrona principal usando asyncio.run
    asyncio.run(main())
    
