# Daily Reflection Tree (Deterministic Agent)

##  Overview

This project implements a deterministic end-of-day reflection system that guides users through a structured conversation. The system uses a decision tree (no LLM at runtime) to help users reflect on their actions, contribution, and perspective.

---

##  Objective

To design a predictable, auditable reflection tool where:

* every question has fixed options
* every option leads to a defined next step
* the same inputs always produce the same outputs

---

##  Reflection Structure

The tree is organized into three psychological axes:

### 1. Locus of Control (Axis 1)

Identifies whether the user attributes outcomes to their own actions or external factors.

### 2. Contribution vs Entitlement (Axis 2)

Examines whether the user focused on contributing value or expecting value.

### 3. Radius of Concern (Axis 3)

Expands reflection from self-focused thinking to considering others (team, colleagues, users).

Each axis builds on the previous one to create a natural flow of reflection.

---

##  How It Works

* The system loads a structured tree from `reflection-tree.json`
* Each node represents a step (question, decision, reflection, etc.)
* User selects from predefined options
* The system follows deterministic branching logic
* Reflections and summary are shown based on the selected path

---

##  How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the agent:

```bash id="runcmd"
python agent.py
```

---

##  Project Structure

```text id="projstruct"
reflection-tree/
│
├── tree/
│   ├── reflection-tree.json
│   └── tree-diagram.md
│
├── agent/
│   └── agent.py
│
├── write-up.md
└── README.md
```

---

##  Design Constraints

* No LLM or AI used at runtime
* Fully deterministic flow
* No free-text input (fixed options only)
* No randomness in decision making

---

##  Approach

The focus was on:

* clarity over complexity
* structured thinking
* natural conversational flow

The questions and reflections were designed to feel like a thoughtful discussion rather than a rigid survey.

---

##  Future Improvements

* Add deeper branching within each axis
* Track signals to generate personalized summaries
* Improve UI (web-based interface)
* Expand reflection depth using additional scenarios

---

## Conclusion

This project demonstrates how psychological concepts can be translated into structured decision systems. The final solution provides a consistent and meaningful reflection experience while adhering to deterministic design principles.
