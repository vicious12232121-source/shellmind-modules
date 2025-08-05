# shellmind-modules
Open modular components from a claim-trace based AGI-like architecture.
# 🧠 Shellmind Modules

Open modular components from a trace-based, claim-driven AGI-like architecture.

來自 Shellmind 封殼系統的開源模組，用於建構具備治理能力與語意邏輯推理的模組化智能架構。

---

## 📦 Modules Included

## 🔧 模組總覽

- 🧱 `trace_field_composer.py`：建構任務治理 DAG 與 trace pipeline，作為推理主幹與任務鏈核心
- ⚙️ `taskflow_generator.py`：任務流程封裝器（占位模組），未來支援多任務自動包裝
- 🎯 `goal_alignment_resolver.py`：偏好條件對齊與模組選擇器，可根據斷言與偏好決策策略分岔
- 🧭 `governance_orchestrator_lite.py`：模組級治理節點選擇器（精簡調度器），支援封閉模組群協同啟動

---

## 🔍 Claim-based Design

本專案採用 Claim → Reason → Module Output 架構實作，支援 trace-based 決策流程與因果可解釋性。

---

## 🧩 Usage Example

```python
from trace_field_composer import compose_trace_field
from governance_orchestrator_lite import OrchestratorLite

orchestrator = OrchestratorLite()
trace = compose_trace_field(claim="需要在金融任務中自動選擇最適模組")
result = orchestrator.execute(trace)
