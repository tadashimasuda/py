x = 10

if x < 10:
    print('negative')
elif x == 0:
    print('0')
else:
    print('positive')

y = [1,2,3]
x=1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

is_ok = True

if not is_ok:
    print('hello')

is_empty = None

if is_empty is not None:
    print('None!!')

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count+=1
        continue

    print(count)
    count+=1

print('#######')
# num_list = [1,2,3,4,5]
#
# for num in num_list:
#     print(num)
#
# for num in range(10):
#     print(num)

# for _ in range(10):
#     print(_)

items = ['A','B','C']

for i,item in enumerate(items):
    print(i,item)

print('#######')

days = ['Mon','Tue','Wed']
fruits = ['apple','banana','orange']
drinks = ['coffee','tea','beer']

for day,fruit,drink in zip(days,fruits,drinks):
    print(day,fruit,drink)

d = {'x':100,'y':200}
print(d.items())

for k,v in d.items():
    print(k,':',v)

def add_num(a:int,b:int) -> int:
    return a+b

r = add_num(10,20)
print(r)

def say_something(*args):
    print(args)

say_something('Hi','Mike','Nance')

def say_something2(word,*args):
    print(word,args)

say_something2('Hi','Mike','Nance')

def something(**kwargs):
    print(kwargs)

d = {
    'A':'a',
    'B':'b',
    'C':'c'
}
something(**d)
something(D='d',E='e')

def outer(a,b):

    def plus(c,d):
        return c+d

    r1 = plus(a,b)
    r2 = plus(b,a)
    print(r1+r2)

outer(1,2)

l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words,func):
    for word in words:
        print(func(word))

# def cap_func(word):
#     return word.capitalize()

cap_func = lambda word:word.capitalize()

change_words(l,cap_func)

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print(next(g))
print(next(g))

t = (1,2,3,4,5)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r = [i for i in t if i % 2==0]
print(r)

w = ['mon','tue','wed']
f = ['coffee','milk','water']

d = {x:y for x,y in zip(w,f)}
print(d)



