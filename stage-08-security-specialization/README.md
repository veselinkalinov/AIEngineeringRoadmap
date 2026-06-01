# Stage 08 — Security & Specialization

> Deploying AI systems without understanding how they fail is not engineering.
> This final stage covers AI red teaming, safety concepts, and portfolio assembly.
> When you finish, you should have something worth showing.

---

## Resources

### AI Red Teaming

**[AI Red Teaming Roadmap — roadmap.sh](https://roadmap.sh/ai-red-teaming)**
Click every node carefully. This roadmap covers: prompt injection, jailbreaking, adversarial inputs, data poisoning, model inversion, and organizational AI risk. Read the introduction — "Why AI Red Teaming" — before anything else.

**[Introduction to AI Red Teaming — OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/)**
The OWASP Top 10 for LLM Applications. Read through all 10 vulnerability classes. Understand how each maps to a real attack vector. For each one, consider: does your Stage 07 capstone expose this vulnerability?

**[AI Red Teaming in Practice](https://roadmap.sh/ai-red-teaming)**
Return to the roadmap for the "In Practice" nodes. Implement at least 3 red teaming exercises against your own Stage 07 application:
- Prompt injection attack and mitigation
- Sensitive data leakage via adversarial prompting
- API key and credential exposure detection

### Safety Patterns

Security patterns to implement in production AI systems:

```python
# Input sanitization
SENSITIVE_PATTERNS = [
    r"ANTHROPIC_API_KEY",
    r"sk-ant-[a-zA-Z0-9]+",
    r"mongodb\+srv://[^\s]+",
]

# Rate limiting, output filtering, system prompt hardening
```

---

## Portfolio Assembly

Before you close this roadmap, build and publish the following. Each project should have a GitHub repository with a production-quality README.

| Project | What It Demonstrates |
|---------|---------------------|
| CS50x Final Project | CS fundamentals, problem decomposition |
| ML Pipeline | Data engineering, model training, evaluation |
| FastAPI ML API | Backend engineering, Docker, MongoDB |
| RAG Application | LLM engineering, vector search, retrieval |
| AI Agent | Agentic patterns, tool use, orchestration |
| Capstone | End-to-end production AI system |

---

## Skills You Should Be Able to Articulate

- How transformer attention works (draw the QKV diagram from memory)
- The difference between RAG and fine-tuning (and when to use each)
- How to containerize and deploy an AI application to a cloud provider
- Three concrete attack vectors against LLM-powered systems
- Your production deployment stack (FastAPI + Docker + MongoDB + Azure)

---

*You made it. Now build something that matters.*

---
