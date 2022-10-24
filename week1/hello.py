# Ask user for their name
name = input("What is your name? ")

# Remove leading and trailing whitespace
name = name.strip()

# Capitalize the first letter of the name
name = name.title()

# Say hello to the user
print(f"hello, {name}")
#print("Hello,", name)
#print("Hello,", end="")
#print(name)
