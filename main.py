import os
import sys
import logging
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

# Configuração de Logging para boas práticas e rastreabilidade
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    # 1. Carregar variáveis de ambiente
    load_dotenv()

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    zapi_instance = os.getenv("ZAPI_INSTANCE")
    zapi_token = os.getenv("ZAPI_TOKEN")

    # Validação do .env
    if not all([supabase_url, supabase_key, zapi_instance, zapi_token]):
        logging.error("Faltam variáveis de ambiente. Verifique o arquivo .env.")
        sys.exit(1)

    # 2. Conectar ao Supabase
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        logging.info("Conexão com o Supabase estabelecida com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao conectar ao Supabase: {e}")
        sys.exit(1)

    # 3. Buscar até 3 contatos na tabela 'contatos'
    try:
        response = supabase.table("contatos").select("*").limit(3).execute()
        contatos = response.data

        if not contatos:
            logging.warning("Nenhum contato encontrado no banco de dados.")
            sys.exit(0)

        logging.info(f"Encontrado(s) {len(contatos)} contato(s). Iniciando envios...")
    except Exception as e:
        logging.error(f"Erro ao buscar dados no Supabase: {e}")
        sys.exit(1)

    # 4. Configurar endpoint da Z-API
    # Verifique na sua dashboard da Z-API se a URL segue este padrão exato
    zapi_url = f"https://api.z-api.io/instances/{zapi_instance}/token/{zapi_token}/send-text"

    # 5. Enviar mensagens personalizadas
    for contato in contatos:
        nome = contato.get("nome", "Contato")
        telefone = contato.get("telefone")

        if not telefone:
            logging.warning(f"Contato {nome} sem telefone cadastrado. Ignorando.")
            continue

        mensagem = f"Olá, {nome} tudo bem com você?"
        
        payload = {
            "phone": telefone,
            "message": mensagem
        }

        try:
            res = requests.post(zapi_url, json=payload)
            res.raise_for_status() # Lança erro se o status HTTP não for 200
            logging.info(f"Sucesso: Mensagem enviada para {nome} ({telefone}).")
        except requests.exceptions.RequestException as e:
            logging.error(f"Falha: Erro ao enviar mensagem para {nome} ({telefone}): {e}")

if __name__ == "__main__":
    main()