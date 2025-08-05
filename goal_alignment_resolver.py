# goal_alignment_resolver.py
# 根據偏好或偏差條件對齊目標與模組調用行為

class GoalAlignmentResolver:
    def __init__(self, preference_graph):
        self.graph = preference_graph

    def resolve(self, claim):
        return self.graph.get(claim, "default_strategy")
