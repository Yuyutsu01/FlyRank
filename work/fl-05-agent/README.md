# FL-05 ? From Workflow to Agent: Understanding Agents and MCP

**Track:** General AI Fluency  
**Assignment:** FL-05: From Workflow to Agent  
**Status:** **Completed, Verified with Real Screenshots & Committed**  

---

## 1. Assignment Overview & Objective

This assignment investigates the architectural distinction between a **fixed AI workflow** and an **autonomous AI agent**, explores Anthropic's **Model Context Protocol (MCP)**, connects a working MCP server to Claude Desktop, executes three real tool tasks on local files, embeds authentic screenshot evidence, and specifies a concrete agent upgrade for our research pipeline.

---

## 2. Key Findings & Conclusions

### Workflow vs. Agent Classification
- **Classification of FL-03 / FL-04**: **WORKFLOW (Not an Agent)**.
- *Rationale*: Our 5-step research pipeline follows a rigid, developer-defined linear sequence (Gather ? Synthesize ? Draft ? Review ? Format). Human operators manually ferry data across web interfaces. Neither model can dynamically alter the pipeline flow, call external retrieval tools on-the-fly, or self-direct iteration loops based on runtime evidence. Calling advanced LLMs at multiple stages does not make a system an agent.

### MCP Architecture & Primitives
- **Model Context Protocol (MCP)** standardizes how foundation models interact with external data sources and tools.
- **Three Core Primitives**:
  1. *Tools*: Executable functions the model can call to perform actions (e.g., `read_file`, `list_directory`).
  2. *Resources*: Structured, read-only data context exposed to the model window.
  3. *Prompts*: Standardized, server-hosted prompt templates for common operations.

---

## 3. Connected MCP Connector & Three Real Tasks

- **MCP Connector**: Official **Filesystem MCP Server** (`@modelcontextprotocol/server-filesystem`).
- **Configuration**: Configured in Claude Desktop (`C:\Users\shiva\AppData\Roaming\Claude\claude_desktop_config.json`) scoped to `C:\Users\shiva\OneDrive\Desktop\FlyRank`.
- **Three Real Tasks Executed & Verified with Screenshots**:
  1. *Task 1 (`list_directory`)*: Audited `work/outputs` directory, confirming `baseline_action_score.csv` (3.5MB) and `baseline_run_receipt.json`.
  2. *Task 2 (`read_file`)*: Read local private `baseline_run_receipt.json`, extracting exact ML-07 baseline metric (`Precision@50 = 0.240`).
  3. *Task 3 (`read_file`)*: Inspected `work/week-03-identity-kit/style-note.md`, verifying exact visual identity HEX palette (`#0F172A`, `#111827`, `#F8FAFC`, `#2563EB`).
  *(Plain chat alone could NOT perform these tasks because standard models have zero access to the local file system).*

---

## 4. Proposed Agent Upgrade for FL-04 Pipeline

- **Upgrade Name**: **Autonomous Iterative Evidence Agent**
- **Autonomous Decisions**: Given a research paper or question, the agent dynamically decides which search/retrieval tools to call, inspects returned ablation tables, evaluates claim strength, and autonomously loops to retrieve follow-up ArXiv papers when evidence is ambiguous?halting only when claims are empirically verified.
- **Human Gate**: Human oversight is preserved at the final publication and code integration gate.

---

## 5. Deliverables & File Map

| Artifact | File Path | Purpose | Status |
|---|---|---|---|
| **Workflow vs. Agent Analysis** | [workflow_vs_agent.md](workflow_vs_agent.md) | Technical comparison, autonomy analysis, and FL-04 classification | **Completed** |
| **Master Agent Explainer** | [agent_explainer.md](agent_explainer.md) | Comprehensive 600?900 word explainer covering agents, MCP, and upgrades (Exact count: 894 words) | **Completed** |
| **MCP Execution & Evidence** | [mcp_tasks.md](mcp_tasks.md) | Documentation of 3 real MCP tasks, inputs, outputs, and embedded screenshots | **Completed** |
| **Captured Screenshots** | [screenshots/](screenshots/) | Real screenshots showing tool call badges and grounded responses | **Verified (3/3)** |
| **Master Documentation** | [README.md](README.md) | Overview, findings, and completed submission checklist | **Completed** |

---

## 6. Submission & Quality Checklist

- [x] FL-04 / FL-03 workflow analyzed and classified (WORKFLOW)
- [x] Technical comparison between workflows and agents in `workflow_vs_agent.md`
- [x] 894-word master explainer in `agent_explainer.md` (meets 600?900 word rule)
- [x] MCP server `@modelcontextprotocol/server-filesystem` configured in Claude Desktop
- [x] Three real tool tasks executed and documented in `mcp_tasks.md`
- [x] Plain chat distinction proven for all three tasks
- [x] 3 authentic screenshots captured and embedded under `screenshots/`
- [x] Autonomous Iterative Evidence Agent upgrade detailed
- [x] Zero fabricated outputs or screenshots
