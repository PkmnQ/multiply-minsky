import sys
f = open(sys.argv[1],"r")
code = f.read()
f.close()
if code == "":
	code = "1 2 0"
code = code.split(" ")
reg = 1
i = 0
while i < len(code):
	reg *= int(code[i])
	div = int(code[i+1])
	if reg % div == 0:
		reg //= div
		i = int(code[i+2])*3
	else:
		i += 3
print(reg)
