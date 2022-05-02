def strcmp(s, i1, i2):
    eqlen = 0
    n = len(s)
    while i1 < n and i2 < n and s[i1] == s[i2]:
        i1 += 1
        i2 += 1
        eqlen += 1
    return eqlen


def prefix_z_values(s):
    n = len(s)
    l = r = 0
    zp = [0] * n

    for i in range(1, n):
        if i >= r:
            zp[i] = strcmp(s, 0, i)
            l = i
            r = l + zp[i]
            print('1: ', end='')
        else:
            j = i - l
            if zp[j] < r - i:
                zp[i] = zp[j]
                print('2: ', end='')
            else:
                zp[i] = r - i + strcmp(s, r - i, r)
                l = i
                r = l + zp[i]
                print('3: ', end='')
        print(f'i:{i} z[{i}]={zp[i]} l={l} r={r}  {s[i:i+zp[i]]}')

    return zp
