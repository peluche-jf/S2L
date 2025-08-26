# Sol2Lana Protocol - Strategic AI Core v2.2

## Visão Geral

O Sol2Lana é um protocolo de gestão de portfólio e yield farming autônomo na blockchain Solana. Ele utiliza uma arquitetura híbrida com um Vault on-chain seguro e um Agente de IA off-chain para executar estratégias de alta complexidade, incluindo:

- **Estratégia Barbell:** Alocação de capital em um "Degen Engine" de altíssimo risco e um "BTC Stronghold" de alta segurança.
- **Acumulação de Valor:** Um flywheel onde os lucros do risco são sistematicamente convertidos e protegidos em WBTC.
- **Gestão de Risco Avançada:** Diversificação de risco, Trailing Stops Adaptativos e um mecanismo de auto-reparo para o motor de yield.
- **Governança por IA e Comunidade:** Um Agente de IA propõe otimizações que são votadas por uma DAO de elite.

---

## Arquitetura

- **On-chain (Músculos):** Vaults em Rust/Anchor na Solana.
- **Off-chain (Cérebro):** Agente de IA em Python que atua como centro de comando estratégico.
- **Interface:** Governança On-chain via staking de `$S2L` (token nativo).

---

## Primeiros Passos

1.  Clone este repositório: `git clone ...`
2.  Crie e ative um ambiente virtual: `python -m venv venv && source venv/bin/activate`
3.  Instale as dependências: `pip install -r requirements.txt`
4.  Configure suas chaves de API: Copie `config/secrets.yaml.template` para `config/secrets.yaml` e adicione suas chaves. **NÃO FAÇA COMMIT DO ARQUIVO `secrets.yaml`.**
5.  Execute o agente: `python -m sol2lana_agent`

---

## Configuração

Todos os parâmetros estratégicos (TVL mínimo, taxas, limites de bins, etc.) podem ser ajustados em `config/config.yaml` sem a necessidade de alterar o código-fonte.