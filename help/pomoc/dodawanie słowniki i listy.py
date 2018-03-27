list = {"key111" : 1 , "key112" : [1,2,3,4]}
#dodanie do klucza nowego elementu w liscie
list["key112"].append(5)
print (list)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in a:
  if x%2 == 0:
   print (x)