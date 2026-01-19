---
name: agents-crewai
description: Multi-agent orchestration framework for autonomous AI collaboration. Use when building teams of specialized agents working together on complex tasks, when you need role-based agent collaboration with memory, or for production workflows requiring sequential/hierarchical execution. Built without LangChain dependencies for lean, fast execution.
---

# CrewAI

Design and run role-based agent teams using CrewAI.

## Quick Start
1) Define agents with clear roles and goals.
2) Define tasks with explicit expected outputs.
3) Choose a process (sequential vs. hierarchical).
4) Run the crew and inspect outputs.

## Minimal Example
```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(role="Researcher", goal="Find 5 key trends")
writer = Agent(role="Writer", goal="Summarize findings")

research = Task(description="Research AI agents", expected_output="5 bullets", agent=researcher)
write = Task(description="Write a summary", expected_output="Short memo", agent=writer, context=[research])

crew = Crew(agents=[researcher, writer], tasks=[research, write], process=Process.sequential)
result = crew.kickoff(inputs={"topic": "AI agents"})
print(result.raw)
```

## Design Guidance
- Keep roles narrow and outputs explicit.
- Use context chaining to pass outputs between tasks.
- Prefer sequential for reliability; hierarchical for delegation-heavy workflows.

## Use Alternatives When
- You need complex graph cycles → consider LangGraph.
- You’re focused on document retrieval → consider LlamaIndex.

## References
- Extended examples: `references/examples.md`

