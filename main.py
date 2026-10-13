"""
1. Create
def add(a, b)
"""
#add
def add(a,b):
    try:
     return f'Sum: {a+b}'
    except:
       raise(ValueError)
print(add(10,20))

#sub
def sub(a,b):
    try:
     return f'Substract: {a-b}'
    except:
       raise(ValueError)
print(sub(10,20))

#multiply
def mul(a,b):
    try:
     return f'Multiply: {a*b}'
    except:
       raise(ValueError)
print(mul(10,20))

#divison
def div(a,b):
    try:
     return f'Div: {a/b}'
    except:
       raise(ValueError)
print(div(10,20))

#2. Create a function that determines whether a number is even or odd.
def odd_even(n):
    try:
        if n % 2 == 0:
            print(f'{n} is even')
        else:
            print(f'{n} is odd')
    except Exception as e:
        print(f'Something went wrong: {e}')


n = int(input('Enter the number: '))
odd_even(n)

#3. Create a function that returns the largest of three numbers without using max().
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


def largest(a, b, c):
    try:
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    except Exception as e:
       print(e)


print("Largest:", largest(a, b, c))

#4. Create a function that calculates factorial.
try:
    n = int(input('Enter the number for factorial: '))

    def factorial(n):
        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

    print(f'Factorial of {n} is {factorial(n)}')

except Exception as e:
    print(f'Something went wrong: {e}')


factorial(n)

#5. Create a function that checks whether a number is prime.
try:
    n = int(input('Enter the number: '))

    def is_prime(n):
        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    if is_prime(n):
        print(f'{n} is a prime number')
    else:
        print(f'{n} is not a prime number')

except Exception as e:
    print(f'Something went wrong: {e}')
      
#6. Create
#def calculate_discount(price, discount=10)
#where the default discount is 10%.
try:
    price = int(input('Price of the product: '))
    def calculate_discount(price, discount=10):
        discount_amount = price * discount / 100
        final_price = price - discount_amount
        return final_price
except Exception as e:
    print(e)


print(calculate_discount(1000))

#7. Create a function that accepts a list and returns its sum without using sum().

def sum_list(numbers):
    add = 0
    for i in numbers:
        add+=i
    print(add)

sum_list([1,2,3])

#8. Create a function that accepts a string and returns the number of vowels.
def count_vowels(word):
    count = 0
    for i in word:
        if i in 'aeiouAEIOU':
            count+=1
        else:
            continue
    print(f'number of vowels in {word} is/are {count}.')

count_vowels('ankita')

#9. Create a function that accepts a string and determines whether it is a palindrome.

def if_palindrome(word):
    if word == word[::-1]:
        print(f'{word} is palindrome')
    else:
        print(f'{word} is not palindrome')

if_palindrome('mom')
if_palindrome('hello')

#10. Create a function that accepts
'''name
age
course
and returns a formatted student profile.
'''

def student_profile(*args):
    name = args[0]
    age = args[1]
    course = args[2]

    profile = f'''
    Student Profile
    ---------------
    Name:{name}
    Age:{age}
    Course:{course}
'''
    return profile

print(student_profile('Ankita',23,'python'))


"""
## Difference Between `print()` and `return` in Python

### 1. Function using `print()`

```python
def add(a, b):
    print(a + b)

x = add(10, 20)
print(x)
```

**Output:**
```text
30
None
```

**Explanation:**
- `print(a + b)` displays the sum on the screen.
- The function does not explicitly return a value.
- Therefore, Python automatically returns `None`, and `x` stores `None`.

### 2. Function using `return`

```python
def add(a, b):
    return a + b

x = add(10, 20)
print(x)
```

**Output:**
```text
30
```

**Explanation:**
- `return a + b` sends the sum back to the caller.
- The variable `x` stores the returned value, which is `30`.

### 3. Why is `return` useful?

```python
def add(a, b):
    return a + b

x = add(10, 20)
print(x * 2)
```

o/p
```text
60
```

The `return` statement allows us to store and reuse the result of a function. Here, the function returns `30`, which is stored in `x`. We can then multiply it by `2` to get `60`.

If we used `print()` instead of `return`, `x` would contain `None`, and multiplying it by `2` would raise a `TypeError`.

`print()` displays information on the screen, whereas `return` sends a value back to the caller so that it can be stored, reused, or used in further calculations.
"""