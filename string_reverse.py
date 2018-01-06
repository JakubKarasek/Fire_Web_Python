def reverse(text):
  word = []
  for letter in text:
      word.append(letter)
  word.reverse()
  a = ""
  b = a.join(word)
  return b

print(reverse("Kuba"))