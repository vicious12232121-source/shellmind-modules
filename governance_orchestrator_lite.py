# governance_orchestrator_lite.py
# 輕量級模組治理指揮器（不含 fallback）

class GovernanceOrchestratorLite:
    def __init__(self, modules):
        self.modules = modules

    def dispatch(self, module_name, payload):
        if module_name in self.modules:
            return self.modules[module_name].run(payload)
        return {"error": "module not found"}
