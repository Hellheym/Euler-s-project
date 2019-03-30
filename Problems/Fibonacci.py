fibonacci_list = [1, 2]
fib = 0
def fibonacci():
    for i in range(1, 1000):
        fib = fibonacci_list[i] + fibonacci_list[i - 1]
        fibonacci_list.append(fib)
        if fib < 4000000:
            continue
        else:
            fibonacci_list.remove(fib)
            break
fibonacci()
print(fibonacci_list)
result = 0
for i in fibonacci_list:
    if i % 2 == 0:
        result += i
print(result)