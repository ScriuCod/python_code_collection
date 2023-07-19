def tournamentWinner(competitions, results):
    t = dict()
    for c, r in zip(competitions, results):
        t[c[1-r]] = t.get(c[1-r], 0) + 1

    return max(t, key=t.get)
