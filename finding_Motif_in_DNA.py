fin = open('rosalind_subs.txt')
#fout = open('rosalind_subs.out', 'w')


s = fin.readline().rstrip('\n')
subs = fin.readline().rstrip('\n')
c = []


for i in range(len(s) - len(subs)):
    if s[i: i + len(subs)] == subs:
        c.append(i + 1)

print(*c)

fin.close()
#fout.close()