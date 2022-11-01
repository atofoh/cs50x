expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

if y == "+":
    print("{0:.1f}".format(float(x) + float(z)))
elif y == "-":
    print("{0:.1f}".format(float(x) - float(z)))
elif y == "*":
    print("{0:.1f}".format(float(x) * float(z)))
else:
    print("{0:.1f}".format(float(x) / float(z)))
