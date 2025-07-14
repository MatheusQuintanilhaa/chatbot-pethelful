# Chatbot Petlove - Projeto de Estágio
# Autor: Matheus Quintanilha
# Descrição: Chatbot simples usando IA generativa para cuidados com pets

import google.generativeai as genai
import os

def configurar_gemini():
    """Configura o Google Gemini com a chave da API"""
    try:
        from config_api import GOOGLE_API_KEY
        api_key = GOOGLE_API_KEY
    except ImportError:
        print("❌ Erro: Arquivo config_api.py não encontrado!")
        print("📝 Copie config_api_example.py para config_api.py")
        print("🔑 Adicione sua chave da API do Google Gemini")
        print("🔗 Obtenha sua chave em: https://aistudio.google.com/app/apikey")
        exit(1)
    
    if api_key == "SUA_CHAVE_AQUI":
        print("❌ Erro: Configure sua chave no arquivo config_api.py!")
        print("🔗 Obtenha sua chave em: https://aistudio.google.com/app/apikey")
        exit(1)
    
    genai.configure(api_key=api_key)  # type: ignore
    return genai.GenerativeModel('gemini-1.5-flash')  # type: ignore

def criar_prompt_pet(mensagem_usuario):
    """Cria um prompt especializado para respostas sobre pets"""
    contexto = """
    Você é um assistente virtual especializado em pets e cuidados com animais.
    Responda de forma amigável sobre:
    - Cuidados com cães e gatos
    - Saúde animal básica
    - Dicas de alimentação
    - Comportamento dos pets
    
    Mantenha as respostas simples e úteis para donos de pets.
    """
    return f"{contexto}\n\nPergunta: {mensagem_usuario}"

def main():
    """Função principal do chatbot"""
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 15 + "🐾 CHATBOT PETLOVE 🐾" + " " * 15 + "║")
    print("╚" + "═" * 48 + "╝")
    print("🌟 Olá! Sou um assistente virtual especializado em pets!")
    print("💡 Faça perguntas sobre cuidados com seu bichinho 🐕🐱")
    print("📝 Digite 'historico' para ver conversas anteriores")
    print("🚪 Digite 'sair' para encerrar")
    print("─" * 50 + "\n")
    
    try:
        model = configurar_gemini()
        print("✅ Chatbot iniciado com sucesso!\n")
    except Exception as e:
        print(f"❌ Erro ao iniciar: {e}")
        return
    
    historico = []
    
    while True:
        try:
            pergunta = input("👤 Você: ").strip()
            
            if pergunta.lower() in ['sair', 'exit']:
                print("\n╔" + "═" * 40 + "╗")
                print("║" + " " * 6 + "🐾 OBRIGADO POR USAR O" + " " * 7 + "║")
                print("║" + " " * 9 + "CHATBOT PETLOVE! 🐾" + " " * 9 + "║")
                print("║" + " " * 11 + "Cuide bem do seu pet!" + " " * 10 + "║")
                print("╚" + "═" * 40 + "╝")
                break
            
            if pergunta.lower() == 'historico':
                print("\n" + "═" * 60)
                print("📜 HISTÓRICO DE CONVERSAS")
                print("═" * 60)
                if not historico:
                    print("🔍 Nenhuma conversa ainda!")
                else:
                    for i, conversa in enumerate(historico, 1):
                        print(f"\n💬 Conversa {i}:")
                        print(f"👤 Você: {conversa['pergunta']}")
                        print(f"🤖 Bot: {conversa['resposta'][:80]}{'...' if len(conversa['resposta']) > 80 else ''}")
                        if i < len(historico):
                            print("─" * 40)
                print("═" * 60 + "\n")
                continue
            
            if not pergunta:
                print("💭 Digite sua pergunta...")
                continue
            
            print("🤖 Pensando...", end="", flush=True)
            prompt_completo = criar_prompt_pet(pergunta)
            response = model.generate_content(prompt_completo)
            
            # Formatação visual melhorada da resposta
            print("\r" + "╔" + "═" * 58 + "╗")
            print("║" + " " * 20 + "🤖 PETLOVE BOT" + " " * 20 + "║")
            print("╚" + "═" * 58 + "╝")
            print()
            print(f"{response.text}")
            print()
            print("─" * 60 + "\n")
            
            historico.append({
                'pergunta': pergunta,
                'resposta': response.text
            })
            
        except KeyboardInterrupt:
            print("\n\n🐾 Chat encerrado pelo usuário! Até logo! 🐾")
            print("💙 Obrigado por testar o Chatbot Petlove!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")
            print("Tente novamente...\n")

if __name__ == "__main__":
    main()
