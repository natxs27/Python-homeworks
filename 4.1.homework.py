r = 50
x = [33, 2, 24, 1, -5, 58, 79, -82, 94, 10]
y = [24, -3, -90, 37, 4, 6, 62, 95, -40, -18]
p = []
for i in range(0,9):
    p.append([x[i], y[i]])
okrag = lambda x,y,r:'Punkt P należy do okręgu.' if x**2+y**2<=r**2 else 'Punkt P nie należy do okręgu.'
poz = lambda x,y: 'Współrzędne są pozytywne.' if x > 0 and y > 0 else 'Jedna lub więcej współrzędnych jest negatywnych.'

for i in range(0,9):
    print('Punkt', p[i][0],',', p[i][1],'-', okrag(p[i][0], p[i][1], r), end=' ')
    print(poz(p[i][0], p[i][1]))

p.sort(key = lambda x: x[0])
print(f"Współrzędne sortowane po Y od wartości najniższej{p}")

p.sort(key = lambda y: y[1], reverse=True)
print(f"Współrzędne sortowane po Y od wartości najwyższej{p}")

p.sort(key = lambda x: abs(x[1])+abs(x[0]))
print(f"Współrzędne sortowane po sumie wartości bezwzględnych:{p}")
