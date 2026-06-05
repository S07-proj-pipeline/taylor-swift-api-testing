import smtplib
import os
from email.message import EmailMessage

emails_env = os.environ.get('EMAILS_DESTINO')
modo_envio = os.environ.get('MODO_ENVIO')
remetente = os.environ.get('REMETENTE_REAL')

lista_destinatarios = [email.strip() for email in emails_env.split(',')]

msg = EmailMessage()
msg.set_content("O pipeline finalizou com sucesso!\nVerifique os relatórios no Nginx.")
msg['Subject'] = f'Notificação [{modo_envio.upper()}] - Projeto S07'
msg['From'] = remetente
msg['To'] = ', '.join(lista_destinatarios)

try:
    if modo_envio == 'real':
        # ENVIO REAL via Relay
        print("A enviar para o contentor SMTP Relay...")
        
        # O Jenkins liga-se ao contentor "smtp-relay" na porta 25 (rede interna)
        # NÃO HÁ LOGIN COM PALAVRA-PASSE AQUI! O Relay trata disso.
        servidor = smtplib.SMTP('smtp-relay', 25)
        servidor.send_message(msg)
        servidor.quit()
        
        print("E-mail entregue ao Relay.")
        
    else:
        # ENVIO LOCAL via MailHog
        print("A enviar para o contentor MailHog (Falso)...")
        
        servidor = smtplib.SMTP('mailhog', 1025)
        servidor.send_message(msg)
        servidor.quit()
        
        print("E-mail LOCAL disparado para o MailHog!")

except Exception as e:
    print(f"Erro na comunicação de rede: {e}")
    exit(1)