
fileptr = open("1.txt", "r", encoding="utf-8")

content = fileptr.read(10)

print(type(content))

print(content)

fileptr.close()
