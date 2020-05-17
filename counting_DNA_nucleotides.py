fin = open('rosalind_dna.txt')
fout = open('rosalind_dna.out', 'w')

s = fin.readline()

a, c, g, t = 0, 0, 0, 0

for i in s:
    if i == 'A':
        a += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1
    else:
        t += 1

print(a, c, g, t, file=fout)

print(a+c+g+t)
print(len(s))
print(s, file=fout)

fin.close()
fout.close()