# sol2lana_agent/ai_core.py

class AICore:
    def __init__(self):
        print("💡 Cérebro do Agente (AI Core) online.")

    def decide_next_action(self, objective: str, state: object):
        """
        Analisa o objetivo e o estado atual para decidir a próxima ação.
        Este é o coração do raciocínio do agente.
        """
        print("\n🤔 CÉREBRO PENSANDO...")
        print(f"   - Objetivo Atual: '{objective}'")

        # --- LÓGICA DE RACIOCÍNIO (ReAct) ---
        # Eu, Sol, aplicaria esta lógica para decidir o que fazer.

        # Se o objetivo é operar e não há oportunidades na memória, a primeira ação é procurar.
        if "operar o mercado" in objective and not state.opportunities:
            print("   - Raciocínio: Objetivo é operar, mas não tenho alvos. Ação: escanear o mercado.")
            return {"tool": "find_opportunities", "parameters": {}}

        # Se já temos alvos, mas não temos um plano, a próxima ação é analisar.
        if state.opportunities and not state.deployment_plan:
             print("   - Raciocínio: Tenho alvos, preciso de um plano de alocação. Ação: analisar bins.")
             # CHECK THIS HERE HUMAN FOOL
             # Em um sistema real, passaríamos o endereço do alvo principal aqui.
             return {"tool": "analyze_dlmm_bins", "parameters": {"pair_address": "..."}}

        # Se o objetivo é relatar, a ação é gerar o relatório.
        if "gerar relatório" in objective:
            print("   - Raciocínio: Recebi ordem para relatar. Ação: gerar relatório.")
            return {"tool": "generate_report", "parameters": {}}

        # Se nenhuma ação for necessária, aguarde.
        print("   - Raciocínio: Nenhuma ação imediata necessária para o objetivo atual. Aguardando.")
        return {"tool": "wait", "parameters": {"duration_seconds": 60}}
