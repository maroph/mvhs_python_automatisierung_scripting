# https://inventwithpython.com/blog/22-examples-of-recursive-functions.html
# Sample: recursive function

log_calls = True
# log_calls = False

def fibonacci(nthNumber: int) -> int:
    print(f'fibonacci({nthNumber}) called.') if log_calls else None
    if nthNumber == 0:
        # base case
        print(f'Base case fibonacci({nthNumber}) returning 0.') if log_calls else None
        return 0
    if nthNumber == 1 or nthNumber == 2:
        # base case
        print(f'Base case fibonacci({nthNumber}) returning 1.') if log_calls else None
        return 1

    # recursive case
    print(f'Calling fibonacci({nthNumber - 1})') if log_calls else None
    result1 = fibonacci(nthNumber - 1)
        
    print(f'Calling fibonacci({nthNumber - 2})') if log_calls else None
    result2 = fibonacci(nthNumber - 2)

    result = result1 + result2
    print(f'Call to fibonacci({nthNumber}) returning {result}.') if log_calls else None
    return result

if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))
