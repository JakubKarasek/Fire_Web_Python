#odpowiednie - dwustopniowe podzielenie listy,użycie .split() i użycie .format()

beatles = 'Harrison George,Lennon John,McCartney Paul,Starr Ringo'
beatles = beatles.split(',')
#print(beatles)

b = []
for i in beatles:
    a = i.split(' ')
    b.append(a)
#print(b)
print('{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}'.format(b[0][1], b[0][0], b[1][1], b[1][0],
    b[2][1], b[2][0], b[3][1], b[3][0]))


