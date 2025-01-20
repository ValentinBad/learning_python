f = open("TheFile.txt" , "r")

#print(f.read())
'''print(f.readline())
print(f.readline())
'''
for x in f:
    print(x)

print("____________")

t=open("TheFile.txt", "rt")
print(t.read(5))

f.close
t.close

out = open("/home/valentin/Документы/secondfile.txt" , "w")
out.write("I'm don't cleaaar")
out.close

out = open("/home/valentin/Документы/secondfile.txt" , "r")
print(out.read())
out.close

out = open("/home/valentin/Документы/secondfile.txt" , "a")
out.write(" 2=2")
out.close

out = open("/home/valentin/Документы/secondfile.txt" , "r")
print(out.read())
out.close
