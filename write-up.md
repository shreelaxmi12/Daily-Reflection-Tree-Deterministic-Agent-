#  Daily Reflection Tree — Design Write-up

## Objective

The goal of this assignment was to design a deterministic reflection system that helps users analyze their day in a structured way. The system avoids randomness and ensures that the same inputs always produce the same output, making it reliable and consistent.

---

## Approach to Tree Design

I designed the reflection flow as a step-by-step conversation rather than a questionnaire. The goal was to make the user pause and think instead of just selecting options quickly.

The tree is structured across three psychological axes:

1. Locus of Control (Axis 1)
2. Contribution vs Entitlement (Axis 2)
3. Radius of Concern (Axis 3)

Each axis builds on the previous one to create a natural progression of reflection.

---

## Axis 1 — Locus (Victim vs Victor)

The first step focuses on understanding how the user perceives control over their day.

The questions were designed to identify whether the user:

* takes ownership of outcomes, or
* attributes results to external factors

For example:

* Options like *“I adapted quickly”* indicate internal locus
* Options like *“I waited for others to act”* indicate external locus

Based on the response, the tree branches into different reflection messages. The goal is not to judge but to gently highlight awareness of personal agency.

---

## Axis 2 — Contribution vs Entitlement

The second axis shifts focus from control to contribution.

The question here explores whether the user:

* focused on helping or contributing, or
* expected recognition or support from others

Branching is used again to differentiate between contribution-oriented and entitlement-oriented responses.

The reflection encourages users to shift toward contribution without making them feel criticized.

---

## Axis 3 — Radius (Self vs Others)

The final axis expands the perspective of the user.

It checks whether the user is:

* focused only on themselves, or
* considering team, colleagues, or end users

This stage is designed to encourage a broader perspective and help the user connect their work to a larger purpose.

---

## Branching Logic

The tree uses deterministic branching based on selected options.

* Each question has fixed options
* Each option leads to a predefined path
* Decision nodes route the flow without user interaction

This ensures:

* no ambiguity
* no randomness
* consistent outcomes

---

## Reflection Design

The reflection messages were written to:

* avoid judgment or criticism
* sound like a thoughtful colleague
* encourage awareness rather than instruction

For example:
Instead of saying *“you should do better”*, the system uses language like:
*“small choices matter — noticing them can help improve control.”*

---

## Guardrails

To prevent misuse or hallucination:

* No free-text input is allowed
* All responses are predefined
* No AI or LLM is used at runtime
* The system does not make assumptions about emotions
* The tone remains neutral and supportive

---

## What I Would Improve

Given more time, I would:

* Add more depth to each axis with additional branching
* Use signal tracking to generate a more personalized summary
* Improve the summary by referencing specific user choices
* Build a simple UI instead of CLI for better usability

---

## Conclusion

This assignment helped me understand how to convert abstract psychological concepts into structured decision trees.

The focus was on clarity, determinism, and user experience rather than complexity. The final system provides a consistent and meaningful reflection flow that aligns with the assignment requirements.
