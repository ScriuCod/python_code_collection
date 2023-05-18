from unittest import TestCase

good_wins = "Battle Result: Good triumphs over Evil"
evil_wins = "Battle Result: Evil eradicates all trace of Good"
tie = "Battle Result: No victor on this battle field"


def good_vs_evil(good, evil):
    good_values = [int(i) for i in good.split(" ")]
    evil_values = [int(i) for i in evil.split(" ")]

    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]

    good_force = [gv * good_worth[i] for i, gv in enumerate(good_values)]
    evil_force = [gv * evil_worth[i] for i, gv in enumerate(evil_values)]

    print(f'for {good_values=} result in {good_force=}')
    print(f'for {evil_values=} result in {evil_force=}')

    battle = sum(good_force) - sum(evil_force)

    if battle < 0:
        return evil_wins
    if battle > 0:
        return good_wins
    else:
        return tie


good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0')
good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0')
