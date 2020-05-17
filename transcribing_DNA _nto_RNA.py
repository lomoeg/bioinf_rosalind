fin = open('rosalind_rna.txt')
fout = open('rosalind_rna.out', 'w')

s_in = fin.readline()

s = ""

for i in s_in:
    if i == 'T':
        s += 'U'
    else:
        s += i


print(s, file=fout)

fin.close()
fout.close()