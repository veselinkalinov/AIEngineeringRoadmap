# Stage 07 — AI Engineering

> This is where everything converges.
> You've built the foundation — CS, Python, data, ML, infrastructure.
> Now you build the systems that use large language models as components.
> Not fine-tuning. Not research. Engineering.

---

## Resources

### LLM Foundations

**[AI Engineer Roadmap — roadmap.sh](https://roadmap.sh/ai-engineer)**
Read through the entire roadmap before starting this stage. Click every node. Then return to it at the end and audit every node against what you've built. This is your primary orientation map for the stage.

**[LangChain for LLM Application Development — DeepLearning.AI](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)**
Free short course by Andrew Ng's team in collaboration with LangChain. Covers chains, memory, agents, and tools — the core building blocks of LLM-powered applications. Hands-on from the first lesson. Complete this before building your own LLM integrations.

### Generative AI & Transformers

**[Neural Networks: Zero to Hero — Andrej Karpathy (YouTube)](https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)**
The most important resource in this stage. Karpathy builds backpropagation by hand, then builds a bigram model, then builds GPT-2 from scratch. Every video is mandatory. Slow down on "Let's build GPT" — watch it multiple times if needed. After this, transformer architectures will not be a black box.

**[Neural Networks — 3Blue1Brown (YouTube)](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)**
If you haven't already watched this in Stage 05, watch it now as a visual primer before Karpathy's series. Explains what's happening geometrically inside the network.

### RAG (Retrieval-Augmented Generation)

**[RAG From Scratch — LangChain (YouTube)](https://www.youtube.com/watch?v=wd7TZ4w1mSw&list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)**
Full series covering retrieval, chunking, embeddings, vector stores, and reranking — from first principles. Built by the LangChain team. Covers: naive RAG, advanced RAG (reranking, multi-query), and agentic RAG. Watch in order, implement every concept.

### AI Agents

**[AI Agents Roadmap — roadmap.sh](https://roadmap.sh/ai-agents)**
Read through every node. Understand: ReAct pattern, tool use, agent loops, memory types (in-context, external, episodic), and multi-agent architectures. This is the pattern behind production AI systems.

### Cloud Deployment

**[Microsoft Azure Fundamentals AZ-900 — Adam Marczak (YouTube)](https://www.youtube.com/watch?v=Pt9LelJ0fL0&list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM)**
Complete AZ-900 preparation series. Covers core Azure services — compute, storage, networking, security — in a beginner-friendly format. Gets you to certification-ready and cloud-comfortable at the same time. Focus on: Azure Container Instances, Azure Container Registry, and Azure Cognitive Services for direct applicability.

---

## Core Concepts Checklist

- [ ] Transformer architecture: attention mechanism, positional encoding, encoder/decoder
- [ ] Tokenization and embeddings
- [ ] Prompt engineering: zero-shot, few-shot, chain-of-thought
- [ ] RAG pipeline: chunking → embedding → retrieval → reranking → generation
- [ ] Vector databases: FAISS, ChromaDB (concepts and basic usage)
- [ ] ReAct agent pattern: Thought → Action → Observation loop
- [ ] Tool use and function calling
- [ ] Containerized deployment to Azure Container Instances

---

## Project Milestone — AI Engineering Capstone

Build a complete AI application:

```
capstone/
├── main.py              — FastAPI app
├── rag_pipeline.py      — RAG implementation
├── agents/
│   ├── orchestrator.py  — agent loop
│   └── tools.py         — custom tools
├── database.py          — MongoDB
├── Dockerfile
└── docker-compose.yml
```

Deploy to Azure Container Instances using Azure Container Registry.

*Next → [Stage 08: Security & Specialization](../stage-08-security-specialization/)*

---
