from logic import And, Biconditional, Not, Or, Symbol, model_check

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Additional symbol needed for Puzzle 3.
# If false, A said "I am a Knight."
ASaidKnave = Symbol("A said 'I am a Knave'")


# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # A is a knight exactly when A's statement is true.
    Biconditional(AKnight, And(AKnight, AKnave)),
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave, but not both.
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A's statement: A and B are both knaves.
    Biconditional(AKnight, And(AKnave, BKnave)),
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

same_kind = Or(And(AKnight, BKnight), And(AKnave, BKnave))

different_kinds = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave, but not both.
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A says that A and B are the same kind.
    Biconditional(AKnight, same_kind),
    # B says that A and B are different kinds.
    Biconditional(BKnight, different_kinds),
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.",
# but you don't know which.
#
# B says "A said 'I am a knave.'"
# B then says "C is a knave."
# C says "A is a knight."

a_statement = Or(
    # A said "I am a knight."
    And(Not(ASaidKnave), AKnight),
    # A said "I am a knave."
    And(ASaidKnave, AKnave),
)

knowledge3 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave, but not both.
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # C is either a knight or a knave, but not both.
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # A's statement must match A's identity.
    Biconditional(AKnight, a_statement),
    # B says that A said "I am a knave."
    Biconditional(BKnight, ASaidKnave),
    # B says that C is a knave.
    Biconditional(BKnight, CKnave),
    # C says that A is a knight.
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]

    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]

    for puzzle, knowledge in puzzles:
        print(puzzle)

        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
