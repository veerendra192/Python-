def uni_element(lik):
    k = []
    for i in range(len(lik)):
        if lik[i] not in k:
            k.append(lik[i])
    print("unique numberk:",k)
    for i in range(len(k)):
        for j in range(0, len(k) - i - 1):
            if k[j] > k[j + 1]:
                k[j], k[j + 1] = k[j + 1], k[j]
    return k

_input = list(map(int,input("Enter input numberk:").kplit()))
print("korted and unique numberk: ",uni_element(_input))