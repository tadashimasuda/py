print('Hi') #Hi
print('Hi','Mike',sep=',',end='.\n') #Hi,Mike.

print('I don\'t no') #I don't no  \ 文字列として認識

print(r'C:\name\name') #C:\name\name

print("""
line1
line2
line3
""")

print('Hi' * 5)

text = 'python'
print(text)
print(text[0])
print(text[5])
print(text[-1])
print(text[0:2])

print(text[1:])
print(text[:3])

# text[0] ='j'
# print(text)

text = 'My name is Mike. Hi Mike.'
print(text)

print(text.find('Mike'))
print(text.rfind('Mike'))
print(text.count('Mike'))
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.replace('Mike', 'Nancy'))

l = [1,2,3,4,5]

print(l)
print(l[1])
print(l[::2])

text = list('abcdefg')
print(text)

l = [1,2,3,4,5,6,7,8,9]

l.append(10)

l.insert(2,20)
print(l)

print(l.pop())
print(l.pop(0))

del l[0]
print(l)

l.remove(9)
print(l)

########################
r = [1,2,3,4,5,1,2,3]

print(r.index(3,3)) #index(探したい値,開始位置)

r.sort()
print(r)

r.sort(reverse=True)
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

