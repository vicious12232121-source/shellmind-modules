# taskflow_generator.py
# 封裝任務為 DSL 可執行格式

class TaskflowGenerator:
    def __init__(self, template="default"):
        self.template = template

    def generate(self, task_name, parameters):
        return {
            "task": task_name,
            "params": parameters,
            "template": self.template
        }
