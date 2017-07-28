def comb(n,k):
    if n < k:
        print("Impossible!")
    if n == k:
        return [[i for i in range(1, n + 1)]]
    if k == 1:
        return [[i] for i in range(1, n + 1)]
    result = list()
    sub = comb(n - 1, k)
    sub2 = comb(n - 1, k - 1)
    for j in sub2:
        j.append(n)
        result.append(j)
    result.extend(sub)
    return result

print(comb(6,3))
