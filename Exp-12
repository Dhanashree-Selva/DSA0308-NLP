# Simple Earley Parser for Context-Free Grammar

grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N': [['cat'], ['dog']],
    'V': [['sees'], ['likes']]
}


def earley_parser(words):
    n = len(words)
    chart = [[] for _ in range(n + 1)]

    # State format: (LHS, RHS, dot, start)
    # Example: S -> NP . VP, 0

    chart[0].append(('S', ['NP', 'VP'], 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for state in chart[i].copy():
                lhs, rhs, dot, start = state

                # Completed state
                if dot == len(rhs):
                    for prev in chart[start]:
                        plhs, prhs, pdot, pstart = prev

                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (plhs, prhs, pdot + 1, pstart)

                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

                else:
                    next_symbol = rhs[dot]

                    # Predictor
                    if next_symbol in grammar:
                        for production in grammar[next_symbol]:
                            new_state = (
                                next_symbol,
                                production,
                                0,
                                i
                            )

                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

            # Scanner
            if i < n:
                for state in chart[i]:
                    lhs, rhs, dot, start = state

                    if dot < len(rhs):
                        next_symbol = rhs[dot]

                        if next_symbol not in grammar:
                            if next_symbol == words[i]:
                                new_state = (
                                    lhs,
                                    rhs,
                                    dot + 1,
                                    start
                                )

                                if new_state not in chart[i + 1]:
                                    chart[i + 1].append(new_state)

    # Check acceptance
    final_state = ('S', ['NP', 'VP'], 2, 0)

    return final_state in chart[n]


# Input sentence
sentence = input("Enter a sentence: ").lower().split()

# Parse the sentence
if earley_parser(sentence):
    print("Sentence is accepted by the grammar.")
else:
    print("Sentence is rejected by the grammar.")

"""
the cat sees a dog
"""
