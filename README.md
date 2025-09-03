# physics

- expérience avec pybullet

- création programmatique intelligente de model

s = batis(h=40, l=40, p=5)
b1 = bras(o=s.c1, l=50)
b2 = bras(o=s.c2, l=50)
b3 = bras(o=s.c3, l=50)

z = rotule(b1.b, b2.b)
z = rotule(b2.b, b3.b)
z = rotule(b1.b, b2.a)


j = axe(b1.a, b2.b)

r = roue(d=60)

