fin = open('rosalind_gc.txt')
#fout = open('rosalind_revc.out', 'w')

f = []
temp = []


def percentageCG(s):
    cg = 0
    for i in s:
        if i in 'CG':
            cg += 1
    return (cg / len(s)) * 100


test_s = ""

for line in fin:
    if line[0] == '>':
        if test_s != "":
            temp.append(percentageCG(test_s))
            temp.append(a)
            f.append(temp)
            temp = []
            test_s = ""

        a = line[1::1].rstrip('\n')

    else:
        test_s += line.rstrip('\n')




print(*reversed(sorted(f)))

fin.close()
#fout.close()