name = input("Input: ")

print("Output: ", end="")

for letter in name:
   if not letter.lower() in ["a", "e", "i", "o", "u"]:
       print(letter, end="")

print()