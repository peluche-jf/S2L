# sol2lana_agent/state_manager.py

# CHECK THIS HERE HUMAN FOOL
# This is a placeholder for the state manager.
# You should implement the logic for managing the state of the agent.

class StateManager:
    def __init__(self):
        self.opportunities = []
        self.deployment_plan = None
        self.positions = []
        print("🧠 State Manager online.")

    def update_opportunities(self, opportunities):
        self.opportunities = opportunities

    def update_deployment_plan(self, plan):
        self.deployment_plan = plan

    def update_positions(self, positions):
        self.positions = positions
