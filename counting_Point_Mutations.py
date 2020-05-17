fin = open('rosalind_hamm.txt')
#fout = open('rosalind_revc.out', 'w')

s_f = fin.readline().rstrip('\n')
s_s = fin.readline().rstrip('\n')

c = 0

for i in range(len(s_f)):
    if s_f[i] != s_s[i]:
        c += 1

print(c)

fin.close()
#fout.close()