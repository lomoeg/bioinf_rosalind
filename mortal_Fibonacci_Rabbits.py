n, k = map(int, input().split())

f_young = [0] * k
f_old = [0] * (k + 1)
f_young.append(1)

print(1, ': ', f_old[-1], f_young[-1])

for i in range(k + 1, n + k):
    f_old.append(f_young[i - 1] - f_young[i - k] + f_old[i - 1])
    f_young.append(f_old[i - 1])
    print(i - k + 1, ': ', f_old[-1], f_young[-1], '      ', f_old, f_young)

print(f_young[n + k - 1] + f_old[n + k - 1])

#   http://rosalind.info/problems/fibd/