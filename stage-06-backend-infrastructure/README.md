# Stage 06 — Backend & Infrastructure

> A model that isn't behind an API isn't a product.
> A container that doesn't run in production is a prototype.
> This stage is about infrastructure — the engineering layer that makes ML work in the real world.

---

## Resources

### FastAPI

**[FastAPI for AI Projects — Dave Ebbelaar (YouTube)](https://www.youtube.com/watch?v=-IaCV5-mlSk)**
Practical getting-started guide specifically built for AI use cases. Covers project structure, routing, Pydantic models for request/response validation, and how to wire ML logic into a clean, production-ready API. Build this first — it's your deployment pattern for every model from here on.

**[Backend Roadmap — roadmap.sh](https://roadmap.sh/backend)**
Scan this at the start of the stage. Focus on the sections you'll need for AI: REST APIs, authentication basics, databases, caching concepts, and deployment patterns. This is a map — not a syllabus.

### Docker

**[Docker — Official Getting Started](https://docs.docker.com/get-started/)**
Work through the full official getting-started guide. Understand: images vs containers, Dockerfiles, multi-stage builds, volumes, networking, and Docker Compose. Every AI project you ship from Stage 07 onward will be containerized.

### MongoDB

**[MongoDB Roadmap — roadmap.sh](https://roadmap.sh/mongodb)**
Read through all sections systematically. MongoDB is the database of choice for AI applications — flexible schema, native JSON, easy horizontal scaling.

**[MongoDB — Official Documentation: Getting Started](https://www.mongodb.com/docs/manual/tutorial/getting-started/)**
Documents, collections, CRUD operations, aggregation pipelines, and indexing. Work through the official tutorial in parallel with the roadmap.

### System Design

**[System Design Fundamentals — ByteByteGo (YouTube)](https://www.youtube.com/watch?v=lX4CrbXMsNQ&list=PLCRMIe5FDPsd0gVs500xeOewfySTsmEjf)**
A series covering the core building blocks of scalable systems — caching, databases, message queues, load balancers, API design, and storage systems. Watch the episodes on: database types, message queues, microservices, and caching strategies. These patterns appear directly in production AI systems.

---

## Project Milestone

ML API with persistence:

```
ml_api/
├── main.py          — FastAPI app with /predict and /history endpoints
├── models.py        — Pydantic request/response schemas
├── ml_model.py      — model loading and prediction logic
├── database.py      — MongoDB connection and operations
├── Dockerfile       — containerized deployment
└── docker-compose.yml
```

The API should:
- Accept feature input via POST `/predict`
- Return prediction + confidence score
- Store every prediction to MongoDB
- Return prediction history via GET `/history`
- Run in Docker

*Next → [Stage 07: AI Engineering](../stage-07-ai-engineering/)*

---
