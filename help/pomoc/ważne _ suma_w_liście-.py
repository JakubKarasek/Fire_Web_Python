n = [0, 3, 67]

def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result
print (total(n))

n = ["Michael", "Lieberman"]

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print (join_strings(n))


#=
"""
n = [3, 5, 7]

def total(numbers):
  return sum(numbers)
print (total(n))
"""

# nie działa to: (nie dla wszystkich)
"""n = [0, 3, 67]

def total(numbers):
  result = 0
  for i in numbers:
    result += numbers[i]
  return result
print (total(n))
"""