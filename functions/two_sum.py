def two_sum(n, t):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[j] == t - n[i]:
                return [i, j]
