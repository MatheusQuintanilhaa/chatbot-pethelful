# 🐾 Chatbot Petlove - Projeto de Estágio

Um chatbot simples feito com Python e Google Gemini AI para ajudar donos de pets!

## 💡 Por que criei isto?

Vi a vaga de estágio na Petlove e quis mostrar meu interesse em **IA generativa** e **chatbots**. Mesmo sendo iniciante em Python, queria demonstrar que tenho curiosidade e vontade de aprender sobre tecnologias de IA!

## 🚀 O que o chatbot faz?

- 💬 Conversa sobre cuidados com pets (cães e gatos)
- 📚 Guarda um histórico das conversas (usando listas e dicionários)
- 🤖 Usa a API do Google Gemini para gerar respostas inteligentes
- 🐕 Foca em temas relacionados a saúde e cuidados com animais

## 📁 Estrutura do projeto

```text
chatbot-petlove/
├── script.py                 # Código principal do chatbot
├── config_api_example.py     # Exemplo de configuração (vai pro GitHub)
├── config_api.py            # Sua chave real (NÃO vai pro GitHub)
├── requirements.txt          # Dependência: google-generativeai
├── .gitignore               # Proteção de arquivos sensíveis
└── README.md                # Esta documentação
```

## 🛠️ Como executar

### Pré-requisitos

- Python 3.8 ou superior
- Chave da API do Google Gemini ([obter aqui](https://aistudio.google.com/app/apikey))

### Passos para executar

1. **Baixar o projeto**

```bash
git clone https://github.com/MatheusQuintanilhaa/chatbot-petlove-estagio.git
cd chatbot-petlove-estagio
```

2. **Instalar a biblioteca necessária**

```bash
pip install google-generativeai
```

3. **Configurar a API Key (SEGURO)**

```bash
# Copie o arquivo de exemplo
cp config_api_example.py config_api.py

# Edite config_api.py e substitua por sua chave real
# GOOGLE_API_KEY = "sua_chave_aqui"
```

4. **Executar o chatbot**

```bash
python script.py
```

**🔒 SEGURANÇA GARANTIDA:**

- Sua chave fica em `config_api.py` (protegido pelo .gitignore)
- O arquivo nunca será enviado para o GitHub
- Código principal (`script.py`) fica limpo e seguro

## 🎯 Conceitos Python que usei

Como estou aprendendo Python, pratiquei:

- **Funções**: `configurar_gemini()`, `criar_prompt_pet()`
- **Listas**: para guardar o histórico de conversas
- **Dicionários**: para organizar perguntas e respostas
- **Loops**: `while True` para manter o chat funcionando
- **Condicionais**: `if/else` para comandos especiais
- **Tratamento de erros**: `try/except` básico
- **APIs**: conexão com Google Gemini AI

## 💭 Exemplo de uso

```text
🐾 === CHATBOT PETLOVE === 🐾
👤 Você: Meu gato está bebendo muita água, é normal?

🤖 Bot: Beber muita água pode indicar alguns problemas de saúde
como diabetes ou problemas renais. É importante observar outros
sintomas e consultar um veterinário...

👤 Você: historico
📜 === HISTÓRICO ===
1. Você: Meu gato está bebendo muita água, é normal?
   Bot: Beber muita água pode indicar alguns problemas...
```

## 🎓 O que aprendi fazendo este projeto

- Como conectar com APIs de IA generativa
- Conceitos básicos de LLMs (Large Language Models)
- Estruturação de código Python mais organizada
- Como criar prompts efetivos para IA
- Manipulação de dados com listas e dicionários

## 🚧 Próximos passos (se eu conseguir o estágio! 😊)

- Aprender mais sobre LangChain
- Melhorar o tratamento de erros
- Adicionar mais funcionalidades pet-friendly
- Estudar sobre RAG (Retrieval-Augmented Generation)

## 🔧 Tecnologias utilizadas

- **Python 3.8+**: Linguagem de programação
- **Google Gemini AI**: Modelo de IA generativa (gemini-1.5-flash)
- **VS Code**: Editor de código

---

**Desenvolvido por Matheus Quintanilha**

_"Onde tem pet, tem love — só falta você!"_

Este é meu primeiro projeto com IA generativa e estou muito animado para aprender mais na Petlove! 🐾
