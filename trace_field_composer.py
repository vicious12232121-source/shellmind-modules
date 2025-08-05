# trace_field_composer.py
# 建構模組 trace DAG 主骨架

class TraceFieldComposer:
    def __init__(self):
        self.trace_chain = []

    def add_node(self, node_id, description, dependencies=None):
        self.trace_chain.append({
            "id": node_id,
            "desc": description,
            "deps": dependencies or []
        })

    def export_dag(self):
        return self.trace_chain
