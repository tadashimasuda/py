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