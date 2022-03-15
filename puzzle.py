from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A cannot be both a knight and a knave
    Not(And(AKnave, AKnight)),
    # A can be a knight of a knave
    Or(AKnave, AKnight),
    # A says I am both a knight and a knave
    # if this is true, A is a knight
    Implication(AKnight, And(AKnight, AKnave)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A cannot be both a knight and a knave
    Not(And(AKnave, AKnight)),
    # A can be a knight of a knave
    Or(AKnave, AKnight),
    # B cannot be both a knight and a knave
    Not(And(BKnave, BKnight)),
    # B can be a knight of a knave
    Or(BKnave, BKnight),
    # A says we are both knaves
    Biconditional(AKnight, And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A cannot be both a knight and a knave
    Not(And(AKnave, AKnight)),
    # A can be a knight of a knave
    Or(AKnave, AKnight),
    # B cannot be both a knight and a knave
    Not(And(BKnave, BKnight)),
    # B can be a knight of a knave
    Or(BKnave, BKnight),
    # A says we are both the same kind
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # B says we are different kinds
    Biconditional(BKnight, Or(And(AKnight, Not(BKnight)), And(AKnave, Not(BKnave)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A cannot be both a knight and a knave
    Not(And(AKnave, AKnight)),
    # A can be a knight of a knave
    Or(AKnave, AKnight),
    # B cannot be both a knight and a knave
    Not(And(BKnave, BKnight)),
    # B can be a knight of a knave
    Or(BKnave, BKnight),
    # C cannot be both a knight and a knave
    Not(And(CKnave, CKnight)),
    # C can be a knight of a knave
    Or(CKnave, CKnight),
    # C says A is a knight
    Biconditional(CKnight, AKnight),
    # B says C is a knave
    Biconditional(BKnight, CKnave),
    # A says I am a knight or a knave
    Biconditional(AKnight, Or(AKnight, AKnave)),
    # B says A said I am a knight
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
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
