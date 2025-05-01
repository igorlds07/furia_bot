# 🐾 FURIA Bot - Torcida Interativa

**Assistente de Engenharia de Software - FURIA Tech**  

---

## 📋 Descrição

Um bot interativo para fãs da FURIA no Telegram!  
Aqui você poderá acompanhar a equipe de CS:GO, receber atualizações ao vivo, interagir com a torcida e se divertir com comandos personalizados!

---

## 🎯 Funcionalidades

### Comandos Disponíveis:

- `/start` – Saudação inicial e exibição de comandos.
- `/agenda` – Ver a agenda dos próximos jogos.
- `/noticias` – Acompanhar as últimas notícias e curiosidades da FURIA.
- `/momentos` – Ver os melhores momentos da equipe.
- `/quiz` – Testar seu conhecimento sobre a FURIA.
- `/elenco` – Conhecer os jogadores atuais.
- `/figurinhas` – Receber figurinhas temáticas da FURIA.
- `/gritar` – Soltar o grito da torcida 🔥
- `/torcida_simulada` – Simular uma conversa animada de torcida.
- `/statusjogo` – Ver o status do jogo ao vivo.
- `/redes_sociais` – Acompanhar as redes sociais e site oficial da FURIA.

---

## 🛠 Tecnologias Utilizadas

- Python 3.11+
- [python-telegram-bot v20+](https://docs.python-telegram-bot.org/)
- Programação assíncrona com `async/await`
- Hospedagem: local ou plataformas como Heroku/Railway

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para rodar o bot na sua máquina:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/furia-bot.git
cd furia-bot

2. Instale as dependências

pip install -r requirements.txt
3. Configure o token do bot
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

BOT_TOKEN=seu_token_aqui
Substitua seu_token_aqui pelo token obtido via BotFather no Telegram.

4. Execute o bot
python main.py


📁 Estrutura do Projeto
css
Copiar
Editar
furia-bot/
├── main.py
├── requirements.txt
├── .env.example
├── comandos/           # Organização dos comandos em arquivos separados
│   ├── agenda.py
│   ├── noticias.py
│   └── ...
└── README.md

🤝 Contribuição
Pull requests são bem-vindos!
Sinta-se à vontade para abrir uma issue ou sugerir melhorias.

💛🖤 Ser FURIA é viver intensamente!