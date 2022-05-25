def fib_generator(n):
    start = 0
    end = 1
    while n != 0:
        yield start
        step = start + end
        start = end
        end = step
        n -= 1


def fib_list(n):
    result = [0, 1]
    for i in range(n - 2):
        result.append(result[i] + result[i + 1])
    return result


my_fib_generator = fib_generator(9)
my_fib_list = fib_list(9)

print('List', my_fib_list)
for i in my_fib_generator:
    print('Generator', i)
