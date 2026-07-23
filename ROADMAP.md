# Roadmap-to-Code Map

The detailed daily schedule lives in the Notion Life OS calendar. This file maps that schedule to development units and avoids duplicating the full calendar.

| Scheduled period | Roadmap item | Development unit | Expected output | Status |
|---|---|---|---|---|
| Completed through 2026-07-20 | CS50P | `stage-02-python-software-design/CS50P/` | Weeks 0-9, problem sets, PromptVault final project, certificate | Completed |
| Independent practice | LeetCode | `stage-03-data-structures-algorithms/leetcode/` | Individually selected solutions with complexity notes | Active, self-directed |
| Completed 2026-07-21 to 2026-07-22 | CS50AI Weeks 0-1 | `stage-05-machine-learning/CS50AI/` | Completed Search and Knowledge work | Completed |
| Daily until AIPO completion | AI Prompt Optimizer | `../aiprompts-optimizer/` | One sequential, tested portfolio project | Active external repository |
| Selected days | WC2026 Predictor technical study | `../wc2026-predictor/wc2026-files/curriculum/` | One curriculum document reviewed per scheduled session | Active external repository |
| 2026-07-23 to 2026-08-05 | NumPy, pandas, Matplotlib, SciPy | `stage-04-data-scientific-python/` | Reproducible notebooks, Spotify API analysis, and a data-stack capstone | Active |
| 2026-08-06 to 2026-08-21 | Standalone practical CS50AI projects | `stage-05-machine-learning/CS50AI/` | PageRank, Heredity, Crossword, Shopping, Nim, Traffic, Parser, and Questions implementations | Planned |
| 2026-08-22 to 2026-09-07 | Portfolio evidence, supporting videos, ML math, and AIPO | Stage-specific folders plus `../aiprompts-optimizer/` | Project evidence, video notes, worked math examples, and tested AIPO progress | Planned |
| 2026-09-08 to 2026-09-16 | Google Machine Learning Crash Course | `stage-05-machine-learning/google-ml-crash-course/` | Module exercises and evaluation notes | Planned |
| 2026-09-17 to 2026-10-31 | Hugging Face LLM Course | `stage-07-ai-engineering/hugging-face-llm-course/` | Chapter notebooks and project artifacts | Planned |
| 2026-11-02 to 2026-12-04 | Practical ML and neural-network foundations | `stage-05-machine-learning/` | Evaluated ML models, NumPy neural network, and Karpathy implementations | Planned |
| 2026-12-05 to 2026-12-31 | RAG and deployment | `stage-06-backend-infrastructure/` and `stage-07-ai-engineering/` | RAG implementations, deployment-course artifacts, and chatbot requirements | Planned |

## Exact Work-Unit Paths

Use the matching path in each Notion calendar day. Create a future work-unit directory only when that task starts.

| Work unit | Exact path |
|---|---|
| NumPy | `C:\Projects\Road to AI Engineer\stage-04-data-scientific-python\numpy\` |
| pandas | `C:\Projects\Road to AI Engineer\stage-04-data-scientific-python\pandas\` |
| Matplotlib | `C:\Projects\Road to AI Engineer\stage-04-data-scientific-python\matplotlib\` |
| SciPy | `C:\Projects\Road to AI Engineer\stage-04-data-scientific-python\scipy\` |
| Spotify API analysis | `C:\Projects\Road to AI Engineer\stage-04-data-scientific-python\projects\spotify-api-analysis\` |
| Data-stack EDA capstone | `C:\Projects\Road to AI Engineer\stage-04-data-scientific-python\projects\pandas-eda\` |
| CS50AI standalone projects | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\CS50AI\<official-week>\<official-project>\` |
| Google ML Crash Course | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\google-ml-crash-course\<module>\` |
| Hugging Face LLM Course | `C:\Projects\Road to AI Engineer\stage-07-ai-engineering\hugging-face-llm-course\chapter-<NN>\` |
| Educative practical ML | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\educative-practical-ml\` |
| Codédex machine learning | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\codedex-machine-learning\` |
| NumPy neural network | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\neural-networks\numpy-network\` |
| Karpathy Zero to Hero | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\neural-networks\karpathy-zero-to-hero\<video-unit>\` |
| 3Blue1Brown linear algebra | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\math-foundations\3blue1brown-linear-algebra\` |
| 3Blue1Brown neural networks | `C:\Projects\Road to AI Engineer\stage-05-machine-learning\math-foundations\3blue1brown-neural-networks\` |
| ArjanCodes notes | `C:\Projects\Road to AI Engineer\stage-02-python-software-design\notes\arjancodes.md` |
| LeetCode | `C:\Projects\Road to AI Engineer\stage-03-data-structures-algorithms\leetcode\<number>-<problem-slug>\` |
| LangChain RAG From Scratch | `C:\Projects\Road to AI Engineer\stage-07-ai-engineering\rag-from-scratch\part-<NN>\` |
| Docker for Developers | `C:\Projects\Road to AI Engineer\stage-06-backend-infrastructure\docker-for-developers\` |
| The Good Parts of AWS | `C:\Projects\Road to AI Engineer\stage-06-backend-infrastructure\aws-good-parts\` |
| Forward Deployed Engineer | `C:\Projects\Road to AI Engineer\stage-07-ai-engineering\forward-deployed-engineer\` |
| RAG Chatbot on Your Own Docs | `C:\Projects\Road to AI Engineer\stage-07-ai-engineering\projects\rag-chatbot-own-docs\` |
| AI Prompt Optimizer | `C:\Projects\aiprompts-optimizer\` |
| WC2026 Predictor curriculum | `C:\Projects\wc2026-predictor\wc2026-files\curriculum\` |

## Repository Boundaries

- Each course, project, and exercise keeps its own required filenames and dependency files.
- External portfolio repositories remain independent Git repositories and are connected through the VS Code multi-root workspace.
- The stage directories describe learning progression; they are not a shared Python package or shared dependency environment.
- New work-unit directories are created when work starts. Future empty project scaffolds are not generated in advance.
