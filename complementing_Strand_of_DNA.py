fin = open('rosalind_revc.txt')
fout = open('rosalind_revc.out', 'w')

s = fin.readline()

c = 0

for i in range(len(s)):
    if i == 'A':
        s += 'T'

    elif i == 'C':
        s += 'G'

    elif i == 'G':
        s += 'C'

    else:
        s += 'A'

print(s[::-1], file=fout)

fin.close()
fout.close()