# 🐾 PetHelpful - Chatbot para Cuidados com Pets

Um chatbot inteligente desenvolvido em Python que utiliza IA generativa (Google Gemini) para fornecer orientações sobre cuidados com pets. Projeto criado com foco em boas práticas de desenvolvimento e segurança.

## ✨ Funcionalidades

- 🤖 **IA Especializada**: Respostas contextualizadas sobre cuidados com cães e gatos
- 🔒 **Segurança**: Configuração segura de API keys
- 📜 **Histórico**: Acompanhe suas conversas anteriores
- 🎨 **Interface Visual**: Layout elegante no terminal
- 💡 **Respostas Concisas**: Informações diretas e práticas

## 🚀 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusQuintanilhaa/chatbot-pethelful.git
cd chatbot-pethelful
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure sua API Key

```bash
# Copie o arquivo de exemplo
copy config_api_example.py config_api.py

# Edite config_api.py e adicione sua chave do Google Gemini
# Obtenha sua chave em: https://aistudio.google.com/app/apikey
```

### 4. Execute o chatbot

```bash
python script.py
```

## 🔧 Estrutura do Projeto

```text
pethelpful/
├── script.py                 # Aplicação principal
├── config_api_example.py     # Exemplo de configuração
├── config_api.py            # Sua configuração (não versionado)
├── requirements.txt          # Dependências Python
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Documentação
```

## 🛡️ Segurança

- ✅ **API Key protegida**: Arquivo `config_api.py` não é versionado
- ✅ **Exemplo fornecido**: Template em `config_api_example.py`
- ✅ **Validação**: Verificação de configuração na inicialização

### ⚠️ Checklist de Segurança

- [ ] Copiei `config_api_example.py` para `config_api.py`
- [ ] Adicionei minha chave real em `config_api.py`
- [ ] Verifiquei que `config_api.py` está no `.gitignore`
- [ ] **NUNCA** commitei minha chave real no Git

## 💡 Exemplos de Uso

```text
👤 Você: Meu cachorro não quer comer
🤖 Bot: Isso pode ter várias causas. Verifique se a ração não estragou, 
        tente mudar o horário da alimentação e observe se há outros 
        sintomas. Se persistir por mais de 24h, consulte um veterinário.

👤 Você: Como dar banho em gato?
🤖 Bot: Use água morna, shampoo específico para gatos e seja muito 
        gentil. Prepare tudo antes, mantenha calmo e recompense após. 
        Muitos gatos se limpam sozinhos, então só é necessário se 
        estiver muito sujo.
```

## 🎯 Comandos Especiais

- `historico` - Ver conversas anteriores
- `sair` ou `exit` - Encerrar o chat

## 🛠️ Tecnologias

- **Python 3.8+**: Linguagem principal
- **Google Generative AI**: Modelo Gemini 1.5 Flash
- **Type Hints**: Código mais legível e maintível
- **Tratamento de Erros**: Experiência robusta do usuário

## 📝 Desenvolvimento

Este projeto demonstra:

- Integração com APIs de IA
- Boas práticas de segurança
- Estrutura de código profissional
- Documentação completa
- Controle de versão com Git

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

💙 **Desenvolvido com carinho para ajudar você a cuidar melhor do seu pet!**
