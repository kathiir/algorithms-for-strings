def gorner_2_mod(string: str, m, q):
    res = 0
    for i in range(m):
        res = ((res << 1) + ord(string[i])) % q
    return res


def karp_rabin(substr: str, string: str, q):
    m = len(substr)
    n = len(string)
    res = list()
    p2m = 1

    for i in range(m - 1):
        p2m = (p2m * 2) % q

    hash_substr = gorner_2_mod(substr, m, q)
    hash_str = gorner_2_mod(string, m, q)

    for j in range(n - m + 1):
        if hash_str == hash_substr:
            k = 0
            while k < m and substr[k] == string[j + k]:
                k += 1

            if k == m:
                res.append(j)
        if j + m < n:
            hash_str = (((hash_str - p2m * ord(string[j])) << 1) + ord(string[j + m])) % q

        if hash_str < 0:
            hash_str += q

    return res
