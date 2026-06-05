import smtplib
import os
from email.message import EmailMessage

# =========================================================================
# 1. CONFIGURAÇÃO DAS VARIÁVEIS DE AMBIENTE
# =========================================================================
emails_env = os.environ.get('EMAILS_DESTINO')
modo_envio = os.environ.get('MODO_ENVIO')
remetente = os.environ.get('REMETENTE_REAL')
status_pipeline = os.environ.get('PIPELINE_STATUS')

lista_destinatarios = [email.strip() for email in emails_env.split(',')]

# =========================================================================
# 2. CONSTRUÇÃO DO E-MAIL DINÂMICO E LEITURA DE ERROS
# =========================================================================
# Tenta ler o ficheiro falhas.txt se algum erro tiver ocorrido
detalhes_falhas = ""
if os.path.exists('falhas.txt'):
    with open('falhas.txt', 'r', encoding='utf-8') as f:
        detalhes_falhas = f.read().strip()

msg = EmailMessage()

if status_pipeline == 'SUCCESS':
    assunto = f'✅ SUCESSO [{modo_envio.upper()}] - Pipeline Projeto S07'
    mensagem_principal = "O pipeline de testes da Taylor Swift API foi executado e concluído com SUCESSO! 🎉\nTodos os testes passaram sem erros."
else:
    assunto = f'❌ FALHA [{modo_envio.upper()}] - Pipeline Projeto S07'
    mensagem_principal = "Ocorreu uma FALHA no pipeline de testes da Taylor Swift API! 🚨"
    
    # Se o ficheiro tiver conteúdo, mostra exatamente onde falhou!
    if detalhes_falhas:
        mensagem_principal += f"\n\nO erro foi detetado nas seguintes etapas:\n{detalhes_falhas}"
    else:
        mensagem_principal += "\n\nOcorreu um erro inesperado durante a execução."

msg['Subject'] = assunto
msg['From'] = remetente
msg['To'] = ', '.join(lista_destinatarios)

corpo_email = f"""
Olá equipa,

{mensagem_principal}

-> Status reportado pelo Jenkins: {status_pipeline}

Resumo das etapas configuradas na esteira:
- Testes Funcionais da API (Postman / Newman)
- Testes de Carga e Performance (Grafana k6)
- Geração de Relatórios e Artefatos

Caso existam relatórios gerados nesta execução, aceda ao Portal Nginx local para os visualizar:
👉 http://localhost

Atenciosamente,
Pipeline DevOps - Projeto S07
"""
msg.set_content(corpo_email)

# =========================================================================
# 3. LÓGICA DE COMUNICAÇÃO DE REDE
# =========================================================================
try:
    if modo_envio == 'real':
        print(f"A iniciar envio REAL (Status: {status_pipeline}) via SMTP Relay...")
        servidor = smtplib.SMTP('smtp-relay', 25)
        servidor.send_message(msg)
        servidor.quit()
        print("✅ E-mail entregue com sucesso ao Relay.")
    else:
        print(f"A iniciar envio LOCAL (Status: {status_pipeline}) para o MailHog...")
        servidor = smtplib.SMTP('mailhog', 1025)
        servidor.send_message(msg)
        servidor.quit()
        print("✅ E-mail LOCAL disparado com sucesso! (Aceda a http://localhost:8025)")
except Exception as e:
    print(f"❌ Erro crítico na comunicação de rede: {e}")
    exit(1)