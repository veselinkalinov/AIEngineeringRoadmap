# Week 1 - Knowledge

Status: Complete
Date started: 2026-07-22
Official module: https://cs50.harvard.edu/ai/weeks/1/

# Notes

## Knowledge
    - Humans reason based on existing knowledge and draw conclusions. The concept of representing knowledge and drawing conclusions from it is also used in AI, and in this lecture we will explore how we can achieve this behavior.

1. **Knowledge-Based Agents**
    - These are agents that reason by operating on internal representations of knowledge.

2. **Sentence**
    - A sentence is an assertion about the world in a knowledge representation language. A sentence is how AI stores knowledge and uses it to infer new information.

## Propositional Logic
    - Propositional logic is based on propositions, statements about the world that can be either true or false, as in sentences 1-5 above.

1. **Propositional Symbols**
    - Propositional symbols are most often letters (P, Q, R) that are used to represent a proposition.

2. **Logical Connectives**
    - Logical connectives are logical symbols that connect propositional symbols in order to reason in a more complex way about the world.
        * Not (¬) inverses the truth value of the proposition. So, for example, if P: “It is raining,” then ¬P: “It is not raining”.
        * And (∧) connects two different propositions. When these two proposition, P and Q, are connected by ∧, the resulting proposition P ∧ Q is true only in the case that both P and Q are true.
        * Or (∨) is true as as long as either of its arguments is true. This means that for P ∨ Q to be true, at least one of P or Q has to be true.
        * Implication (→) represents a structure of “if P then Q.” For example, if P: “It is raining” and Q: “I’m indoors”, then P → Q means “If it is raining, then I’m indoors.” In the case of P implies Q (P → Q), P is called the antecedent and Q is called the consequent.
        * Biconditional (↔) is an implication that goes both directions. You can read it as “if and only if.” P ↔ Q is the same as P → Q and Q → P taken together. For example, if P: “It is raining.” and Q: “I’m indoors,” then P ↔ Q means that “If it is raining, then I’m indoors,” and “if I’m indoors, then it is raining.” This means that we can infer more than we could with a simple implication. If P is false, then Q is also false; if it is not raining, we know that I’m also not indoors.

3. **Model**
    - assignmen of a thruth value to every propositional symbol

4. **Knowledge Base**
    - a set of sentences known by a knowledged-based agent
5. **Entailnment**
    - If α ⊨ β (α entails β), then in any world where α is true, β is true, too.
        * For example, if α: “It is a Tuesday in January” and β: “It is January,” then we know that α ⊨ β. If it is true that it is a Tuesday in January, we also know that it is January. Entailment is different from implication. Implication is a logical connective between two propositions. Entailment, on the other hand, is a relation that means that if all the information in α is true, then all the information in β is true.

## Inference
 - Inference is the process of deriving new sentences from old ones.
    * For instance, in the Harry Potter example earlier, sentences 4 and 5 were inferred from sentences 1, 2, and 3.
    * There are multiple ways to infer new knowledge based on existing knowledge. First, we will consider the Model Checking algorithm.
        ** To determine if KB ⊨ α (in other words, answering the question: “can we conclude that α is true based on our knowledge base”)Enumerate all possible models. If in every model where KB is true, α is true as well, then KB entails α (KB ⊨ α).

1. **Model Checkiing algorithm**
    -   To run the Model Checking algorithm, the following information is needed:
        * Knowledge Base, which will be used to draw inferences
        * A query, or the proposition that we are interested in whether it is entailed by the KB
        * Symbols, a list of all the symbols (or atomic propositions) used (in our case, these are rain, hagrid, and dumbledore)
        * Model, an assignment of truth and false values to symbols

## Knoledge Engineering
    - Knowledge engineering is the process of figuring out how to represent propositions and logic in AI.

## Inference Rules
    - Model Checking is not an efficient algorithm because it has to consider every possible model before giving the answer (a reminder: a query R is true if under all the models (truth assignments) where the KB is true, R is true as well). Inference rules allow us to generate new information based on existing knowledge without considering every possible model.

    - Inference rules are usually represented using a horizontal bar that separates the top part, the premise, from the bottom part, the conclusion. The premise is whatever knowledge we have, and the conclusion is what knowledge can be generated based on the premise.

## First Order Logic
    - First order logic is another type of logic that allows us to express more complex ideas more succinctly than propositional logic. First order logic uses two types of symbols: Constant Symbols and Predicate Symbols. Constant symbols represent objects, while predicate symbols are like relations or functions that take an argument and return a true or false value.
