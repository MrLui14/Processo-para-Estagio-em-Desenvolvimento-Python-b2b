# Integração Supabase + Z-API 🚀

Projeto em Python para leitura de contatos em um banco de dados Supabase e envio de mensagens automatizadas no WhatsApp utilizando a Z-API.

## 📋 Setup da Tabela no Supabase

Crie uma tabela chamada `contatos` no seu projeto do Supabase com as seguintes colunas:
- `id` (int8, chave primária)
- `nome` (text) - Nome do contato para personalização.
- `telefone` (text) - Número do WhatsApp com DDI e DDD (ex: `5511999999999`).

Insira até 3 registros para testar a aplicação.

## ⚙️ Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto, usando o arquivo `.env.example` como base. Preencha com as suas credenciais:

- **SUPABASE_URL** e **SUPABASE_KEY**: Disponíveis em *Project Settings > API* no Supabase.
- **ZAPI_INSTANCE** e **ZAPI_TOKEN**: Disponíveis na dashboard da sua instância na Z-API.

## 🚀 Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO