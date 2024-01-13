f = open("sample.txt", "w+")
f.write("BEGINNING")
f.writelines("\nFIRST LINE\nSECOND LINE\n")
l = ['THIRD LINE\n', 'END']
f.writelines(l)
f.close()

file = open("sample.txt", 'r')
r = file.read()
print(r)
file.close()