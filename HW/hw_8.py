def periods(S, D):
    count = 0
    for i in range(len(S)):
        if S[i] == D[i]:
            count += 1
    return count
S = [155, 25, 45]
D = [155, 25, 45]
count = periods(S, D)
print(count)