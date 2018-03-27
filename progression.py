"""
Bardzo trudne! Dla zadanego n wyświetl liczby wg przzykładowego schematu:

Dla n=5:
[0,1,2,3,4],
[1,2,3,4,0],
[2,3,4,0,1],
[3,4,0,1,2],
[4,0,1,2,3]
"""
#modulo
def progression(n):
      my_list = list(range(n))

      for i in range(n):
          print(my_list)

          #poświrować coś z pop() i append() - poczyać o tych meotodach w docsach


print(progression(5))

