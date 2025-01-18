x = 1
x = x+1
x += x 
x+x
print(x)

while x > 0:
    print("err")
    x-=1

print("x=0")

'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
'''
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')