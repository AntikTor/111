a = 'Python is the best programming language in the world';
a1 = a[5:-7]
print(a1)
b = 'Guido van Rossum is the benevolent dictator for life'
b1 = b[::3]
print(b1)
c = 'You have a problem with authority, Mr. Anderson.'
c1 = list(map(c.count,c))
print(c1)
c2 = list(zip(list(c),c1))
print(c2)
c3=dict(c2)
print(c3)
