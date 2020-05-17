import operator
fin = open('rosalind_cons.txt')
#fout = open('rosalind_revc.out', 'w')

f = []
temp = []
graph = []

def string_to_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr


test_s = ""
for line in fin:
    if line[0] == '>':
        if test_s != "":
            graph.append(string_to_array(test_s))
            test_s = ""

        a = line[1::1].rstrip('\n')

    else:
        test_s += line.rstrip('\n')

d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
res_graph = []
for i in range(len(graph[0])):
    res_graph.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})


for i in range(len(graph[0])):
    for j in range(len(graph)):
        res_graph[i][graph[j][i]] += 1

consensus = ""
for i in range(len(res_graph)):
    consensus += sorted(res_graph[i].items(), key=operator.itemgetter(1))[-1][0]

print(consensus)

finn = []
for i in 'ACGT':
    for j in range(len(res_graph)):
        finn.append(res_graph[j][i])
    print(i + ':', *finn)
    finn = []




#print(*reversed(sorted(f)))

fin.close()
#fout.close()