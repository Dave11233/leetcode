s = input()
# print(s)
s = s.replace("{", "(")
s = s.replace("}", ")")
s = s.replace("[", "(")
s = s.replace("]", ")")
# print(s)
print(eval(s))