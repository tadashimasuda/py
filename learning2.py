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



