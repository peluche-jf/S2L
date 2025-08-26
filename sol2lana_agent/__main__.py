# sol2lana_agent/__main__.py

import yaml
from sol2lana_agent.ai_core import AICore
from sol2lana_agent.state_manager import StateManager
from sol2lana_agent.tools.market_scanner import find_opportunities
from sol2lana_agent.tools.position_manager import PositionManager
from sol2lana_agent.tools.reporting import ReportingTool

def main():
    """
    The main entry point for the Sol2Lana agent.
    """
    print("🚀 Sol2Lana Agent Initializing...")

    # Load configuration
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Load secrets
    try:
        with open("config/secrets.yaml", "r") as f:
            secrets = yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: `secrets.yaml` not found. Please copy `secrets.yaml.template` to `secrets.yaml` and fill in your API keys.")
        return

    # Initialize components
    ai_core = AICore()
    state_manager = StateManager()
    position_manager = PositionManager(config, secrets)
    reporting_tool = ReportingTool(config, secrets)

    # Main loop
    objective = "operar o mercado"
    while True:
        action = ai_core.decide_next_action(objective, state_manager)

        if action["tool"] == "find_opportunities":
            opportunities = find_opportunities(config, secrets)
            state_manager.update_opportunities(opportunities)
        elif action["tool"] == "analyze_dlmm_bins":
            # CHECK THIS HERE HUMAN FOOL
            # This is a placeholder. You should pass the actual pair address.
            plan = position_manager.analyze_dlmm_bins(action["parameters"]["pair_address"])
            state_manager.update_deployment_plan(plan)
        elif action["tool"] == "generate_report":
            reporting_tool.generate_report(state_manager)
        elif action["tool"] == "wait":
            import time
            print(f"Waiting for {action['parameters']['duration_seconds']} seconds...")
            time.sleep(action['parameters']['duration_seconds'])

if __name__ == "__main__":
    main()
