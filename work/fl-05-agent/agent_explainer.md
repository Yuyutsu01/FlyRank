# From Workflow to Agent: Understanding Agents and MCP

The rise of large language models has triggered widespread terminology inflation. Today, nearly any automated script or prompt sequence is casually labeled an "agent." In machine learning engineering, precision matters: conflating a fixed AI workflow with an autonomous AI agent obscures critical architectural trade-offs between predictability and autonomy.

### 1. What an Agent Is
An AI agent is an autonomous system where a foundation model is provided with a high-level goal, environmental tools, and the authority to govern its own control flow. Operating within an iterative loop?perceiving the environment, deciding which tool to call, observing the execution result, and reflecting on its progress?an agent determines its own path to goal completion. Crucially, the model itself decides when more information is needed and when the task is finished.

### 2. What an Agent Is NOT
An agent is not simply an LLM with access to an API, nor is it a multi-prompt chain. Merely calling Claude or GPT-4 three times in a row inside a script does not constitute an agent. If the control flow, execution order, and conditional branching are predetermined by human code, the system lacks dynamic decision-making. Calling something an agent simply because AI is involved is a fundamental misclassification.

### 3. Workflow vs. Agent
The distinction lies in who controls the execution loop. In an AI workflow, the developer designs a fixed, hard-coded path. Step A reliably feeds Step B, which feeds Step C. Workflows prioritize determinism, low latency, and auditable consistency. In contrast, an agent controls its own execution path. Given the goal "find the baseline precision for our model," an agent might inspect a file, find it missing, query a database, encounter an error, fix its query, and summarize the result. This flexibility grants autonomy, but sacrifices strict determinism.

### 4. How My FL-04 Workflow Currently Works
My previous FL-04 research analysis pipeline (Gather ? Synthesize ? Draft ? Review ? Format) is a textbook workflow. It uses Google NotebookLM for source-grounded evidence extraction and Claude Project for drafting and review. However, the sequence is entirely static. A human manually uploads the PDF, copies extraction outputs between tools, triggers the review prompt, and pastes the final markdown into the repository. The models process text at isolated stations, but neither tool can autonomously alter the pipeline's direction.

### 5. What Would Need to Change to Become an Agent
To transform this workflow into an agent, two foundational capabilities are required: dynamic control flow and tool access. Instead of relying on a human to ferry text across web interfaces, the language model must be situated within an autonomous runtime. It must be empowered to evaluate whether the evidence gathered from a research paper is sufficient to support a claim. If an ablation study is missing, the agent?not the human?must autonomously formulate a query, call an external retrieval tool, evaluate the returned data, and decide whether to proceed or gather further proof.

### 6. What MCP Is
The Model Context Protocol (MCP) is an open standard introduced by Anthropic that provides a universal, standardized interface between AI models and external data systems. Previously, connecting an LLM to local files, GitHub, or SQL databases required proprietary API wrappers for every provider. MCP standardizes this architecture through a client-host-server model, decoupling the AI application from external tool implementations.

### 7. MCP Tools, Resources, and Prompts
MCP defines three fundamental architectural primitives:
- **Tools**: Executable functions that the model can invoke to perform actions in the real world (e.g., `read_file`, `execute_query`).
- **Resources**: Standardized data streams and static context that the client can read into the model's window without executing arbitrary code (e.g., file contents, server logs).
- **Prompts**: Parameterized, pre-configured prompt templates hosted by the server that guide the model through standardized workflows.

### 8. Why MCP Matters for Agents
Without standard protocols like MCP, agents remain sandboxed conversationalists capable only of discussing code rather than inspecting it. MCP acts as the sensory and motor system for agents. It provides a standardized protocol through which an agent can discover available tools at runtime, inspect their JSON schemas, execute calls safely, and consume structured responses.

### 9. What My MCP Connector Demonstrated
By connecting the official Filesystem MCP server (`@modelcontextprotocol/server-filesystem`) to Claude Desktop, we granted the model direct access to the local `FlyRank` repository. Rather than relying on human copy-pasting, Claude invoked real tools (`list_directory`, `read_file`, `search_files`) to audit our actual codebase, inspect baseline action scores, and verify data contract constraints. This demonstrated genuine tool-use: reading grounded local data that closed chat interfaces cannot access.

### 10. Limitations and Human Oversight
Granting agents tool access introduces real failure modes. Agents can misinterpret tool outputs, enter expensive retry loops, or hallucinate parameters. Therefore, human oversight is non-negotiable. Critical boundaries?such as executing write operations, committing code, or determining research validity?must remain gated by human approval. AI accelerates analysis; humans verify truth.

### 11. Concrete Agent Upgrade for FL-04
An immediate agentic upgrade to our FL-04 pipeline is an **Autonomous Iterative Evidence Agent**. Given an open research question, the agent uses MCP search tools to query ArXiv, inspects empirical tables, runs an automated claim-audit, and autonomously loops back to gather secondary verification sources if a statistical claim is ambiguous. It stops and alerts the researcher only when evidence is conclusive, replacing a rigid human-ferried sequence with goal-driven autonomous inquiry.
