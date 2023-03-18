import math
n = 2022
x = round(math.pi, 5)
word = 'Python'
polish = 'książka'
outfile = open('vars.txt', 'w',encoding='utf-8')
outfile.write('{}\n{}\n{}\n{}\n'.format(n, x, word, polish))
outfile.close()
infile = open('vars.txt', 'r', encoding='utf-8')
S = infile.read()
print(S)
infile.close()
