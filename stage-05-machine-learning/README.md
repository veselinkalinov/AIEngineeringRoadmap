# Stage 05 — Machine Learning

> Every AI engineer using models without understanding them
> is one bug away from being completely lost.
> Start with theory. Build from scratch. Then use the libraries.
> In that order.

---

## Resources

### Theory First

**[All Machine Learning Algorithms Explained in 17 Minutes — YouTube](https://www.youtube.com/watch?v=E0Hmnixke2g)**
Watch this before touching any code. It gives you the vocabulary and the landscape — what supervised vs unsupervised means, what classification vs regression means, and where each algorithm fits. Watch it again after finishing the stage.

**[W3Schools — AI & Machine Learning](https://www.w3schools.com/ai/)**
Reference-level coverage of ML concepts. Use for quick definitions and worked examples as you encounter new terms.

**[Machine Learning Roadmap — roadmap.sh](https://roadmap.sh/machine-learning)**
Open this roadmap and click every node systematically — don't skip any. At each node, understand the concept before moving to the next. Return to this at the end of the stage and verify you can explain every node without help.

### Hands-On

**[Educative — Machine Learning with NumPy, Pandas & scikit-learn](https://www.educative.io)**
The primary implementation course for this stage. Covers supervised learning (linear regression, logistic regression, SVM, decision trees, random forests), unsupervised learning (k-means, PCA), and model evaluation. Work through classification chapters first, then unsupervised learning.

**[scikit-learn — Official User Guide](https://scikit-learn.org/stable/user_guide.html)**
The reference you'll return to constantly. Don't try to read it linearly — use it as documentation while implementing in the Educative course. Pay particular attention to: `model_selection`, `preprocessing`, `metrics`, and `pipeline`.

### Neural Networks

**[Neural Networks — 3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)**
The visual foundation. Watch the full playlist before writing any neural network code. Explains what's happening geometrically inside the network — forward pass, backpropagation, gradient descent — without a single line of code.

**[Make Your Own Neural Network — Tariq Rashid](https://www.educative.io)**
Build a neural network from scratch in Python (NumPy only, no frameworks). Train it on MNIST and reach >95% accuracy. This is the implementation companion to the 3Blue1Brown series. Do this before Stage 07 — you'll understand transformers and LLMs dramatically better.

---

## Core Concepts Checklist

- [ ] Supervised vs unsupervised vs reinforcement learning
- [ ] Bias-variance tradeoff
- [ ] Gradient descent (batch, stochastic, mini-batch)
- [ ] Regularization (L1, L2, dropout)
- [ ] Cross-validation and model selection
- [ ] Classification metrics: accuracy, precision, recall, F1, ROC-AUC
- [ ] Regression metrics: MSE, RMSE, MAE, R²
- [ ] Feature engineering and selection
- [ ] Forward pass and backpropagation by hand (NumPy)

---

## What You'll Be Able to Do After This Stage

- Implement ML pipelines end-to-end: data → features → model → evaluation
- Choose the right algorithm for a given problem
- Tune hyperparameters systematically (GridSearchCV, cross-validation)
- Build and train a neural network from scratch in NumPy
- Explain gradient descent, backpropagation, and why regularization works

---

## Project Milestone

Fraud detection classifier:
- Load an imbalanced dataset (credit card fraud or similar)
- Apply SMOTE or class weighting to handle imbalance
- Train and compare at least 3 algorithms (logistic regression, random forest, gradient boosting)
- Evaluate using precision-recall curve and ROC-AUC
- Document your findings in a structured report

*Next → [Stage 06: Backend & Infrastructure](../stage-06-backend-infrastructure/)*

---
