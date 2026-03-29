s=set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))

# python cosiders 20==20.0 regardless of their different datatypes